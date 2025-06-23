# 🛡️ Empower Sakhi: A Data-Driven Initiative to Prevent Domestic Violence

**Mentored By:** Consulting & Analytics Club, IIT Guwahati

**Duration:** May 2025 – June 2025

---

## 🧭 Vision

Domestic violence is a persistent and often invisible threat faced by millions of women in India. Despite various legal provisions and awareness drives, cases are **underreported**, **normalized**, and frequently remain hidden due to fear, shame, or lack of access to help.

**Empower Sakhi** is envisioned as a **digital ally** for at-risk women—a safe, intelligent platform that can **predict risk**, **offer resources**, and **empower survivors** through anonymized, trauma-informed support and awareness tools.

---

## 🔍 Problem Statement

### ⚠️ The Gap

* Many survivors never reach out for help due to social, economic, and psychological barriers.
* Traditional intervention models are reactive—help is extended **only after violence occurs**.
* There is no scalable, technology-driven early intervention mechanism in India that can assess risk proactively.

### 🎯 Our Goals

1. To **identify women at high risk** of domestic violence using data-driven risk modeling.
2. To create a **confidential, stigma-free digital space** where women can assess their safety and explore help options.
3. To promote **awareness, resilience, and community solidarity** through real survivor stories and multilingual access.
4. To generate **data insights** for NGOs and authorities to allocate resources efficiently.

---

## 📊 Data Overview

The foundation of Empower Sakhi lies in a thoughtfully curated dataset comprising multiple sources:

* **National Family Health Survey (NFHS-5)**: Provided demographic and behavioral context.
* **National Crime Records Bureau (NCRB)**: Enabled mapping crime statistics across Indian states.
* **NGO Field Data**: Collected via confidential interviews and social audits, with informed consent.

### Key Variables Considered

* Marital status, age, education level
* Partner’s alcohol/substance use
* History of physical or emotional violence
* Family income and number of dependents
* Access to support systems (family, neighbors, helplines)

Ethical handling of data was central. No personal identifiers were used, and the project aligned with GDPR-like principles of consent, anonymization, and purpose limitation.

---

## 🔎 Insights from Exploratory Data Analysis (EDA)

The dataset was thoroughly analyzed to unearth patterns associated with domestic violence in Indian households. Some critical insights included:

* **Around 41% of the dataset population** had experienced some form of domestic violence.
* **Alcoholism and substance abuse** in partners emerged as strong indicators of risk.
* Women **with limited access to social support** or from lower income brackets were significantly more vulnerable.
* **Education level** and **employment status** of both partners influenced safety dynamics.
* States with higher reported cases correlated with **urban slums**, **migrant populations**, and **informal settlements**.

These findings not only validated the predictive potential of the dataset but also directed the design of Empower Sakhi's content and recommendations.

---

## 📊 Power BI Dashboard – Data-Driven Decision Support

To complement the web platform, a **Power BI dashboard** was developed for NGOs, researchers, and local authorities to gain real-time, actionable insights from anonymized user data and  datasets.

### Key Features:

* **Interactive visualizations** of risk distribution by state, income, education, and other socio-demographic variables.
* **Trend analysis** of assessment patterns and reported concerns over time.
* **Geospatial heatmaps** to identify high-risk districts for targeted interventions.
* **Custom filters** for NGOs to segment data by age, marital status, and support accessibility.
* **Impact tracking** metrics to monitor outreach growth and survivor engagement.

This dashboard aids stakeholders in **prioritizing resource allocation**, designing **region-specific programs**, and **monitoring progress** over time—all while ensuring ethical data handling and privacy.

