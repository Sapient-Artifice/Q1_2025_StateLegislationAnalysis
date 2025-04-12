import matplotlib.pyplot as plt

# NOTE: Add your dataframe loading logic here if needed
# Map conflict risk to numeric score and color
risk_score_map = {"Low": 1, "Medium": 2, "High": 3}
risk_color_map = {1: "#b7e4c7", 2: "#ffe066", 3: "#e63946"}

# Add numeric and color columns
df_conflict_viz["Risk Score"] = df_conflict_viz["Conflict Risk"].map(risk_score_map)
df_conflict_viz["Color"] = df_conflict_viz["Risk Score"].map(risk_color_map)

# Plot bubble chart
plt.figure(figsize=(12, 8))
plt.scatter(
    df_conflict_viz["State Bills"],
    df_conflict_viz["Federal Bills"],
    s=df_conflict_viz["Risk Score"] * 500,  # scale bubble size
    c=df_conflict_viz["Color"],
    alpha=0.8,
    edgecolors="gray",
    linewidths=1
)

# Add labels to each point
for i, row in df_conflict_viz.iterrows():
    plt.text(
        row["State Bills"] + 1,
        row["Federal Bills"] + 0.2,
        row["Policy Topic"],
        fontsize=9,
        ha='left',
        va='center'
    )

# Axis labels and title
plt.xlabel("Number of State Bills")
plt.ylabel("Number of Federal Bills")
plt.title("AI Policy Conflict Landscape – Bubble Plot (Q1 2025)")
plt.grid(True)
plt.tight_layout()
plt.show()
