import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.cm import get_cmap
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

# Load dataset
df = pd.read_csv("AI_Legislation_State_Tracker_2025.csv")

# Clean and vectorize summaries
custom_stopwords = set([
    'ai', 'artificial', 'intelligence', 'use', 'uses', 'using', 'technology', 'technologies',
    'content', 'generated', 'state', 'require', 'requires', 'bill', 'act', 'section', 'establishes',
    'program', 'commission', 'department', 'public'
])

vectorizer = TfidfVectorizer(stop_words=custom_stopwords, max_features=1000)
X = vectorizer.fit_transform(df['Summary'].fillna(""))
nmf_model = NMF(n_components=6, random_state=42)
W = nmf_model.fit_transform(X)
H = nmf_model.components_

terms = vectorizer.get_feature_names_out()
topic_keywords = [", ".join([terms[i] for i in comp.argsort()[::-1][:3]]) for comp in H]
df['Theme Keywords'] = W.argmax(axis=1).astype(int).map(lambda i: topic_keywords[i])

# Count themes by state
theme_counts = (
    df.groupby(['State', 'Theme Keywords'])
    .size()
    .reset_index(name='Count')
)

theme_counts['Top 3 Keywords'] = theme_counts['Theme Keywords']
bill_totals = df.groupby('State').size().sort_values(ascending=True)
theme_counts['Total_Bills'] = theme_counts['State'].map(bill_totals)

# Sort states and prepare positions
state_order = bill_totals.index.tolist()
theme_counts['State'] = pd.Categorical(theme_counts['State'], categories=state_order, ordered=True)
theme_counts = theme_counts.sort_values(['State', 'Count'], ascending=[True, False])
y_positions = {state: i for i, state in enumerate(state_order)}

# Color palette
unique_keywords = theme_counts['Top 3 Keywords'].unique()
cmap = get_cmap('tab20c')
keyword_colors = {kw: cmap(i % cmap.N) for i, kw in enumerate(unique_keywords)}

# Plotting
fig, ax = plt.subplots(figsize=(16, 18))
x_offsets = {state: 0 for state in state_order}
bar_height = 0.8
used_labels = set()

for _, row in theme_counts.iterrows():
    state = row['State']
    y = y_positions[state]
    width = row['Count']
    x = x_offsets[state]
    label = row['Top 3 Keywords']
    color = keyword_colors[label]
    show_label = label if label not in used_labels else None
    used_labels.add(label)

    ax.add_patch(Rectangle((x, y - bar_height / 2), width, bar_height, color=color, edgecolor='white', label=show_label))
    x_offsets[state] += width

# Axis setup
ax.set_yticks(range(len(state_order)))
ax.set_yticklabels(state_order)
ax.set_xlabel("Number of AI-Related Bills Introduced")
ax.set_title("AI Legislative Themes by State (2025)", fontsize=16)
ax.set_xlim(0, bill_totals.max() * 1.1)
ax.set_ylim(-0.5, len(state_order) - 0.5)
ax.invert_yaxis()
ax.tick_params(axis='x', bottom=True)
ax.tick_params(axis='y', left=False)

# Legend
legend_handles = [Rectangle((0, 0), 1, 1, color=keyword_colors[kw]) for kw in used_labels]
ax.legend(legend_handles, used_labels, title="Theme Clusters (Top 3 Keywords)", bbox_to_anchor=(1.01, 1), loc='upper left')

plt.tight_layout()
plt.show()
