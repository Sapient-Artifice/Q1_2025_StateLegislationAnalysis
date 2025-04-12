import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

# --- Load or assume your dataframe ---
# df = pd.read_csv("your_data.csv")  # if needed
# It must include a 'Summary' column with text data

# --- Step 1: Vectorize summaries with TF-IDF ---
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X = vectorizer.fit_transform(df['Summary'].fillna(""))

# --- Step 2: KMeans clustering ---
num_clusters = 6
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

# --- Step 3: Extract top keywords for each cluster ---
terms = vectorizer.get_feature_names_out()
top_keywords_per_cluster = []

for i in range(kmeans.n_clusters):
    centroid = kmeans.cluster_centers_[i]
    top_indices = centroid.argsort()[-5:][::-1]
    top_words = [terms[ind] for ind in top_indices]
    top_keywords_per_cluster.append(", ".join(top_words))

# --- Step 4: Map cluster numbers to readable labels ---
cluster_labels = {i: f"Cluster {i}: {top_keywords_per_cluster[i]}" for i in range(kmeans.n_clusters)}
df['Cluster Label'] = df['Cluster'].map(cluster_labels)

# --- Step 5: Reduce dimensions with PCA for 2D plotting ---
pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X.toarray())
df['PCA1'], df['PCA2'] = X_pca[:, 0], X_pca[:, 1]

# --- Step 6: Plot with seaborn ---
plt.figure(figsize=(16, 12))
palette = sns.color_palette("husl", len(cluster_labels))
sns.scatterplot(data=df, x='PCA1', y='PCA2', hue='Cluster Label', palette=palette, s=100)

plt.title('Clustering of AI-Related Legislation with Keyword Labels (2025)', fontsize=18)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend(title='Cluster Keywords', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()
