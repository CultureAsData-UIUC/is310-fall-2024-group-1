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

For more information on this approach, see: [https://www.sbgames.org/proceedings2020/ComputacaoShort/209781.pdf](https://www.sbgames.org/proceedings2020/ComputacaoShort/209781.pdf)
