import pandas as pd
from drift.metrics import (
    calculate_mean_diff,
    calculate_var_diff,
    percent_change,
    ks_test,
    calculate_psi
)

THRESHOLD = 10  # percentage threshold for drift


def detect_drift(ref_df, cur_df):
    results = []

    for col in ref_df.columns:
        ref = ref_df[col]
        cur = cur_df[col]

        # ---- Statistical Test (KS Test) ----
        ks_stat, p_value = ks_test(ref, cur)
        ks_drift = p_value < 0.05

        # ---- Basic Metrics ----
        mean_diff = calculate_mean_diff(ref, cur)
        var_diff = calculate_var_diff(ref, cur)
        pct_change = percent_change(ref, cur)
        rule_drift = abs(pct_change) > THRESHOLD

        # ---- PSI Calculation ----
        psi_value = calculate_psi(ref, cur)

        # PSI interpretation
        if psi_value < 0.1:
            psi_status = "no_drift"
        elif psi_value < 0.25:
            psi_status = "moderate_drift"
        else:
            psi_status = "high_drift"

        # ---- DRIFT SCORING SYSTEM (TUNED) ----
        score = 0

        # Strong signal → KS Test
        if ks_drift:
            score += 2

        # Medium signal → PSI (tuned weights)
        if psi_value > 0.25:
            score += 1.5
        elif psi_value > 0.1:
            score += 1

        # Weak signal → Rule-based
        if rule_drift:
            score += 1

        # Final decision
        drift_detected = score >= 3

        # Confidence score (0 to 1 scale approx)
        drift_confidence = round(score / 4.5, 2)

        # ---- Store Results ----
        results.append({
            "feature": col,
            "mean_diff": round(mean_diff, 2),
            "var_diff": round(var_diff, 2),
            "percent_change": round(pct_change, 2),
            "ks_p_value": round(p_value, 4),
            "psi": round(psi_value, 4),
            "psi_status": psi_status,
            "rule_drift": rule_drift,
            "ks_drift": ks_drift,
            "drift_score": round(score, 2),
            "drift_confidence": drift_confidence,
            "drift_detected": drift_detected
        })

    return pd.DataFrame(results)