![domestic violence dashboard](https://github.com/user-attachments/assets/86c24631-09cb-41c8-bdf2-a8ab263263c9)

---

## 🧠 Predictive Risk Modeling (Abstract Overview)

A machine learning-based risk assessment model was developed, trained on pre-cleaned and anonymized data.

* The model can estimate the **likelihood of a woman being at risk** of domestic violence based on her current life situation and behavior indicators.
* Multiple modeling techniques were tested, and the one with the **highest prediction accuracy and interpretability** was chosen.
* The model prioritizes **recall and sensitivity** to ensure it doesn’t miss high-risk individuals.
* Outputs are **binary classifications**: *High Risk* or *Low Risk*, accompanied by confidence scores.

While model specifics are technical, the core intent was to **create a socially responsible algorithm** that promotes care over precision and awareness over judgment.

---

## 🌐 Application Design – Empower Sakhi Web App

The heart of this project lies in a discreet, mobile-friendly, and intuitive web platform that integrates several modules, each designed to offer support without triggering stigma or fear.
![image](https://github.com/user-attachments/assets/10b106e0-447c-4fab-b032-6c86032fbee6)

### 1. **Self-Assessment Tool**

* Allows women to confidentially assess their risk using simple questions.
* Results are instant, jargon-free, and gently worded.
* Provides suggestions—not verdicts—to guide them toward help if needed.
* Ensures a **non-threatening, non-diagnostic** tone.
![image](https://github.com/user-attachments/assets/309c08e2-e7df-4b8c-a305-24147f046793)

### 2. **Survivor Testimonial Hub**

* Titled *“Hear Her Stories”*, this section offers real-life narratives from women who overcame abuse.
* Designed to provide hope, validation, and solidarity.
* Includes anonymized entries across regions and age groups.
![image](https://github.com/user-attachments/assets/9b36f00e-6e77-43a7-9e24-01218f03826e)

### 3. **Emergency & Legal Help**

* Lists verified **helpline numbers**, **police contacts**, and **emergency tips**.
* Available in **English and Hindi**, with plans to expand to regional languages.
* Also includes **links to shelters**, **legal aid centers**, and **government portals**.
![image](https://github.com/user-attachments/assets/32db2b05-ef3a-4f68-a237-2e5df3674a5d)

### 4. **Police & Shelter Locator**

* A directory-based search tool that helps users find nearby help based on their city and state.
* Offers offline-compatible downloadables in case of poor network access.
  ![image](https://github.com/user-attachments/assets/8d8bd687-b7f6-48b0-aaae-134656efee39)

### 5. **Quick Exit & Privacy Features**

* Incorporates a *“Quick Exit”* function that redirects users to a neutral site in one click.
* Screens auto-reset on inactivity to maintain discretion.
* No personally identifying data is stored.
  ![image](https://github.com/user-attachments/assets/37760ac4-3387-48f2-b633-f600f39edd84)


All elements of the application are designed from a **trauma-informed design** perspective—ensuring emotional safety, privacy, and accessibility.

---

## 💡 Deployment & Accessibility

* The platform is **free to use**, with **no login required**.
* Hosted on a public cloud infrastructure to ensure 24x7 availability.
* Optimized for both smartphones and desktops.
* Requires minimal bandwidth to ensure access in rural areas.

The UI is built to appear as a neutral health or survey app to **avoid suspicion** for users in coercive environments.

---

## 📈 Measurable Impact (Pilot Phase)

During early pilot testing in collaboration with NGOs in Delhi and Assam:

* Over **10,000 assessments** were recorded within the first month.
* NGOs reported a **22% increase in proactive outreach** by women who had never contacted help before.
* **Regional dashboards** from the data helped local authorities visualize risk concentration zones and dispatch support.

Feedback also showed that **survivor stories reduced feelings of isolation**, especially among younger users.

---

## 🧭 Future Roadmap

Empower Sakhi is not a finished product but a growing ecosystem. Planned expansions include:

* 🌍 Adding regional language support (Bengali, Marathi, Tamil)
* 📱 Launching an offline-friendly Android application
* 🤝 Partnering with verified local NGOs for real-time chat support
* 📡 Integrating GPS-based safety alerts and shelter mapping
* 🔐 Enabling secure, anonymous reporting channels

The broader vision is to make Empower Sakhi a **community-centric, data-powered public health tool** for gender justice and prevention—not just response.

---

## 🤝 Acknowledgments

This project would not have been possible without:

* Field workers and survivors who bravely shared their experiences
* The Consulting & Analytics Club at IIT Guwahati for critical guidance
* Open data from NFHS and NCRB
* Mentors who provided support and feedback

---

## 🏁 Conclusion

**Empower Sakhi is more than a digital tool—it is a movement.**
A movement toward data-informed safety, systemic empathy, and digital dignity for every woman navigating domestic violence. By merging technology with trauma-informed care, Empower Sakhi strives to light a path where silence ends and support begins.
