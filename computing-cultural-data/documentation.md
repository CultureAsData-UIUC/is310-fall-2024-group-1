# Computation Methods and Cultural Data Analysis
## Cultural Data: Number of Skin Tones & Non Euro-Centric Features (Thea K) ##
https://sociation.ncsociologyassoc.org/wp-content/uploads/2023/03/avatarwhiteness_proof_final.pdf
Author: David R. Dietrich
	For cultural data, I wanted to look into the numeric value of skin tones present in video games throughout multiple years. I chose Reexamining Avatars of Whiteness: Changes in Racial Presentation of Video Game Player Characters as my scholarly article. This article examines whether or not racial diversity in video games has increased over the years, and how outside cultural events, such as the Black Lives Matter movement, have affected these numbers. To find the data for the article, the writer gathered the number of skin color options from multiple MMPORGSs. The data was gathered from MMPORG.com and Gamespot. Of the 85 games that were chosen for the study, you could not customize  your skin color in 16 of them. This data was then compared to 2009, in which 40% of games wouldn’t have let you change your skin color, showing an improvement. There were also more options for african hair styles seen in the games sampled in the most recent study rather than the one done in 2009. The conclusion the author of the study came to was that the number of skin colors available in games has increased since 2009, there is still a noticeable lack of options for black characters in video games, especially as seen in facial features and hair styles. The number of options for non-white characters in video games reflects the cultural ideals at the time they were created and the dominance of whiteness in culture.
	The most interesting part of this scholarly article, to me, was the discussion of cultural context and how that could cause a shift in the number of skin tones available in video games. We can use the same practice that the researcher did for our own data. We can use online databases of dress up games that already exist and compare the number of skin tones by year, allowing us to see trends over time. This will also make it easier for us to examine how dress up games were impacted by the social culture at the time. 
## Computation Method: Sentiment Analysis (Natural Language Processing)
### Cultural Data: User Reviews and Player Comments

In this study, we used user-generated reviews and comments from Flashpoint dress-up games to assess player perceptions of diversity, specifically focusing on skin tone and gender representation. We utilized **VADER Sentiment Analysis** to categorize each review as positive, negative, or neutral, aiming to understand how players reacted to customization options.

**Findings:**

- **Pre-2011:** Player reviews were mostly neutral or negative, often highlighting a lack of diverse skin tones.
- **Post-2011:** Reviews became more positive, with players praising the increased diversity of customization, such as more skin tone options and gender choices. Games developed by Rinmaru Games and Kongregate received specific praise for inclusivity efforts.

The sentiment distribution was not well balanced, but with the addition of more datasets from the Flashpoint Archive, we expect a broader and more distributed analysis. This study adds an essential qualitative perspective, showing how players perceived inclusivity in these games. This complements quantitative methods like image analysis of visual features.
doc
For more on sentiment analysis in games, see:
- [Proceedings of SBGames 2020](https://www.sbgames.org/proceedings2020/ComputacaoShort/209781.pdf)
- [ScienceDirect Article on Sentiment Analysis](https://www.sciencedirect.com/science/article/pii/S2212041617301559?casa_token=1TudC9YygHcAAAAA:KoR3h73zpIZMc03E5LyUIeLzHbbYcLx8V7GwMhKUGCOB_qLtqIvL3QmNpM11MhL9EvuTMsZs)


## Cultural Data: Video game screenshots from Horror Game Playthroughs
### Computational method: ImagePlot
(A.G. Samaniego)

- **Author**: Cody Mejeur, University at Buffalo SUNY, in Vol. 14 No. 3 of the Digital Humanities Quarterly (2020). https://www.digitalhumanities.org/dhq/vol/14/3/000486/000486.html 

In this section, we explore the Horror video game genre through the form of game playthrough videos, and observe how computational tools such as ImagePlot can be used to assess unique narrative paths and features across horror video games. 

## Key Concepts
**Summary**: Inspired by his interest and experiences with P.T., Mejeur decided to conduct a study about video games and the "similarity, difference, and variation in narrative" across iterations of P.T. playthroughs. Mejeur essentially challenges the idea that plot and game interactivity are conflicting features, and chooses to leverage the ludonarrative as a unique feature of analysis.

### **Methodology Choices**
- **Genre**: Horror games, P.T.
    - Mejeur chose the genre of Horror games because he argues that part of the genre's feature is to limit user choices to create a sense of fear. This hypothetically enacts more plot constraints, and makes analysis easier to conduct given the smaller number of choice permutations.
- **Analyzing**: Variance in time, and variance in signs
        - Time: How long it takes to perform specific sequences in the game
        - Signs: Encountering different objects or encounters in a narrative; their absence or presence
- **Data**: YouTube and Twitch recordings of P.T. playthroughs
    - One important data collection aspect to note is how Mejeur deliberately chooses videos that are not "over-edited" (excessive jumpcuts). I do not know what specific metric Mejeur uses to determine if something is "over-edited", but I understand his reasoning: since part of his game analysis is dependent on time (as a variable related to narrative), including videos with significant 10-30 minute clips missing would introduce significant bias.
- **Tool of Choice**: ImagePlot macro for ImageJ
    - Image plot is a no-code open source software (can be found (here)[https://github.com/culturevis/imageplot]) This tool allows for analysis of visual media such as paintings, photos, film, and video. It extracts images from video recordings, and plots it onto a graph so that it is compressed into one image.
        - X-axis of time, and randomly generated y-axis
        - No code, it involves files that will be run with ImageJ
    - Running the macro: Need a collection of images & an associated file/spreadsheet with filenames of images & any other needed data (ex: saturation or hues)


### Interesting takeaways:
- I was mind-blown by the idea of using ImagePlot as a tool for visualizing unique markers and variations in narrative features. While I often see ImagePlots in more humorous settings (ex: someone creating an image plot of the entire Bee Movie), I found it interesting to see how different "markers/objects" (ex: when a player encounters the red hallway segment) appear as bright colors in various places across the different image plots. While one image plot is cool, the comparison across 10 plots reveals relationships between length of time/order of events, and player experience.

While ImagePlot may not be the best tool for assessing dress-up games, given the static nature of dress-up games and absence of plot, ImagePlot could potentially be a useful tool when analyzing larger swaths of in-game screenshots pulled from Flashpoint Archive. 



## Computation Method: Image Recognition (Machine Learning)
### Cultural Data: Social Media Photographs
https://www.sciencedirect.com/science/article/pii/S2212041617301559?casa_token=1TudC9YygHcAAAAA:KoR3h73zpIZMc03E5LyUIeLzHbbYcLx8V7GwMhKUGCOB_qLtqIvL3QmNpM11MhL9EvuTMsZs

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

