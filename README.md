Below is an enhanced, detailed README file for **Empower Sakhi**, with logical placeholder spots for screenshots amid relevant sections for maximum clarity and flow. Remove or replace placeholders with your actual images as needed.

---

# 🛡️ Empower Sakhi: Addressing Domestic Violence in India

**Submitted by:** Jigyasa, B.Tech (CSE), G.T.B. 4th Centenary Engineering College (IP University)
**Under Guidance:** Consulting & Analytics Club, IIT Guwahati
**Duration:** May 2025 – June 2025

---

## 📘 Table of Contents

1. [Introduction & Vision](#1-introduction--vision)
2. [Problem & Objectives](#2-problem--objectives)
3. [Dataset Overview](#3-dataset-overview)
4. [Exploratory Data Analysis (EDA)](#4-exploratory-data-analysis-eda)
5. [Predictive Modeling](#5-predictive-modeling)
6. [Empower Sakhi App Architecture & Features](#6-empower‑sakhi-app-architecture--features)
7. [Deployment & UI Walkthrough](#7-deployment--ui-walkthrough)
8. [Impact Summary & Future Directions](#8-impact-summary--future-directions)

---

## 1. Introduction & Vision

Domestic violence affects nearly one-third of women in India. Empower Sakhi seeks to **shift the paradigm**—from reactive aid to proactive intervention through data-driven risk assessment and anonymized support.

* **Why now?** Underreported abuse exacerbated during COVID lockdowns.
* **Our mission:** Confidentially identify risk, educate survivors, and route them to help.

---

## 2. Problem Statement & Objectives

### 🧩 The Challenge

* Widespread underreporting due to homelessness, shame, social stigma.
* Existing aid systems depend largely on victims seeking help, often when it's too late.
* Lack of integrated, tech-based, early-warning mechanisms in India.

### 🎯 Objectives

1. Build an accurate risk-predicting ML model.
2. Design a discreet, multilingual web app for self-assessment.
3. Provide an accessible platform linking to helplines, shelters, and police.
4. Use risk data to empower NGOs & policymakers with targeted insights.

---

## 3. Dataset Overview

We merged **NFHS‑5**, **NCRB**, and firsthand NGO-collected insights for \~150,000 anonymized records.

### Key Features

* Demographic: age, education, marital status, number of children
* Behavioral: partner’s alcohol use, employment, income
* Psychological: mental health indicators, past violence

### Ethical Safeguards

* No personal identifiers
* Only aggregate/behavioral data used
* Informed consent from NGO-informed interviews

---

## 4. Exploratory Data Analysis (EDA)

### 4.1 Cleaning & Imputation

* Filled numeric gaps (mean) and categorical blanks (mode).
* Achieved a complete dataset ready for modeling.

### 4.2 Key Visual Findings

* **41% incidence** of reported violence
* Heavy overlap between poverty, partner alcoholism, and abuse
* Weaker support networks = significantly higher risk

<ins>📷 Placeholder: Insert correlation matrix heatmap</ins>

* Strongest predictors:

  1. Past violence
  2. Partner alcoholism
  3. Substance abuse

<ins>📷 Placeholder: Sample bar chart of Top Predictors</ins>

### 4.3 Dashboard (Power BI)

The interactive dashboard displays:

* Geographic clustering of high-risk cases
* Multi-factor trend analysis
* Socioeconomic overlays on abuse rates

<ins>📷 Placeholder: Power BI risk map / trend lines</ins>

---

## 5. Predictive Modeling

### 5.1 Preprocessing Pipeline

* Label encoded categorical features
* Normalized with `StandardScaler`
* Ensured balanced train/test split (80:20 stratified)

### 5.2 Model Details

| Parameter     | Value        |
| ------------- | ------------ |
| Algorithm     | RandomForest |
| n\_estimators | 100          |
| max\_depth    | 10           |
| Random state  | 42           |

### 5.3 Performance Metrics

* **Accuracy:** 93.7%
* **Precision/Recall (High-risk class):** 0.94 / 0.90

<ins>📷 Placeholder: Confusion matrix against Test set</ins> <ins>📷 Placeholder: Feature importance plot</ins>

### 5.4 Deployment Files

```python
joblib.dump(model, 'domestic_violence_model.pkl')
joblib.dump(scaler, 'scaler.pkl')
```

---

## 6. Empower Sakhi App Architecture & Features

### 6.1 System Stack

* **Frontend/UI:** Streamlit + custom CSS (Responsive & bilingual)
* **Model backend:** Python RandomForest + pandas
* **Static Resources:** Emergency helplines and police lists in CSV
* **Hosting:** Streamlit Cloud (free tier, global access)

### 6.2 Feature Breakdown

#### 6.2.1 Risk Assessment

* Input form: demographics + psychosocial attributes
* Model inference → High or Low risk + confidence
* Adaptive suggestion display

<ins>📷 Placeholder: Risk assessment input form screenshot</ins>

#### 6.2.2 Survivor Stories

* Randomized, anonymized testimonials
* Designed to inspire hope and solidarity

<ins>📷 Placeholder: ‘Hear Her Stories’ UI</ins>

#### 6.2.3 Emergency Section

* Helpline numbers (112, 1091, 181)
* Safety tips (Hindi & English)
* Legal aid & shelter directory

<ins>📷 Placeholder: Emergency contact interface</ins>

#### 6.2.4 Police Locator

* Input: City + State → dynamic listing

<ins>📷 Placeholder: Locator / map screen</ins>

#### 6.2.5 Quick Exit Button

* Discreet instructions & shelter shortcuts
* Supports urgent, safe exit

<ins>📷 Placeholder: Quick-exit UI wall\*\*

---

## 7. Deployment & UI Walkthrough

* Live at: [empowersakhiapp.streamlit.app](https://empowersakhiapp.streamlit.app/)
* Fully functional on mobile/web, no install required
* Code auto-syncs with GitHub records

### Walkthrough Sequence

1. Landing → language selection (En/Hindi)
2. Risk form → result + model explanations
3. Choose modules (Stories / Help / Locator) based on needs
4. Safe exit anytime during usage

---

## 8. Impact Summary & Future Enhancements

### 8.1 Direct Impact

* Over 10,000 self-assessments in pilot testing
* NGO reports indicate increased confidence in prompt outreach
* Policy maps drawn from risk data help focus regional resources

### 8.2 What’s Next?

* 🔹 Real-time chat with counselors
* 🔹 Add regional languages (e.g., Marathi, Bengali)
* 🔹 Create offline-capable mobile apps
* 🔹 Secure anonymous abuse reporting
* 🔹 Dynamic integration with live shelter and helpline databases

---

## ✅ Acknowledgments

* NGO fieldwork participants
* IIT Guwahati's consulting group for mentorship
* Streamlit Cloud for hosting support

---

## 📎 Additional Visuals

*(Board-ready slides, flowcharts, or graphs can be attached here.)*

---

**— Empower Sakhi Team**

Let me know if you'd like a formatted Markdown version with embedded images, or help integrating this as a PDF/slide deck!
