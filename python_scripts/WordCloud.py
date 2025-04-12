from wordcloud import WordCloud
import matplotlib.pyplot as plt
# NOTE: Add your dataframe loading logic here if needed

# Combine all bill summaries into one large text string
text_data = " ".join(df["Summary"].dropna().astype(str).tolist())

# Generate the word cloud
wordcloud = WordCloud(width=1600, height=800, background_color='white', collocations=True).generate(text_data)

# Display the word cloud
plt.figure(figsize=(20, 10))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Bill Summaries (2025 State Legislation)', fontsize=20)
plt.show()
