import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('DataForTable2.1.xls')

print(df.head())

corr = df.corr(numeric_only=True)
print(corr)


plt.figure(figsize=(12, 10))
map = sns.heatmap(corr, annot=True, cmap='', fmt='.2f', robust=True)
plt.title('Heatmap do Nadottins')
plt.show()
