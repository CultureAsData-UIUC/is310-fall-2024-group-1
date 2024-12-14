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
Potential Uses: Provide guidelines for how your dataset might be used by other scholars. This section should include potential scholarly applications, with citations to relevant work that informed your project or could benefit from your dataset.

**Contextual Framework for Analysis:**
This dataset focuses on Adobe Flash dress-up games selected before and after the year 2011. This temporal division was chosen to observe whether changes in inclusivity—expressed through the number of available skin tones—corresponded with broader shifts in online gaming culture and aesthetics. Researchers are encouraged to consider this historical framing when conducting their analyses and to remain mindful of how the specific time boundary and subject matter influence observed patterns.

**Using the Controlled Vocabulary and Search Process:**
The dataset was compiled using a controlled vocabulary of dress-up-related keywords (e.g., “dress-up,” “fashion,” “styling,” “makeover,” “character customization”). Scholars looking to reproduce or build upon this research can employ a similar keyword strategy to ensure consistency and comparability. This approach helps future users navigate large archives like Flashpoint and systematically locate relevant materials, potentially adapting the controlled vocabulary to their own selection criteria.

**Incorporating the Dataset’s Structure and Attributes:**
The dataset includes fields such as Game Name, Year of Release, Operability Status, Developer, Publisher, Number of Skin Tones, and Screenshots. It also takes into account columns that were initially considered but eventually removed, ensuring transparency about the selection process. Understanding these attributes is essential for effective data reuse. For example, the Number of Skin Tones field can be used as a key indicator of representation changes over time, while the Year of Release and Operability Status help contextualize technological constraints and access issues related to legacy Flash content.

**Leveraging Visual Data (Screenshots):**
Screenshots were included to support visual analysis and provide qualitative context. They can serve as a resource for examining aesthetic trends, interface evolutions, and stylistic choices. Though the initial attempt to use ImagePlot was hindered by outdated documentation and missing macros, the presence of these images still allows for alternative forms of visualization and image-based research methods. Scholars are encouraged to use these screenshots to complement quantitative analyses, enabling a richer interpretation of how design elements evolve alongside metadata trends.

**Potential Scholarly Applications:**
- Cultural and Aesthetic Studies: Investigate how visual diversity and representation in digital dress-up games mirror or diverge from broader social attitudes, including the inclusion of more nuanced skin tone options.
- Temporal Comparisons and Trend Analysis: Examine patterns that emerge before and after 2011, considering how historical moments, technological advancements, or shifting player demographics may align with changes in game design and inclusivity.
- Methodological Replicability: Use the documented controlled vocabulary and filtering criteria as a blueprint for future archival research. This can help in comparing different eras, platforms, or genres, and encourage standardized practices in digital humanities research.


### Limitations and Considerations
Discuss any limitations of the dataset, such as privacy concerns, data quality issues, or barriers to reuse. Be transparent about the dataset’s strengths and weaknesses so that future users can approach it with a clear understanding of its potential and its constraints.

- **Partial Coverage and Metadata Variability:** While the dataset is as comprehensive as possible within the project’s scope, it is not exhaustive. Variations in developer documentation, incomplete metadata, and technical constraints may limit representativeness.
- **Temporal and Cultural Sensitivity:** Interpretations of changes in skin tone diversity or stylistic elements should factor in the cultural and technological contexts of the time. The pre-and post-2011 division is a starting point, not a definitive marker of cultural shifts.
- **Technical Dependencies:** Emulating or accessing these games may require specialized tools due to the phasing out of Adobe Flash. Future scholars may need to rely on emulators and preserved copies of the dataset, as well as continually updated methods for viewing legacy web content.

### Encouraging Ongoing Research and Preservation:
The documented rationales—such as the selection of dress-up games specifically, the focus on 2011 as a pivotal year, and the decision to include screenshots—offer a foundation for ongoing inquiry. Future scholars can expand upon these methods by incorporating additional data points, exploring other interactive genres, or applying machine learning techniques. By doing so, researchers can ensure that this dataset remains a living, adaptable resource, supporting deeper understanding and more nuanced analysis of cultural representation within online game archives.

