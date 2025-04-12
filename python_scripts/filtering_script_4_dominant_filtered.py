from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

# NOTE: Add your dataframe loading logic here if needed
# Define custom stopwords to remove generic terms like "ai", "content", etc.
custom_stopwords = ENGLISH_STOP_WORDS.union({
    'ai', 'artificial', 'intelligence', 'use', 'uses', 'using', 'technology', 'technologies',
    'content', 'generated', 'state', 'require', 'requires', 'bill', 'act',
    'section', 'establishes', 'program', 'commission', 'department', 'public'
})

# Rebuild the TF-IDF matrix using the new stopword list
vectorizer_filtered = TfidfVectorizer(stop_words=custom_stopwords, max_features=1000)
X_filtered = vectorizer_filtered.fit_transform(df['Summary'])

# Topic modeling with NMF again
nmf_filtered = NMF(n_components=6, random_state=42)
W_filtered = nmf_filtered.fit_transform(X_filtered)
H_filtered = nmf_filtered.components_

# Extract cleaner top keywords per topic
filtered_terms = vectorizer_filtered.get_feature_names_out()
clean_topic_keywords = []

for topic_weights in H_filtered:
    top_indices = topic_weights.argsort()[::-1][:6]
    top_words = [filtered_terms[i] for i in top_indices]
    clean_topic_keywords.append(", ".join(top_words))

# Assign each summary a new "cleaned" theme
df['Filtered Theme Keywords'] = W_filtered.argmax(axis=1)
df['Filtered Theme Keywords'] = df['Filtered Theme Keywords'].apply(lambda i: clean_topic_keywords[i])

# Export a clean version for use with the overlay map
dominant_filtered_theme = df.groupby('State')['Filtered Theme Keywords'].agg(
    lambda x: x.mode().iloc[0] if not x.mode().empty else 'None'
).reset_index()

dominant_filtered_theme['State Abbrev'] = dominant_filtered_theme['State'].map(us_state_abbrev)
filtered_theme_path = "/mnt/data/dominant_filtered_theme_per_state.csv"
dominant_filtered_theme.to_csv(filtered_theme_path, index=False)

filtered_theme_path
