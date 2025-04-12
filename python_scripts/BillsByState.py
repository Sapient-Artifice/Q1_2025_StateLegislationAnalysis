import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Recreate the pivot table using the cleaned data
# NOTE: Add your dataframe loading logic here if needed
bill_counts_clean = df.pivot_table(index="State", columns="Bill_Type", values="Bill_Number", aggfunc="count", fill_value=0)

# Sort the bill counts by total number of bills per state, descending
bill_counts_sorted_clean = bill_counts_clean.loc[bill_counts_clean.sum(axis=1).sort_values(ascending=False).index]

# Generate the stacked bar chart
fig, ax = plt.subplots(figsize=(16, 10))
bottom = pd.Series([0] * len(bill_counts_sorted_clean), index=bill_counts_sorted_clean.index)

for bill_type in bill_counts_sorted_clean.columns:
    ax.bar(bill_counts_sorted_clean.index, bill_counts_sorted_clean[bill_type], bottom=bottom, label=bill_type)
    bottom += bill_counts_sorted_clean[bill_type]

ax.set_ylabel('Number of Bills')
ax.set_title('2025 State Legislation: Total Bills by State and Bill Type (Sorted, Cleaned)')
ax.legend(title='Bill Type')
ax.set_xticks(range(len(bill_counts_sorted_clean.index)))
ax.set_xticklabels(bill_counts_sorted_clean.index, rotation=90)

plt.tight_layout()
plt.show()

