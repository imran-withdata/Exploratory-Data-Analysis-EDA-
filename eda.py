"""EDA script for kc_house_data.csv
Run: python eda.py
"""
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("kc_house_data.csv")
df.describe(include='all').to_csv("summary_statistics.csv")
df.isnull().sum().to_frame("missing_count").to_csv("missing_values.csv")
with open("data_info.txt","w") as f:
    df.info(buf=f)
# Simple plots
plt.figure()
df['price'].hist(bins=50)
plt.title("Histogram of house prices")
plt.xlabel("price")
plt.ylabel("count")
plt.savefig("hist_price.png", bbox_inches="tight")
plt.close()

plt.figure()
plt.scatter(df['sqft_living'], df['price'], s=10)
plt.title("Price vs sqft_living")
plt.xlabel("sqft_living")
plt.ylabel("price")
plt.savefig("scatter_price_sqft_living.png", bbox_inches="tight")
plt.close()

corr = df.select_dtypes(include=['number']).corr()
plt.figure(figsize=(10,8))
plt.imshow(corr, cmap='viridis', aspect='auto')
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.index)), corr.index)
plt.title("Correlation matrix (numeric features) - heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png", bbox_inches="tight")
plt.close()
print('EDA script finished. Outputs saved to current directory.')
