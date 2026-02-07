import pandas as pd
import matplotlib.pyplot as plt
import numpy

df = pd.read_csv("Training/sales_data.csv")

df["Profit"] = df.Sales - df.Cost

df["SalesGrowthRate"] = df["Sales"].pct_change() * 100
df["CostGrowthRate"] = df["Cost"].pct_change() * 100
df["ProfitGrowthRate"] = df["Profit"].pct_change() * 100

# print(df["SalesGrowthRate"])
# print(df["CostGrowthRate"])
# print(df["ProfitGrowthRate"])

print(df["Sales"])
print(df["Cost"])
print(df["Profit"])

lowestProfitMonth = df.Month[df["Profit"].idxmin()]
averageProfit = df["Profit"].mean()
highestProfitMonth = df.Month[df["Profit"].idxmax()]

print("Average Profit:", averageProfit)
print("Lowest Profit Month:", lowestProfitMonth, df["Profit"].min())
print("Highest Profit Month:", highestProfitMonth, df["Profit"].max())

# plt.figure(figsize=(10, 5))

# plt.plot(df.Month, df["Sales"], marker="o", label="Sales")
# plt.plot(df.Month, df["Cost"], marker="o", label="Cost")
# plt.plot(df.Month, df["Profit"], marker="o", label="Profit")
# plt.axhline(averageProfit, color="green", linestyle="--")

# plt.grid(True)
# plt.show()

plt.figure(figsize=(10, 5))

plt.plot(df.Month, df["SalesGrowthRate"], marker="o", label="Sales")
plt.plot(df.Month, df["CostGrowthRate"], marker="o", label="Cost")
plt.plot(df.Month, df["ProfitGrowthRate"], marker="o", label="Profit")

plt.grid(True)
plt.show()

# plt.figure(figsize=(10, 5))

# plt.bar(df.Month, df["ProfitGrowthRate"])
# plt.axhline(0, color="red", linestyle="--")

# plt.grid(True)
# plt.show()
