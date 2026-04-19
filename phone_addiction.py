import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

print("All libraries imported successfully!")

# Load
df = pd.read_csv('Smartphone_Usage_And_Addiction.csv')
print(df.shape, df.dtypes)

# Check missing values
print(df.isnull().sum())

# Fill missing addiction_level with 'Unknown'
df['addiction_level'] = df['addiction_level'].fillna('Unknown')

# Add age group column
df['age_group'] = pd.cut(df['age'],
    bins=[17,22,27,32,35],
    labels=['18-22','23-27','28-32','33-35'])

# Verify cleaned data
print(df.isnull().sum())
print(df.describe())

# Set style
sns.set_style('darkgrid')
plt.rcParams['figure.figsize'] = (12, 5)

# 1. Addiction level count plot
sns.countplot(data=df, x='addiction_level',
    order=['Mild','Moderate','Severe','Unknown'],
    palette='viridis')
plt.title('Addiction Level Distribution')
plt.show()

# 2. Screen time by addiction level (boxplot)
sns.boxplot(data=df[df['addiction_level']!='Unknown'],
    x='addiction_level', y='daily_screen_time_hours',
    palette='Set2')
plt.title('Screen Time by Addiction Level')
plt.show()

# 3. Correlation heatmap
num_cols = ['age','daily_screen_time_hours','social_media_hours',
    'gaming_hours','sleep_hours','notifications_per_day',
    'app_opens_per_day','addicted_label']
sns.heatmap(df[num_cols].corr(), annot=True,
    cmap='coolwarm', fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

# Group-level stats
print(df.groupby('addiction_level')[[
    'daily_screen_time_hours','sleep_hours',
    'app_opens_per_day']].mean().round(2))

# Chi-square test: gender vs addiction
from scipy.stats import chi2_contingency
ct = pd.crosstab(df['gender'], df['addicted_label'])
chi2, p, dof, exp = chi2_contingency(ct)
print(f"Chi2={chi2:.2f}, p-value={p:.4f}")

# ANOVA: screen time across stress levels
from scipy.stats import f_oneway
groups = [df[df['stress_level']==s]['daily_screen_time_hours']
          for s in ['Low','Medium','High']]
f, p = f_oneway(*groups)
print(f"ANOVA F={f:.2f}, p={p:.4f}")

# Encode categoricals
le = LabelEncoder()
df['gender_enc']       = le.fit_transform(df['gender'])
df['stress_enc']       = le.fit_transform(df['stress_level'])
df['academic_enc']     = le.fit_transform(df['academic_work_impact'])

features = ['age','daily_screen_time_hours','social_media_hours',
    'gaming_hours','work_study_hours','sleep_hours',
    'notifications_per_day','app_opens_per_day',
    'gender_enc','stress_enc','academic_enc']

X = df[features]
y = df['addicted_label']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

print(classification_report(y_test, rf.predict(X_test)))

# Feature importance
fi = pd.Series(rf.feature_importances_, index=features).sort_values(ascending=False)
fi.plot(kind='bar', title='Feature Importance')
plt.show()

# Export summary stats to CSV
summary = df.groupby(['addiction_level','gender']).agg(
    avg_screen=('daily_screen_time_hours','mean'),
    avg_sleep=('sleep_hours','mean'),
    count=('user_id','count')
).round(2).reset_index()
summary.to_csv('addiction_summary.csv', index=False)

# Save all plots as PDF report
from matplotlib.backends.backend_pdf import PdfPages
with PdfPages('eda_report.pdf') as pdf:
    # add your figure calls here
    pdf.savefig(fig1)
    pdf.savefig(fig2)