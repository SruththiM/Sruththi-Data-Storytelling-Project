import pandas as pd

df = pd.read_csv("../data/sruththi_lifestyle_dataset.csv")

print("✅ Dataset loaded successfully")
print(df.head())
print("\nShape:", df.shape)
