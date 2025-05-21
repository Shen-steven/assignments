import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 讀取資料
df = pd.read_excel("DATA_Kiss_count_gender_and_IQ (2).xlsx")
df.columns = df.columns.str.strip()
df = df.dropna(subset=['Kiss Count', 'Age of First Kiss'])

# 建立年齡分組（例如：<=16, 17–19, 20+）
bins = [0, 16, 19, 30]
labels = ['Early (≤16)', 'Middle (17–19)', 'Late (≥20)']
df['First_Kiss_Group'] = pd.cut(df['Age of First Kiss'], bins=bins, labels=labels)

# 畫圖：以組別畫出接吻次數分佈
plt.figure(figsize=(8, 5))
sns.boxplot(x='First_Kiss_Group', y='Kiss Count', data=df, palette='pastel')
sns.stripplot(x='First_Kiss_Group', y='Kiss Count', data=df, color='black', alpha=0.4, jitter=True)

plt.title("Kiss Count by Age of First Kiss Group")
plt.xlabel("Age of First Kiss Group")
plt.ylabel("Kiss Count")
plt.tight_layout()
plt.savefig("kisscount_vs_firstkiss_boxplot_grouped.png", dpi=300)
plt.show()
