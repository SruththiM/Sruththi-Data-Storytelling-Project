import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/sruththi_lifestyle_dataset.csv")

phase_avg = df.groupby("Phase").mean(numeric_only=True)

phase_avg[["Concentration_Score", "Stress_Level"]].plot(kind="bar")

plt.title("Past vs Present: Concentration & Stress")
plt.xlabel("Phase")
plt.ylabel("Score")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()


