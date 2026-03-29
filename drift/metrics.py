import numpy as np
from scipy.stats import ks_2samp

def ks_test(ref, cur):
    stat, p_value = ks_2samp(ref, cur)
    return stat, p_value
def calculate_mean_diff(ref, cur):
    return np.mean(cur) - np.mean(ref)

def calculate_var_diff(ref, cur):
    return np.var(cur) - np.var(ref)

def percent_change(ref, cur):
    return ((np.mean(cur) - np.mean(ref)) / np.mean(ref)) * 100


def calculate_psi(ref, cur, bins=10):
    import numpy as np

    ref = np.array(ref)
    cur = np.array(cur)

    # Create bins based on reference
    breakpoints = np.percentile(ref, np.linspace(0, 100, bins + 1))

    # Avoid duplicate bin edges
    breakpoints = np.unique(breakpoints)

    ref_counts, _ = np.histogram(ref, bins=breakpoints)
    cur_counts, _ = np.histogram(cur, bins=breakpoints)

    ref_perc = ref_counts / len(ref)
    cur_perc = cur_counts / len(cur)

    # Avoid division by zero
    ref_perc = np.where(ref_perc == 0, 0.0001, ref_perc)
    cur_perc = np.where(cur_perc == 0, 0.0001, cur_perc)

    psi = np.sum((cur_perc - ref_perc) * np.log(cur_perc / ref_perc))

    return psi