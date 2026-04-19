# 📱 Smartphone Usage & Addiction Analysis

> A complete end-to-end Data Analysis project exploring behavioral patterns, screen time habits, and addiction trends among **7,500 smartphone users** aged 18–35.

---

## 🗂️ Project Files

| File | Description |
|------|-------------|
| `Smartphone_Usage_And_Addiction.csv` | Raw dataset — 7,500 records, 16 features |
| `addiction_summary.csv` | Aggregated summary stats by addiction level & gender |
| `phone_addiction.py` | Python script — EDA, ML model, visualizations |
| `smartphone_analysis_report.html` | Interactive web report with Chart.js visualizations |
| `smartphone_usage.pbix` | Power BI dashboard file |
| `Microsoft-Power-BI-Storytelling.pptx` | Power BI storytelling presentation |

---

## 📌 Project Overview

This project investigates how smartphone usage patterns relate to addiction, sleep quality, stress, and academic/work performance. The dataset contains **7,500 records** with **16 behavioral features** collected from users aged 18–35.

**Goal:** Identify key drivers of smartphone addiction and build a predictive model to classify addicted vs non-addicted users.

---

## 📊 Key Findings

| Metric | Value |
|--------|-------|
| 📱 Total Users Analyzed | 7,500 |
| 🔴 Addicted Users | 70.8% (5,308 users) |
| ⏱️ Avg Daily Screen Time | 7.5 hours |
| 😴 Avg Sleep Duration | 6.74 hrs/night *(below 7hr healthy threshold)* |
| 📲 Social Media Usage | 3.27 hrs/day (highest category) |
| 🔔 Daily Notifications | ~134 per user |

### Addiction Level Breakdown
| Level | Count | Avg Screen Time | Avg Sleep |
|-------|-------|----------------|-----------|
| Mild | 1,373 | 5.54 hrs | 6.66 hrs |
| Moderate | 2,874 | 8.35 hrs | 6.76 hrs |
| Severe | 2,434 | 8.60 hrs | 6.78 hrs |
| Unknown | 819 | — | — |

### Key Insights
- 🔴 **Severe addiction** users spend **55% more time** on phones than Mild users (8.6 vs 5.5 hrs)
- 😴 **Sleep deprivation** is consistent across all addiction levels — none reach the 7hr healthy threshold
- 👥 **Gender has no significant effect** on screen time (Chi-square test confirmed, p > 0.05)
- 📚 **50% of users** report smartphone usage negatively impacts their academic/work performance
- 🔔 Notification count shows **no meaningful correlation** with stress level

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| 🐍 Python | Data cleaning, EDA, ML model, visualizations |
| 🗃️ SQL | Data querying & aggregation |
| 📊 Power BI | Interactive dashboard & storytelling |
| 🌐 HTML + Chart.js | Web-based interactive report |
| 📦 scikit-learn | Random Forest Classifier |

---

## 🤖 Machine Learning Model

A **Random Forest Classifier** was trained to predict whether a user is addicted (binary classification).

**Features used:**
- Age, daily screen time, social media hours, gaming hours
- Work/study hours, sleep hours
- Notifications per day, app opens per day
- Gender, stress level, academic work impact

**Top Predictors (Feature Importance):**
1. `daily_screen_time_hours`
2. `social_media_hours`
3. `app_opens_per_day`
4. `notifications_per_day`
5. `sleep_hours`

---

## 🗃️ Dataset Schema

| # | Column | Type | Description |
|---|--------|------|-------------|
| 1 | user_id | int | Unique user identifier |
| 2 | age | int | User age (18–35) |
| 3 | gender | string | Male / Female / Other |
| 4 | daily_screen_time_hours | float | Total daily phone usage |
| 5 | social_media_hours | float | Time on social media |
| 6 | gaming_hours | float | Time on gaming |
| 7 | work_study_hours | float | Time on work/study |
| 8 | app_opens_per_day | int | Number of app opens |
| 9 | notifications_per_day | int | Notifications received |
| 10 | sleep_hours | float | Sleep per night |
| 11 | stress_level | string | Low / Medium / High |
| 12 | weekend_screen_time | float | Weekend usage (hrs) |
| 13 | academic_work_impact | string | Yes / No |
| 14 | addiction_level | string | Mild / Moderate / Severe (819 nulls) |
| 15 | addicted_label | int | 1 = Addicted, 0 = Not Addicted |

---

## 🚀 How to Run

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/smartphone-usage-analysis.git
cd smartphone-usage-analysis

# 2. Install dependencies
pip install pandas numpy matplotlib seaborn scikit-learn scipy

# 3. Run the Python analysis
python phone_addiction.py

# 4. Open the HTML report in browser
open smartphone_analysis_report.html
```


## 📬 Connect

If you found this project useful, feel free to ⭐ the repo!

