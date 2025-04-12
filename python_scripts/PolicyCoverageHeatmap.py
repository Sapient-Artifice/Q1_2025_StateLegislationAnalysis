import matplotlib.pyplot as plt
import seaborn as sns
# NOTE: Add your dataframe loading logic here if needed
from matplotlib.patches import Patch

# Define full topic list (as used in previous comparison)
full_topics = [
    "Deepfakes / Misinformation",
    "Automated Hiring / Employment",
    "Healthcare & Pandemic Preparedness",
    "Generative AI & LLMs",
    "Algorithmic Discrimination",
    "Facial Recognition / Biometrics",
    "Autonomous Systems / Vehicles",
    "AI Governance / Infrastructure",
    "AI in Schools / Curriculum",
    "Robocalls / Communications",
    "Economic Regulation",
    "Workforce / Education",
    "Other / Emerging Uses"
]

# Generate new matrix for heatmap
heatmap_df = pd.DataFrame(index=full_topics)
heatmap_df["Federal"] = 0
heatmap_df["State"] = 0

# Fill in new federal counts
for topic, count in topic_counts.items():
    heatmap_df.loc[topic, "Federal"] = count

# Preserve previous state-level counts (approximate, from earlier analysis)
state_estimates = {
    "Deepfakes / Misinformation": 46,
    "Automated Hiring / Employment": 35,
    "Healthcare & Pandemic Preparedness": 12,
    "Generative AI & LLMs": 8,
    "Algorithmic Discrimination": 29,
    "Facial Recognition / Biometrics": 22,
    "Autonomous Systems / Vehicles": 18,
    "AI Governance / Infrastructure": 8,
    "AI in Schools / Curriculum": 21,
    "Robocalls / Communications": 26,
    "Economic Regulation": 14,
    "Workforce / Education": 35,
    "Other / Emerging Uses": 70
}

for topic, count in state_estimates.items():
    if topic in heatmap_df.index:
        heatmap_df.loc[topic, "State"] = count

# Map bill counts to symbolic coverage levels for plotting
def get_symbolic_coverage(count):
    if count >= 3:
        return "✅"
    elif count == 1 or count == 2:
        return "⚠️"
    else:
        return "❌"

symbolic_df = heatmap_df.copy()
symbolic_df["Federal"] = symbolic_df["Federal"].apply(get_symbolic_coverage)
symbolic_df["State"] = symbolic_df["State"].apply(get_symbolic_coverage)

# Prepare numeric version for heatmap background
numeric_df = symbolic_df.replace({"✅": 2, "⚠️": 1, "❌": 0})

# Create heatmap with annotations
plt.figure(figsize=(12, 7))
sns.heatmap(numeric_df, annot=heatmap_df.astype(int), fmt='d', cmap="YlGnBu", cbar=False, linewidths=0.5, linecolor='gray')
plt.title("AI Policy Coverage Heatmap – Federal vs. State (Q1 2025)\nColor: Coverage Strength · Text: # of Bills")
plt.xticks(rotation=0)
plt.yticks(rotation=0)

# Legend for coverage levels
legend_elements = [
    Patch(facecolor='#08306b', edgecolor='gray', label='✅ Strong Coverage (3+)'),
    Patch(facecolor='#6baed6', edgecolor='gray', label='⚠️ Partial Coverage (1–2)'),
    Patch(facecolor='#f7fbff', edgecolor='gray', label='❌ No Coverage')
]
plt.legend(handles=legend_elements, bbox_to_anchor=(1.02, 1), loc='upper left', title="Coverage Key")

plt.tight_layout()
plt.show()
