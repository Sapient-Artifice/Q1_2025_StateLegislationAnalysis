import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# AI policy coverage data (bill counts per topic)
data = {
    "Policy Topic": [
        "Deepfakes / Misinformation", "Automated Hiring / Employment", "Healthcare & Pandemic Preparedness",
        "Generative AI & LLMs", "Algorithmic Discrimination", "Facial Recognition / Biometrics",
        "Autonomous Systems / Vehicles", "AI Governance / Infrastructure", "AI in Schools / Curriculum",
        "Robocalls / Communications", "Economic Regulation", "Workforce / Education", "Other / Emerging Uses"
    ],
    "Federal": [2, 1, 3, 1, 1, 0, 2, 5, 0, 2, 1, 2, 4],
    "State": [46, 35, 12, 8, 29, 22, 18, 8, 21, 26, 14, 35, 70]
}

# Create DataFrame
df = pd.DataFrame(data)
df.set_index("Policy Topic", inplace=True)

# Plot heatmap with a continuous color scale
plt.figure(figsize=(12, 7))
sns.heatmap(
    df,
    annot=True,
    fmt='d',
    cmap="YlOrRd",  # continuous color gradient
    linewidths=0.5,
    linecolor='gray',
    cbar_kws={"label": "Number of Bills"}
)

plt.title("AI Policy Coverage Heatmap – Federal vs. State (Q1 2025)", fontsize=14)
plt.xlabel("Jurisdiction")
plt.ylabel("Policy Topic")
plt.xticks(rotation=0)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
