# Flashpoint Archive Project - Final Data Essay

## Purpose: 

The purpose of our project was to explore and answer the question: how has the number of skin tones available in dress-up games evolved before and after 2011, and what does this reveal about the representation of diversity in games? By focusing on this timeline, we aim to identify trends in inclusivity within the gaming industry, particularly in the context of character customization. This analysis provides insights into whether game developers have made significant strides in representing diverse audiences and how societal changes may have influenced the design of these games. Through this research, we hope to contribute to a broader conversation about diversity and inclusivity in digital entertainment.

## Content: 

Due to the lack of a structured directory on Flashpoint Archive's API, our group developed a controlled vocabulary to refine our searches and efficiently locate relevant dress-up games. We followed these steps to ensure consistent results across team members:

	While building our dataset, we initially had a column labeled ‘gender’. Our plan for this was to find aspects of the game that featured either male or female oriented marketing. We decided to get rid of this after Professor LeBlanc reminded us that the gender binary is very difficult to track objectively, and also an old metric that isn’t very relevant. We also added a screenshots column to the dataset so that people could see what the games actually looked like, instead of just numbers on a table. This way, it would be easier for people to collect other information from the games we provided as well and to also assist with our image plot analysis. We chose 2011 because Adobe Flash Player 11 was released that year. It included the release of the first stage 3D and improved 3D rendering capabilities. We chose to analyze dress-up games because we thought they would be a good window into the subconscious biases that are being presented to little kids, and because we all played dress-up games multiple times as kids. 

Controlled Vocabulary Development:
We searched through Flashpoint Archive's current documentation and found a list of tags used for flash game organization. We pulled these tags and created a list of keywords relevant to dress-up games and gender representation, such as “dress-up,” “fashion,” “styling,” “makeover,” and “character customization." These keywords were tested iteratively to capture the broadest selection of games that aligned with our project focus.
Search Process:
Platform Navigation: Each team member used the Flashpoint Archive's search bar with the controlled vocabulary to locate games.
Keyword Application: Keywords were applied individually when sourcing games.
Date Filters: To separate games pre- and post-2011, we used the "Year Released" filter that was on Flashpoint's search engine, and searched individual years prior to, and after 2011.
Inclusion Criteria:
Games with dress-up and customization features.
Availability of gender selection and multiple skin tones.
Games that run on the Ruffle emulator for usability in analysis.
Exclusion Criteria:
Excluded non-dress-up games, NSFW results, or those with limited customization features.
Games without specified release dates or those that could not operate fully on the Ruffle emulator were deprioritized. 

We noted…

-Game Name
-Year of Release
-Operability Status
-Developer
-Publisher
-Number of Skin Tones
-Screenshots


## Labor Division 

**Data Collection & Standardization (Thea)**
- Thea led the initial dataset preparation, starting with a CSV of post-2011 dress-up games. She ensured key attributes like game name, year of release, operability, developer, and skin tone options were present and standardized.
- After validating operability through the Ruffle emulator, the cleaned dataset was saved for analysis.

**API Scripting & Debugging (Ellis)**
- Ellis worked on enriching the dataset using the Flashpoint Archive API. Ellis wrote and debugged a Python script to pull additional metadata.
- Debugging involved identifying inconsistencies in API responses, such as null values or unexpected formats, and improving error handling to ensure reliable data. This enriched the dataset for deeper analysis.

**Linear Regression Model (Divya)**
- Divya built a linear regression model to predict the number of skin tones based on the year of release.
The model performed well but was limited by a single feature—Year of Release—highlighting the importance of incorporating more contextual data like cultural movements to improve accuracy.

**ImagePlot Visualization (A.G.)**
- A.G. experimented with ImagePlot to visualize game screenshots and identify trends. However, outdated documentation and missing macro files limited its functionality.
- Alternate tools within ImageJ were explored, and screenshots were sourced for future visualizations.


## Dataset

Dataset: https://docs.google.com/spreadsheets/d/1cLHv558ZuL77vAilZiQpX9K0Jln4tfCmSbDe6m8vNmI/edit?usp=sharing



### Dataset Documentation

The dataset is organized into columns as follows: 
- Game Name (string): The title of the Adobe Flash dress-up game.
- Year of Release (int): The year the game was first made available to the public.
- Operability Status (string): Indicates whether the game is currently playable or not.
- Developer (string): The individual or studio responsible for creating the game.
- Publisher (string): The company or platform that distributed the game.
- Number of Skin Tones (int): The count of distinct skin tones available in the game's character customization.
- Screenshots (jpg/png): Images captured from the game, used for analysis or visual reference.

We identified a null value in the "Screenshot" column for the game Cinderella Flies to Mexico because the game is non-operable, and therefore no screenshots could be captured. Additionally, we observed inconsistencies in the "Screenshot" column, where the images are in both PNG and JPG formats. These discrepancies arise from differences in how the screenshots were created—some were pulled directly from the Adobe Flash game files, while others were manually taken during gameplay.

