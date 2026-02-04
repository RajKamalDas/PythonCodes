import pandas as pd
import matplotlib.pyplot as plt
import numpy

df = pd.read_csv("Training\sales_data.csv")

df["Profit"] = df.Sales - df.Cost

df["SalesGrowthRate"] = df["Sales"].pct_change() * 100
df["CostGrowthRate"] = df["Cost"].pct_change() * 100
df["ProfitGrowthRate"] = df["Profit"].pct_change() * 100

plt.figure(figsize=(10, 5))

plt.plot(df.Month, df["Sales"], marker="o", label="Sales")
plt.plot(df.Month, df["Profit"], marker="o", label="Profit")

plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))

print(df["ProfitGrowthRate"])
plt.bar(df.Month, df["ProfitGrowthRate"])
plt.axhline(0, color="red", linestyle="--")

plt.grid(True)
plt.show()
