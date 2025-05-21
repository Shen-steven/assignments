import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("DATA_Kiss_count_gender_and_IQ (2).xlsx")

# 畫盒鬚圖
sns.boxplot(x='Gender', y='Kiss_Count', data=df)
sns.stripplot(x='Gender', y='Kiss_Count', data=df, color='black', alpha=0.4, jitter=True)

plt.title('Kiss Count by Gender')
plt.savefig('gender_kiss_boxplot.png', dpi=300)
plt.show()
