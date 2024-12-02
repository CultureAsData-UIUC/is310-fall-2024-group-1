import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

# Download necessary NLTK data
nltk.download('vader_lexicon')

# Load the cleaned or combined dataset
df_games = pd.read_csv('combined_dress_up_games.csv')

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to get sentiment score
def get_sentiment(text):
    if pd.isna(text):
        return 0
    score = analyzer.polarity_scores(text)
    return score['compound']

# Apply sentiment analysis to the game descriptions
df_games['sentiment_score'] = df_games['GAME_DESCRIPTION'].apply(get_sentiment)

# Categorize the sentiment
df_games['sentiment_category'] = df_games['sentiment_score'].apply(
    lambda x: 'positive' if x > 0.05 else ('negative' if x < -0.05 else 'neutral')
)

# Handle 'YOR' and 'NO_OF_SKINTONES' if not already numeric
df_games['YOR'] = pd.to_numeric(df_games['YOR'], errors='coerce').fillna(0).astype(int)
df_games['NO_OF_SKINTONES'] = pd.to_numeric(df_games['NO_OF_SKINTONES'], errors='coerce').fillna(0).astype(int)

# Create a column to label pre- and post-2011
df_games['period'] = df_games['YOR'].apply(lambda x: 'pre-2011' if x < 2011 else 'post-2011')

# Display the processed games with sentiment categories
print(df_games.head())

# Set the style of seaborn plots
sns.set_style("whitegrid")

# Plot the sentiment distribution
plt.figure(figsize=(10, 6))
sns.countplot(data=df_games, x='sentiment_category', palette='coolwarm')
plt.title('Sentiment Distribution of Game Descriptions for Dress-Up Games')
plt.xlabel('Sentiment')
plt.ylabel('Number of Games')
plt.show()

# Boxplot to compare sentiment scores pre- and post-2011
plt.figure(figsize=(10, 6))
sns.boxplot(data=df_games, x='period', y='sentiment_score', palette='viridis')
plt.title('Sentiment Scores Pre- and Post-2011')
plt.xlabel('Period')
plt.ylabel('Sentiment Score')
plt.show()

# Save the processed dataset with sentiment scores and categories
df_games.to_csv('processed_game_descriptions.csv', index=False)
print("Processed data saved to 'processed_game_descriptions.csv'")


