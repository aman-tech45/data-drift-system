import streamlit as st
import pandas as pd
import os
from drift.detector import detect_drift
from drift.visualization import plot_feature_distribution

st.set_page_config(page_title="Data Drift Detection System", layout="wide")

st.title("📊 Data Drift Detection Dashboard")

# ---- Upload Section ----
st.sidebar.header("Upload Data")

ref_file = st.sidebar.file_uploader("Upload Reference Dataset", type=["csv"])
cur_file = st.sidebar.file_uploader("Upload Current Dataset", type=["csv"])

if ref_file and cur_file:
    ref_df = pd.read_csv(ref_file)
    cur_df = pd.read_csv(cur_file)

    # ---- Data Preview ----
    st.subheader("📌 Data Preview")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Reference Data")
        st.dataframe(ref_df.head())

    with col2:
        st.write("Current Data")
        st.dataframe(cur_df.head())

    # ---- Drift Detection ----
    st.subheader("📊 Drift Report")

    report = detect_drift(ref_df, cur_df)

    # ---- Highlight Drift Rows ----
    def highlight_drift(row):
        if row["drift_detected"]:
            return ["background-color: #ffcccc"] * len(row)  # red
        else:
            return ["background-color: #ccffcc"] * len(row)  # green

    st.dataframe(report.style.apply(highlight_drift, axis=1))

    # ---- Summary Insights ----
    st.subheader("🧠 Summary Insights")

    total_features = len(report)
    drifted = report["drift_detected"].sum()
    moderate = (report["psi_status"] == "moderate_drift").sum()

    st.write(f"✅ Total Features: {total_features}")
    st.write(f"⚠️ Features with Drift: {drifted}")
    st.write(f"📊 Moderate Drift Features: {moderate}")

    # ---- Download Report ----
    st.subheader("⬇️ Download Report")

    csv = report.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download Drift Report",
        data=csv,
        file_name="drift_report.csv",
        mime="text/csv",
    )

    # ---- Visualization ----
    plot_feature_distribution(ref_df, cur_df, output_dir="plots")

    st.subheader("📈 Feature Distributions")

    for col in ref_df.columns:
        img_path = os.path.join("plots", f"{col}_distribution.png")
        if os.path.exists(img_path):
            st.image(img_path, caption=f"{col} Distribution", use_container_width=True)

else:
    st.info("👈 Upload both datasets to begin")