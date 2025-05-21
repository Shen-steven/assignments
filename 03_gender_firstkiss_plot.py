import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("DATA_Kiss_count_gender_and_IQ (2).xlsx")

sns.boxplot(x='Gender', y='Age_of_First_Kiss', data=df)
sns.stripplot(x='Gender', y='Age_of_First_Kiss', data=df, color='black', alpha=0.4, jitter=True)

plt.title('Age of First Kiss by Gender')
plt.savefig('gender_firstkiss_boxplot.png', dpi=300)
plt.show()
