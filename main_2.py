import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv(r"ENTER FILE PATH")
print(data)

group_data1 = data.groupby(['Month', 'Day'])['Annual growth percentage'].sum().unstack()
group_data1.plot(kind='bar', figsize=(10,6), colormap='coolwarm')
plt.xlabel('Month')
plt.ylabel('Annual growth %')
plt.title('Stock return Analysis')

plt.show()

plt.scatter(data['Date'], data["Daily Return"], color='black', marker="o")
plt.grid(True)

plt.show()