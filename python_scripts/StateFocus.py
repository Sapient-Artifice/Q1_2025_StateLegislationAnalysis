from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
# NOTE: Add your dataframe loading logic here if needed
import seaborn as sns
import matplotlib.pyplot as plt

# Use summaries for topic modeling
summaries = df['Summary'].fillna("")

# Vectorize the summaries
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(summaries)

# Apply NMF
nmf_model = NMF(n_components=6, random_state=42)
W = nmf_model.fit_transform(X)
H = nmf_model.components_

# Extract top words per topic
top_n = 6
terms = vectorizer.get_feature_names_out()
topic_keywords = []

for topic_weights in H:
    top_indices = topic_weights.argsort()[::-1][:top_n]
    top_words = [terms[i] for i in top_indices]
    topic_keywords.append(", ".join(top_words))

# Assign dominant topic to each summary
df['Theme Index'] = W.argmax(axis=1)
df['Theme Keywords'] = df['Theme Index'].apply(lambda i: topic_keywords[i])

# Create a theme-by-state heatmap
theme_heatmap_data = df.groupby(['State', 'Theme Keywords']).size().unstack(fill_value=0)

# Sort rows and columns for cleaner display
theme_heatmap_data = theme_heatmap_data.loc[theme_heatmap_data.sum(axis=1).sort_values(ascending=False).index]
theme_heatmap_data = theme_heatmap_data[theme_heatmap_data.sum(axis=0).sort_values(ascending=False).index]

# Display cleaned-up heatmap
plt.figure(figsize=(20, 14))
sns.set(font_scale=1.1)
sns.heatmap(theme_heatmap_data, cmap='YlGnBu', linewidths=.5, annot=True, fmt='d', cbar_kws={'label': 'Number of Bills'})
plt.title('State-Level Focus on AI Legislative Themes (2025)', fontsize=20, weight='bold', pad=20)
plt.xlabel('Thematic Clusters (Keywords)', fontsize=14)
plt.ylabel('State', fontsize=14)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

