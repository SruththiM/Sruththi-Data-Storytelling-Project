import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sruththi_lifestyle_dataset.csv")

plt.scatter(df["Study_Hours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()
