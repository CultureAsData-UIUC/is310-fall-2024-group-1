
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