import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram of sentiment polarity across all summaries
# NOTE: Add your dataframe loading logic here if needed
plt.figure(figsize=(12, 6))
sns.histplot(df['Polarity'], bins=30, kde=True, color='purple')
plt.title('Distribution of Sentiment Polarity in AI Legislative Summaries (2025)', fontsize=16)
plt.xlabel('Sentiment Polarity (-1 = Negative, 0 = Neutral, 1 = Positive)', fontsize=14)
plt.ylabel('Number of Summaries', fontsize=14)
plt.axvline(0, color='black', linestyle='--')
plt.tight_layout()
plt.show()

# Average sentiment polarity by state
state_sentiment = df.groupby('State')['Polarity'].mean().reset_index()
state_sentiment_sorted = state_sentiment.sort_values(by='Polarity', ascending=False)

# Bar plot of average sentiment polarity by state
plt.figure(figsize=(14, 12))
sns.barplot(data=state_sentiment_sorted, y='State', x='Polarity', palette='coolwarm')
plt.title('Average Sentiment Polarity of AI Legislative Summaries by State (2025)', fontsize=16)
plt.xlabel('Average Sentiment Polarity (-1 = Negative, 0 = Neutral, 1 = Positive)', fontsize=14)
plt.ylabel('State', fontsize=14)
plt.axvline(0, color='black', linestyle='--')
plt.tight_layout()
plt.show()
