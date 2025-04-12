# Reuse the same categorization logic for state summaries
def categorize_state_ai_bill(summary):
# NOTE: Add your dataframe loading logic here if needed
    summary = summary.lower()
    categories = []

    if any(kw in summary for kw in ["defense", "terrorism", "homeland", "border", "threat"]):
        categories.append("National Security")
    if any(kw in summary for kw in ["research", "framework", "infrastructure", "resource", "standard", "strategy"]):
        categories.append("AI Governance / Infrastructure")
    if any(kw in summary for kw in ["ethics", "accountability", "transparency", "consumer", "protection", "disclosure"]):
        categories.append("AI Ethics / Consumer Protections")
    if any(kw in summary for kw in ["deepfake", "synthetic media", "misinformation", "scam"]):
        categories.append("Deepfakes / Misinformation")
    if any(kw in summary for kw in ["health", "pandemic", "medical", "hospital"]):
        categories.append("Healthcare & Pandemic Preparedness")
    if any(kw in summary for kw in ["price", "pricing", "collusion", "economic"]):
        categories.append("Economic Regulation")
    if any(kw in summary for kw in ["workforce", "education", "training", "curriculum"]):
        categories.append("Workforce / Education")
    if any(kw in summary for kw in ["robocall", "communication", "voice", "telemarketing"]):
        categories.append("Robocalls / Communications")
    if any(kw in summary for kw in ["agriculture", "farming", "environment", "climate"]):
        categories.append("Agriculture / Environment")
    if not categories:
        categories.append("Other / Emerging Uses")

    return ", ".join(categories)

# Apply categorization
df_state["AI Topic"] = df_state["Summary"].apply(categorize_state_ai_bill)

# Count topic frequencies
state_topic_counts = df_state["AI Topic"].str.get_dummies(sep=", ").sum().sort_values(ascending=False)

# Combine with federal data
combined_topics = pd.DataFrame({
    "Federal": cleaned_df["AI Topic"].str.get_dummies(sep=", ").sum(),
    "State": state_topic_counts
}).fillna(0).astype(int)

# Show combined for visualization
import matplotlib.pyplot as plt

#combined_topics.plot(kind="bar", figsize=(12, 6))
#plt.title("AI Legislation by Topic – Federal vs. State (Q1 2025)")
#plt.ylabel("Number of Bills")
#plt.xlabel("AI Topic")
#plt.xticks(rotation=45, ha='right')
#plt.grid(axis="y")
#plt.legend(title="Level")
#plt.tight_layout()
#plt.show()


# Normalize counts by converting to percentage of total per level
normalized_topics = combined_topics.copy()
normalized_topics["Federal"] = (normalized_topics["Federal"] / normalized_topics["Federal"].sum() * 100).round(2)
normalized_topics["State"] = (normalized_topics["State"] / normalized_topics["State"].sum() * 100).round(2)

# Plot normalized comparison
normalized_topics.plot(kind="bar", figsize=(12, 6))
plt.title("Normalized AI Legislative Focus by Topic – Federal vs. State (Q1 2025)")
plt.ylabel("Percentage of AI Bills")
plt.xlabel("AI Topic")
plt.xticks(rotation=45, ha='right')
plt.grid(axis="y")
plt.legend(title="Level")
plt.tight_layout()
plt.show()
