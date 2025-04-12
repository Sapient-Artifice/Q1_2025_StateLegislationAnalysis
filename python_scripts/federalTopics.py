# Define categorization logic based on title keyword patterns
def categorize_ai_bill(title):
# NOTE: Add your dataframe loading logic here if needed
    title = title.lower()
    categories = []

    if any(kw in title for kw in ["defense", "terrorism", "homeland", "border", "threat"]):
        categories.append("National Security")
    if any(kw in title for kw in ["research", "infrastructure", "resource", "standards", "strategy", "code of federal regulations"]):
        categories.append("AI Governance / Infrastructure")
    if any(kw in title for kw in ["ethics", "accountability", "transparency", "consumer", "protection"]):
        categories.append("AI Ethics / Consumer Protections")
    if any(kw in title for kw in ["deepfake", "deceptive media", "scam", "misinformation"]):
        categories.append("Deepfakes / Misinformation")
    if any(kw in title for kw in ["health", "pandemic", "public health", "medical"]):
        categories.append("Healthcare & Pandemic Preparedness")
    if any(kw in title for kw in ["price", "pricing", "grocery", "collusion"]):
        categories.append("Economic Regulation")
    if any(kw in title for kw in ["workforce", "education", "training"]):
        categories.append("Workforce / Education")
    if any(kw in title for kw in ["robocall", "communication", "voice"]):
        categories.append("Robocalls / Communications")
    if any(kw in title for kw in ["agriculture", "farming"]):
        categories.append("Agriculture / Environment")
    if not categories:
        categories.append("Other / Emerging Uses")

    return ", ".join(categories)

# Apply categorization
cleaned_df["AI Topic"] = cleaned_df["Title"].apply(categorize_ai_bill)

# Count category distribution
topic_counts = cleaned_df["AI Topic"].str.get_dummies(sep=", ").sum().sort_values(ascending=False)

# Plot results
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
topic_counts.plot(kind="bar")
plt.title("Federal AI Legislation by Topic – Q1 2025")
plt.ylabel("Number of Bills")
plt.xlabel("AI Topic")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis="y")
plt.show()
