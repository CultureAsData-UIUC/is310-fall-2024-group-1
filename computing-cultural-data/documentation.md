# Computation Methods and Cultural Data Analysis

## Computation Method: Sentiment Analysis (Natural Language Processing)
### Cultural Data: User Reviews and Player Comments

In this study, we used user-generated reviews and comments from Flashpoint dress-up games to assess player perceptions of diversity, specifically focusing on skin tone and gender representation. We utilized **VADER Sentiment Analysis** to categorize each review as positive, negative, or neutral, aiming to understand how players reacted to customization options.

**Findings:**

- **Pre-2011:** Player reviews were mostly neutral or negative, often highlighting a lack of diverse skin tones.
- **Post-2011:** Reviews became more positive, with players praising the increased diversity of customization, such as more skin tone options and gender choices. Games developed by Rinmaru Games and Kongregate received specific praise for inclusivity efforts.

The sentiment distribution was not well balanced, but with the addition of more datasets from the Flashpoint Archive, we expect a broader and more distributed analysis. This study adds an essential qualitative perspective, showing how players perceived inclusivity in these games. This complements quantitative methods like image analysis of visual features.

For more on sentiment analysis in games, see:
- [Proceedings of SBGames 2020](https://www.sbgames.org/proceedings2020/ComputacaoShort/209781.pdf)
- [ScienceDirect Article on Sentiment Analysis](https://www.sciencedirect.com/science/article/pii/S2212041617301559?casa_token=1TudC9YygHcAAAAA:KoR3h73zpIZMc03E5LyUIeLzHbbYcLx8V7GwMhKUGCOB_qLtqIvL3QmNpM11MhL9EvuTMsZs)

## Computation Method: Image Recognition (Machine Learning)
### Cultural Data: Social Media Photographs

In the article, researchers discussed using photos from social media to understand how people appreciate nature (e.g., through recreational activities) in Singapore. Manual analysis would have taken too long, so they used **machine learning** to automate the process. They gathered over 20,000 geo-tagged photos from Flickr, which were analyzed using **Google Cloud Vision**. This tool identified elements in the photos (e.g., "plant," "animal," "food") and tagged them accordingly.

Researchers mapped photo locations and analyzed factors influencing where nature photos were taken, such as proximity to tourist spots and the amount of nearby greenery. This automated method enabled quick mapping and study of people's interactions with nature, aiding urban planners in understanding areas valued for nature activities.

**Interesting Insight:** Just as researchers used Google Cloud Vision for analyzing social media photos, we can use similar image recognition tools to analyze screenshots or images from Flash dress-up games. The image recognition tool can identify visual features like skin tone, clothing, and hairstyles, allowing us to track the evolution of these features before and after 2011.

## Group Project Proposal

For our group project, we propose using **image recognition and machine learning (ML)** to extract skin colors from Adobe Flash game screenshots. This method allows us to analyze the diversity of characters, focusing on skin tone representation in dress-up games over time.

### Related Article:
- [Avatar Whiteness Study](https://sociation.ncsociologyassoc.org/wp-content/uploads/2023/03/avatarwhiteness_proof_final.pdf)
- **Author:** David R. Dietrich
- **Cultural Data:** Number of skin tones in video games (numeric)

The article, *Reexamining Avatars of Whiteness: Changes in Racial Presentation of Video Game Player Characters*, examines racial diversity in video games over the years. The data was gathered from MMORPG.com and Gamespot, analyzing the number of skin color options across 85 games. The study found an increase in skin tone options compared to 2009, where 40% of games did not allow skin color customization. The recent study highlighted more options for African hairstyles, showing progress but also noting a continued lack of features for non-white characters.

**Interesting Insight:** The study discusses cultural context and its influence on the availability of diverse skin tones in games. We can apply a similar approach by using existing online databases of dress-up games and comparing the number of skin tones by year. This will allow us to examine how cultural events and social trends have influenced game design.

### Methodology Rationale

We chose this method because it enables us to automatically process a large number of game screenshots, saving significant time compared to manual analysis. By leveraging image recognition tools and pre-trained ML models, we can efficiently identify and classify different skin tones in the characters. This approach will help us track how the representation of diverse skin tones has evolved before and after 2011 in the games.

