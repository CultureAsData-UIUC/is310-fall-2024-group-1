# Sentiment Analysis of Dress-Up Game Descriptions

## Project Overview
This project performs sentiment analysis on descriptions of dress-up games, focusing on their inclusivity and customization features, such as skin tone diversity and gender representation. The dataset consists of game descriptions from dress-up games released before and after 2011, gathered from the Flashpoint Archive. By applying sentiment analysis, we aim to understand the language used in these descriptions and whether they reflect a trend towards inclusivity over time.

## Cultural Data
### Game Descriptions
The cultural data for this analysis consists of descriptions of dress-up games from the Flashpoint Archive. These descriptions are used to evaluate how the language surrounding customization and inclusivity has evolved over time. The games are divided into pre-2011 and post-2011 categories to determine if there is a noticeable shift in sentiment associated with game descriptions after 2011.

## Computational Method: Sentiment Analysis
### Objective
The goal of this sentiment analysis is to assess how the language in game descriptions portrays the level of customization, diversity, and overall experience in dress-up games. Specifically, we are interested in understanding:
- Whether the descriptions highlight diversity in skin tones and gender options.
- If there is a noticeable trend in the language used for games released before versus after 2011.

### Sentiment Analysis Process
1. **Data Collection**: Descriptions of dress-up games were collected from the Flashpoint Archive.
2. **Preprocessing the Text Data**:
   - The descriptions were cleaned by removing special characters and converting all text to lowercase for consistency.
3. **Sentiment Analysis Using Natural Language Processing (NLP) Tools**:
   - We used the VADER Sentiment Analysis tool from the `nltk` library to determine the sentiment of each game description.
   - Sentiments are categorized as positive, negative, or neutral.

## Files in this Repository
- `dress_up_games.csv`: Contains the original dataset of dress-up game descriptions, including metadata such as year of release and developer.
- `sentiment_analysis.py`: Python script used to perform sentiment analysis on the game descriptions.
- `processed_game_descriptions.csv`: Contains the processed dataset, including sentiment scores and sentiment categories.
- `SENTIMENT_README.md`: An additional README outlining the sentiment analysis method used and its findings.

## Results
The sentiment analysis was applied to game descriptions to assess whether inclusivity and customization have been highlighted in the language used.
- **Pre-2011 Games**: Game descriptions were generally neutral, with limited emphasis on customization features such as skin tone or gender options.
- **Post-2011 Games**: Game descriptions showed more positive sentiment, with greater emphasis on diversity and inclusivity, particularly regarding skin tones and gender representation.

## Visualization
We generated several visualizations to help interpret the results:
- **Sentiment Distribution**: A count plot showing the sentiment categories (positive, negative, neutral) for all game descriptions.
- **Sentiment Comparison Pre- and Post-2011**: A boxplot comparing sentiment scores of game descriptions pre- and post-2011.

## How to Run the Code
1. Clone this repository.
2. Ensure all necessary Python packages are installed:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the sentiment analysis script:
   ```sh
   python sentiment_analysis.py
   ```
4. View the results and generated visualizations.

## Requirements
- Python 3.x
- nltk
- pandas
- matplotlib
- seaborn

## Conclusion
The sentiment analysis adds a qualitative perspective to our research by showing how inclusivity is reflected in the language used in game descriptions. It provides insights into how game developers have approached themes of diversity and customization, particularly in the years following 2011.

=======
# Sentiment Analysis for Flashpoint Dress-Up Games

## Overview
This project explores user perceptions of diversity in Flashpoint dress-up games using sentiment analysis of game descriptions. The goal is to understand how players reacted to inclusivity, focusing on features such as skin tone diversity and gender options.

## Methods
We used the VADER Sentiment Analysis tool from the `nltk` library to classify the sentiment of game descriptions into positive, negative, or neutral. The sentiment analysis results were visualized to understand trends pre- and post-2011.

## Dataset
The dataset includes Flashpoint dress-up game descriptions along with metadata such as year of release and the number of skin tone options. Sentiment scores and categories were added after processing.

### Files
- `sentiment_analysis.py`: Script to perform sentiment analysis on game descriptions.
- `dress_up_games.csv`: Dataset containing descriptions, metadata, and game information.
- `processed_game_descriptions.csv`: Output dataset containing sentiment scores and categories.

## Findings
- **Pre-2011**: The sentiment analysis showed a predominance of neutral or negative sentiment towards the lack of customization.
- **Post-2011**: Sentiments were generally more positive, reflecting improved inclusivity with additional skin tone and gender options.

The sentiment distribution is currently limited but is expected to improve as more games are included from the Flashpoint Archive.

For more information on this approach: [https://www.sbgames.org/proceedings2020/ComputacaoShort/209781.pdf](https://www.sbgames.org/proceedings2020/ComputacaoShort/209781.pdf)

