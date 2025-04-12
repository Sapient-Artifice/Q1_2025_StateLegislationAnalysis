# Histogram of sentiment polarity across all summaries
import matplotlib.pyplot as plt
# NOTE: Add your dataframe loading logic here if needed
import seaborn as sns
from textblob import TextBlob  # if you're calculating polarity

plt.figure(figsize=(12, 6))
sns.histplot(df['Polarity'], bins=30, kde=True, color='purple')
plt.title('Distribution of Sentiment Polarity in AI Legislative Summaries (2025)', fontsize=16)
plt.xlabel('Sentiment Polarity (-1 = Negative, 0 = Neutral, 1 = Positive)', fontsize=14)
plt.ylabel('Number of Summaries', fontsize=14)
plt.axvline(0, color='black', linestyle='--')
plt.tight_layout()
plt.show()
