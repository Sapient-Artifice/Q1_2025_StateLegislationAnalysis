from textblob import TextBlob

# NOTE: Add your dataframe loading logic here if needed
# Perform sentiment analysis on each bill summary
df['Summary'] = df['Summary'].fillna("")
df['Polarity'] = df['Summary'].apply(lambda text: TextBlob(text).sentiment.polarity)
df['Subjectivity'] = df['Summary'].apply(lambda text: TextBlob(text).sentiment.subjectivity)

# Display basic statistics for sentiment scores
sentiment_summary = df[['Polarity', 'Subjectivity']].describe()
import ace_tools as tools; tools.display_dataframe_to_user(name="Sentiment Analysis Summary", dataframe=sentiment_summary)


#Result on Cleaned_sort2_Legislation_Data.csv
#
#         Polarity  Subjectivity
#count  595.000000    595.000000
#mean     0.015323      0.462836
#std      0.222454      0.280480
#min     -0.600000      0.000000
#25%     -0.073214      0.277525

#See sentimentAnalysis.csv
#To generate a visualization for this use this script:

import seaborn as sns
import matplotlib.pyplot as plt

# Calculate average sentiment per state
state_sentiment = df.groupby('State')[['Polarity', 'Subjectivity']].mean().sort_values(by='Polarity', ascending=False)

# Create a scatter plot for state-level sentiment
plt.figure(figsize=(16, 10))
sns.scatterplot(data=state_sentiment, x='Polarity', y='Subjectivity', hue=state_sentiment.index, s=100, palette='tab20')

for state, row in state_sentiment.iterrows():
    plt.text(row['Polarity'], row['Subjectivity'], state, fontsize=9, ha='right')

plt.title('Average Sentiment of 2025 AI-Related Legislation by State')
plt.xlabel('Polarity (Negative to Positive)')
plt.ylabel('Subjectivity (Factual to Opinionated)')
plt.legend([],[], frameon=False)
plt.grid(True)
plt.tight_layout()
plt.show()
