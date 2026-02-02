# AI-Supported Automated Data Preprocessing System

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Overview
[cite_start]**Automated Data Preprocessing** is an AI-powered system designed to automate the data cleaning and preparation process, which is one of the most time-consuming stages in data analytics[cite: 13, 16].

[cite_start]Developed as a graduation project for **Bandırma Onyedi Eylül University**, this system analyzes structured datasets (CSV, TXT, XLSX) to detect missing values, outliers, and format inconsistencies using Machine Learning algorithms[cite: 17, 29]. [cite_start]Unlike traditional tools, it offers an **explainable recommendation engine**, allowing users to approve or modify cleaning strategies before execution[cite: 26, 33].

## 🚀 Key Features
* [cite_start]**📂 Multi-Format Support:** Automatically reads and processes **CSV, TXT, and XLSX** files[cite: 17, 29].
* [cite_start]**🧠 AI-Driven Detection:** Utilizes advanced algorithms for anomaly detection[cite: 31, 60, 61]:
    * **KNN Imputer:** For intelligent missing value completion.
    * **Isolation Forest & LOF:** For robust outlier detection.
* [cite_start]**💡 Recommendation Engine:** Provides explainable preprocessing suggestions (e.g., *"Clean with Mean Imputation"*) instead of "black-box" changes[cite: 33, 110].
* [cite_start]**⚡ Automated Pipeline:** Automatically applies selected cleaning steps and logs every action for reproducibility[cite: 35, 101].
* [cite_start]**📊 Quality Reporting:** Generates downloadable **PDF/HTML reports** showing data quality metrics before and after cleaning[cite: 37, 75].

## 🛠️ Tech Stack
[cite_start]This project is built using the following technologies[cite: 172]:

| Category | Tool/Library | Description |
| :--- | :--- | :--- |
| **Language** | Python | Core programming language |
| **UI Framework** | Streamlit | Web-based interactive user interface |
| **Data Manipulation** | Pandas, NumPy | Data reading and processing |
| **Machine Learning** | Scikit-learn | KNN, LOF, Isolation Forest algorithms |
| **Visualization** | Matplotlib, Seaborn | Data distribution plotting |
| **Reporting** | ReportLab / WeasyPrint | PDF report generation |

## ⚙️ Workflow
[cite_start]The system follows a modular "Human-in-the-loop" pipeline approach[cite: 114, 125]:

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
[cite_start]This project was developed within the scope of the **Computer Engineering** program at **Bandırma Onyedi Eylül University**[cite: 1, 3].

* [cite_start]**Course:** BLM 4121 - Engineering Design [cite: 4]
* [cite_start]**Student:** Büşra Yavuz [cite: 8]
* [cite_start]**Advisor:** Dr. Arzum KARATAŞ [cite: 10]
* [cite_start]**Date:** January 2026 [cite: 11]

---
*Disclaimer: This tool is a prototype developed for academic purposes and focuses on structured tabular data.*