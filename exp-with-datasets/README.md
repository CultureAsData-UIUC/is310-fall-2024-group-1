# Experimenting With Datasets Update
**PM**: A.G. Samaniego

**Objective**: The objective of engaging with dress-up games as our data set was to get a more concrete grasp of certain aspects of flash dress-up games changed over the span of years. We took games from pre-2011 and post-2011 and catalogued how many skin tones were offered, as well as what genre of game they were (anime, disney) so we could see if there was a noticeable difference between the two eras. We made sure to grab multiple games from each year in order to get a more detailed, accurate picture of trends.
- Computational Methods Used in this Update: Linear Regression Predictive Analysis for # of Skin tones, and ImageJ macros to visualize games across the collection

- **Addressing Research Gaps**: The research gap our data set addresses is the relationship between cultural movements in real life and the number of skin tones and genre of dress-up games. For example, was there an uptick in skin color options in games following the emphasis on the Black Lives Matter movement after George Floyd’s death? Was there an uptick in Disney themed dress-up games after popular Disney movies such as Frozen were released? Our research allows us to see how large events or movements can affect the skin color diversity in dress-up games, which is important because they are largely used by younger generations.


## Contents of this Folder:
- Linear Regression Analysis: [Computation Method - Linear Regression Analysis.ipynb](/exp-with-datasets/Computation%20Method%20-%20Linear%20Regression%20Analysis.ipynb) and [Documentation](/exp-with-datasets/LinearRegressionReflection.md)
- ImagePlot: [Documentation & Reflection](/ImagePlot-Docs.md)
- Flashpoint API Data Collection (our current work in progress): [Documentation](/exp-with-datasets/flashpoint_api_datacollection.md), [Current Progress in the Jupyter Notebook](/exp-with-datasets/flashpoint_api_datacollection%20(2).ipynb) 
    -**IMPORTANT TO NOTE**: For this submission, our group is still currently using our original Google Sheet dataset of games that had been manually pulled from Flashpoint Archive. We are currently working to expand our dataset and pull more games from the archive by switching to API/python scripting instead, and included our progress in the folder. While it is not a computational method, we'd like for the labor to be seen and included, as we are aiming for it to be our final project dataset at the end of the semester.


### Reflections
In this section we address various obstacles and observations we individually encountered while working on different parts of the project.
- **Linear Regression Predictive Model** (Divya): [Reflection](/exp-with-datasets/LinearRegressionReflection.md)
- **API Scripting** (Ellis): [Reflection](/exp-with-datasets/flashpoint_api_datacollection.md)
- **ImagePlot** (A.G.): [Reflection](/ImagePlot-Docs.md)

## Division of Work
- **PM**: A.G. Samaniego
- Dataset Update Summaries: Thea
- Linear Regression Prediction Model: Divya
- ImagePlot: A.G. Samaniego/Thea
- Flashpoint API Scripting: Ellis

#### Labor Summary:
For this checkpoint, Divya and I handled 2 computational methods of choice, which were Linear Regression Predictive analysis of # of skin tones, and screenshot visualizations using ImagePlot. The work for this checkpoint was 50% experimenting with visualizations, and 50% retroactively going back into the Flashpoint archive and seeing what information we could pull from the API. I assigned Thea the "Objective" and "Addressing Research Gaps" section of this document (before realizing there weren't as many questions as I anticipated), and had her and Divya assigned to work on a computational method. Divya mostly worked on the method independently, so to make sure Thea had the opportunity to contribute more fully, she helped me source some of the ImagePlot documentation (before we realized that neither of us can find the actual .txt file for ImagePlot needed to run the macro) and helped me source screenshots of the games (not reflected in the commit histories, since we did this through text/Google docs).