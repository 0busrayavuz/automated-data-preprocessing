# AI-Supported Automated Data Preprocessing System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Overview
**Automated Data Preprocessing** is an AI-powered system designed to automate the data cleaning and preparation process, which is one of the most time-consuming stages in data analytics.

Developed as a graduation project for **Bandırma Onyedi Eylül University**, this system analyzes structured datasets (CSV, TXT, XLSX) to detect missing values, outliers, and format inconsistencies using Machine Learning algorithms. Unlike traditional tools, it offers an **explainable recommendation engine**, allowing users to approve or modify cleaning strategies before execution.

## 🚀 Key Features
* **📂 Multi-Format Support:** Automatically reads and processes **CSV, TXT, and XLSX** files.
* **🧠 AI-Driven Detection:** Utilizes advanced algorithms for anomaly detection:
    * **KNN Imputer:** For intelligent missing value completion.
    * **Isolation Forest & LOF:** For robust outlier detection.
* **💡 Recommendation Engine:** Provides explainable preprocessing suggestions (e.g., *"Clean with Mean Imputation"*) instead of "black-box" changes.
* **⚡ Automated Pipeline:** Automatically applies selected cleaning steps and logs every action for reproducibility.
* **📊 Quality Reporting:** Generates downloadable **PDF/HTML reports** showing data quality metrics before and after cleaning.

## 🛠️ Tech Stack
This project is built using the following technologies:

| Category | Tool/Library | Description |
| :--- | :--- | :--- |
| **Language** | Python | Core programming language |
| **UI Framework** | Streamlit | Web-based interactive user interface |
| **Data Manipulation** | Pandas, NumPy | Data reading and processing |
| **Machine Learning** | Scikit-learn | KNN, LOF, Isolation Forest algorithms |
| **Visualization** | Matplotlib, Seaborn | Data distribution plotting |
| **Reporting** | ReportLab / WeasyPrint | PDF report generation |

## ⚙️ Workflow
The system follows a modular "Human-in-the-loop" pipeline approach:

1.  **Data Ingestion:** User uploads a dataset (CSV/TXT/Excel).
2.  **Analysis:** System scans for missing values, outliers, and format errors.
3.  **Recommendation:** The engine suggests optimal cleaning strategies.
4.  **Execution:** User reviews and approves the suggestions; the system applies the fixes.
5.  **Reporting:** A final quality report is generated and the clean dataset is downloaded.

## 💻 Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/0busrayavuz/automated-data-preprocessing.git](https://github.com/0busrayavuz/automated-data-preprocessing.git)
    cd automated-data-preprocessing
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

## 🎓 Academic Information
This project was developed within the scope of the **Computer Engineering** program at **Bandırma Onyedi Eylül University**.

* **Course:** BLM 4121 - Engineering Design
* **Student:** Büşra Yavuz
* **Advisor:** Dr. Arzum KARATAŞ
* **Date:** January 2026

---
*Disclaimer: This tool is a prototype developed for academic purposes and focuses on structured tabular data.*
