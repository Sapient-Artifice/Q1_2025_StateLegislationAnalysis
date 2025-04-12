import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fig, ax = plt.subplots(figsize=(16, 18))
x_offsets = {state: 0 for state in state_order}
bar_height = 0.8
used_labels = set()

for _, row in theme_segment_data.iterrows():
    state = row['State']
    y = y_positions[state]
    width = row['Count']
    if width <= 0:
        continue
    x = x_offsets[state]
    label = row['Top 3 Keywords']
    color = keyword_colors[label]

    show_label = label if label not in used_labels else None
    used_labels.add(label)

    ax.add_patch(Rectangle(
        (x, y - bar_height / 2),
        width,
        bar_height,
        color=color,
        edgecolor='white',
        label=show_label
    ))

    x_offsets[state] += width

# Axis and title
ax.set_yticks(range(len(state_order)))
ax.set_yticklabels(state_order)
ax.set_xlabel("Number of AI-Related Bills Introduced")
ax.set_title("AI Legislative Themes by State (2025)", fontsize=16)
ax.set_xlim(0, bill_totals.max() * 1.1)
ax.set_ylim(-0.5, len(state_order) - 0.5)
ax.invert_yaxis()
ax.tick_params(axis='x', bottom=True, top=False)
ax.tick_params(axis='y', left=False, right=False)

# Legend
legend_handles = [
    Rectangle((0, 0), 1, 1, color=keyword_colors[kw]) for kw in used_labels
]
ax.legend(legend_handles, used_labels, title="Theme Clusters (Top 3 Keywords)", bbox_to_anchor=(1.01, 1), loc='upper left')

plt.tight_layout()
plt.show()
