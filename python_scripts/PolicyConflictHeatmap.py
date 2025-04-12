import pandas as pd
import matplotlib.pyplot as plt
# NOTE: Add your dataframe loading logic here if needed
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# Define your AI policy topics and associated conflict risk levels
data = {
    "Policy Topic": [
        "Deepfakes / Misinformation", "Automated Hiring / Employment", "Healthcare & Pandemic Preparedness",
        "Generative AI & LLMs", "Algorithmic Discrimination", "Facial Recognition / Biometrics",
        "Autonomous Systems / Vehicles", "AI Governance / Infrastructure", "AI in Schools / Curriculum",
        "Robocalls / Communications", "Economic Regulation", "Workforce / Education", "Other / Emerging Uses"
    ],
    "Conflict Risk": [
        "High", "Medium", "Medium", "High", "High", "High", "Medium", "Low", "Low", "Medium", "Medium", "Low", "Medium"
    ]
}

# Map the conflict risk levels to numeric values
risk_map = {"Low": 1, "Medium": 2, "High": 3}
df = pd.DataFrame(data)
df["Risk Value"] = df["Conflict Risk"].map(risk_map)
df.set_index("Policy Topic", inplace=True)

# Custom colormap: green (low) → yellow (medium) → red (high)
custom_cmap = LinearSegmentedColormap.from_list("risk_scale", ["#b7e4c7", "#ffe066", "#e63946"])

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
    df[["Risk Value"]],
    annot=df[["Conflict Risk"]].values,
    fmt='',
    cmap=custom_cmap,
    linewidths=0.5,
    linecolor='gray',
    cbar=False
)
plt.title("AI Policy Conflict Risk by Topic (Q1 2025)")
plt.xticks([])
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