Because all our other values were consistent and existing, we didn’t need to do any cleaning and were able to use our columns as is.

## Guidelines for Data Use
Contextual Framework for Analysis:
This dataset focuses on Adobe Flash dress-up games selected from periods before and after 2011. Researchers can consider this temporal division in light of historical, social, and technological shifts that influence online culture. To place these trends into broader scholarly conversations, studies on digital culture and inclusivity can be particularly insightful. For instance, scholarly works have examined how digital platforms mediate identity, culture, and representation (Nakamura, 2008; Shaw, 2014).

Using the Controlled Vocabulary and Search Process:
The controlled vocabulary (e.g., “dress-up,” “fashion,” “character customization”) developed for this project ensures more consistent and reproducible data retrieval. Similar keyword strategies have been recommended in digital humanities for standardizing queries and ensuring comparability across datasets (Drucker, 2014). Future scholars can adopt or adapt this approach to ensure replicability and coherence when navigating large-scale archives.

## Incorporating the Dataset’s Structure and Attributes:
Each attribute—Game Name, Year of Release, Operability Status, Developer, Publisher, Number of Skin Tones, and Screenshots—offers a pathway into analyzing cultural production in digital media. Number of Skin Tones can serve as a proxy for examining inclusivity, reflecting how creators may respond to evolving norms around diversity (Nakamura, 2008). Meanwhile, temporal attributes like Year of Release help contextualize shifts in technological landscapes and audience expectations (Bolter & Grusin, 2000).

## Leveraging Visual Data (Screenshots):
Screenshots, while initially intended for visualization through tools like ImagePlot, still provide a valuable resource. They allow for qualitative analyses of aesthetic trends and interface changes. Researchers can interpret visual shifts in character designs, color palettes, and thematic styles as indicators of broader cultural and technological transitions. Such visual analysis aligns with digital humanities approaches that emphasize visual forms of knowledge production (Drucker, 2014) and the importance of remediation in digital media (Bolter & Grusin, 2000).

## Potential Scholarly Applications:

Cultural and Aesthetic Studies: Examine how the availability of diverse character customizations in dress-up games relates to cultural discourses on inclusivity and representation (Shaw, 2014; Nakamura, 2008).
Temporal Comparisons and Trend Analysis: Identify patterns in genre popularity or customization features over time, situating these shifts within historical and media studies frameworks (Cassell & Jenkins, 1998; Murray, 1997).
Methodological Replicability: Use this dataset’s controlled vocabulary and selection criteria as a model for conducting similar archival research in game studies, platform studies, or digital humanities (Apperley & Parikka, 2018).
Limitations and Considerations:

## Partial Coverage and Metadata Variability: Differences in metadata quality reflect broader challenges in preserving and cataloging ephemeral digital content. Scholars should note these limitations when drawing conclusions, as has been discussed in media archaeology and platform studies (Apperley & Parikka, 2018).
Temporal and Cultural Sensitivity: Changes in inclusivity should be analyzed with an understanding that societal values evolve over time. Media scholarship acknowledges that cultural artifacts do not exist in a vacuum but respond to and shape prevailing social discourses (Nakamura, 2008; Shaw, 2014).
Technical Dependencies: Emulating Flash-based content is increasingly difficult. Considering the broader issues of digital preservation and remediation ensures that researchers maintain a critical perspective on access and interpretation (Bolter & Grusin, 2000).
Respectful and Informed Engagement:
While the dataset is anonymized and focused on game metadata, these games are cultural products. Researchers are encouraged to approach their analyses thoughtfully, acknowledging how creative communities, audience dynamics, and historical contexts shape these digital artifacts (Cassell & Jenkins, 1998). Sensitivity to cultural values and a measured interpretive approach help avoid oversimplification.

## Encouraging Ongoing Research and Preservation:
By offering explicit documentation on selection criteria, keyword usage, and methodology, this dataset provides a springboard for future research. Scholars can build on these approaches, incorporating additional data points, new analytical frameworks, or advanced computational methods, ensuring that the study of digital cultural artifacts remains dynamic and responsive to evolving scholarly questions.

## Selected References
Apperley, T., & Parikka, J. (2018). “Platform Studies’ Epistemic Threshold.” Games and Culture, 13(4), 349–369.
Bolter, J. D., & Grusin, R. (2000). Remediation: Understanding New Media. MIT Press.
Cassell, J., & Jenkins, H. (Eds.). (1998). From Barbie to Mortal Kombat: Gender and Computer Games. MIT Press.
Drucker, J. (2014). Graphesis: Visual Forms of Knowledge Production. Harvard University Press.
Murray, J. H. (1997). Hamlet on the Holodeck: The Future of Narrative in Cyberspace. The Free Press.
Nakamura, L. (2008). Digitizing Race: Visual Cultures of the Internet. University of Minnesota Press.
Shaw, A. (2014). Gaming at the Edge: Sexuality and Gender at the Margins of Gamer Culture. University of Minnesota Press.

