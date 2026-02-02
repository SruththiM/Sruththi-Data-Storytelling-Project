import pandas as pd

df = pd.read_csv("../data/sruththi_lifestyle_dataset.csv")


phase_summary = df.groupby("Phase").mean(numeric_only=True)

print("📊 Phase-wise Comparison\n")
print(phase_summary)
