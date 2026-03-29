# 📊 Data Drift Detection System

An end-to-end **Data Drift Detection System** built using Python and Streamlit to monitor changes in data distributions over time.
This project combines **statistical tests, distribution metrics, and visualization** to detect and explain drift in datasets.

---

## 🚀 Live Demo

👉 *(Add your Streamlit link here after deployment)*

---

## 🧠 Problem Statement

In real-world ML systems, data distribution changes over time, leading to **model performance degradation**.
This project helps identify such changes early using statistical and heuristic techniques.

---

## 🔍 Features

* ✅ Detect data drift using:

  * Kolmogorov-Smirnov (KS) Test
  * Population Stability Index (PSI)
  * Mean & Variance comparison
* 📊 Interactive Streamlit dashboard
* 📈 Distribution visualization (Reference vs Current)
* 🎯 Drift scoring system with confidence level
* 🟢🟥 Highlighted drift results
* 📥 Downloadable drift reports (CSV)

---

## ⚙️ Tech Stack

* **Python**
* **Pandas / NumPy**
* **SciPy** (Statistical Testing)
* **Matplotlib** (Visualization)
* **Streamlit** (Dashboard UI)

---

## 🏗️ Project Structure

```
data-drift-system/
│
├── data/
│   ├── reference.csv
│   ├── current.csv
│
├── drift/
│   ├── detector.py
│   ├── metrics.py
│   ├── visualization.py
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚡ How It Works

1. Upload reference and current datasets
2. System computes:

   * Statistical drift (KS Test)
   * Distribution drift (PSI)
   * Heuristic drift (% change)
3. Combines signals using a **weighted scoring system**
4. Outputs:

   * Drift report
   * Confidence score
   * Visual comparisons

---

## 📊 Drift Detection Logic

The system uses a **multi-signal scoring approach**:

* KS Test → Strong statistical signal
* PSI → Distribution shift indicator
* % Change → Business-level signal

Final drift decision is based on a **weighted score**, reducing false positives.

---

## 📈 Example Output

| Feature | Drift Score | Confidence | Drift Detected |
| ------- | ----------- | ---------- | -------------- |
| Age     | 2.5         | 0.56       | ❌ No           |
| Salary  | 2.5         | 0.56       | ❌ No           |

---

## ▶️ Run Locally

```bash
git clone https://github.com/aman-tech45/data-drift-system.git
cd data-drift-system

pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Future Improvements

* 🔥 ML model performance monitoring
* 📡 Real-time data pipeline integration (Kafka/Airflow)
* 📊 Advanced visualizations (KDE, drift heatmaps)
* 🤖 Automated alerts & notifications

---

## 👨‍💻 Author

**Aman Jha**


* Passionate about AI, ML & Data Systems

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
