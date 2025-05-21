import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("DATA_Kiss_count_gender_and_IQ (2).xlsx")

sns.regplot(x='IQ', y='Age_of_First_Kiss', data=df, ci=95, scatter_kws={"alpha":0.5})

plt.title('IQ vs Age of First Kiss')
plt.savefig('iq_firstkiss_scatter.png', dpi=300)
plt.show()
