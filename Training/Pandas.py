import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def printLine():
    for i in range(129):
        print("-", end="")


df = pd.read_csv("nba.csv")

printLine()
print(df.dtypes)
printLine()
print(df[df["Salary"].isnull()])
printLine()

ser = pd.Series(df.Name)
print(ser.loc[3:6])
printLine()