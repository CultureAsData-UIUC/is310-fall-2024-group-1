# Instructor Feedback on Experimenting with Datasets Update

## General Comments

Overall, I’m pleased with your progress on the *Experimenting with Datasets* update. You’ve done a commendable job dividing the labor effectively and exploring a range of computational methods. While I think you could have pushed further with the Flashpoint API data collection, I understand that this is new territory for everyone, and I appreciate the effort you’ve put in so far. Your detailed reflections and thoughtful assessment of the labor division and process were particularly strong points.

One note for improvement: the `IS310 Data.csv` file was missing from the repository, which meant I couldn’t reproduce the code for the linear regression analysis or the Flashpoint API data collection notebooks. Please ensure that all necessary files are included in the repository for the final submission.

## Specific Feedback

### Linear Regression Feedback

Your linear regression notebook is well-documented and easy to follow, with clear explanations of your process and decisions. I especially appreciated your reflection on how additional metadata could enhance the model.

However, running a regression model on so few data points, while possible, is not ideal. It’s clear from the limited data that there is no linear relationship between the variables, which could be observed visually. I understand that you’re still in the data collection phase, so this is a reasonable work-in-progress.

I also want to flag that skin tone is a discrete variable, not a continuous one, making linear regression a less suitable model for this analysis. A decision tree or random forest model might be more appropriate and could incorporate the additional metadata you mentioned. These models would also help identify which features in your dataset are most predictive of skin tone. Excellent work so far on this notebook, Divya!

### Flashpoint API Data Collection

I can see the effort you’ve put into this notebook, but I believe there’s room to expand the scope of your data collection. From what I reviewed, the notebook appears focused on validating your current data rather than collecting new data (please correct me if I misunderstood). This makes the notebook’s name or stated purpose a bit unclear.

Validation is valuable, and the code you’ve written looks promising (though I couldn’t test it without the missing dataset). The visualizations all look great, and show that you’re on the right track. Moving forward, I’d recommend either renaming this notebook to better reflect its content or expanding it to include additional data collection efforts. Great work overall, Ellis!

### ImagePlot

I appreciated your detailed reflections on attempting to use ImagePlot and the challenges you faced. Your documentation of the process and the obstacles is thorough and helpful. While I’m sorry it didn’t work out, the alternative ImageClustering code I shared previously could be a useful substitute. I hope that helps if you decide to revisit this tool for your final project submission.

## For Final Project Submission

For your final project submission, I encourage you to include both the most relevant code and results from your notebooks as well as your reflections on the process. These elements will provide valuable context for future users of your dataset, helping them understand how the data was collected, curated, and intended to be used. Additionally, I recommend incorporating some of the peer-reviewed scholarship from the *Computing Cultural Data assignment* to ground your dataset further and guide others in using it responsibly.

Overall, you’re in a strong position for the final project submission, and I’m excited to see everything come together!