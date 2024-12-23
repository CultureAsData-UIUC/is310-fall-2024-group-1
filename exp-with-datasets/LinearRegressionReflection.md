# Documentation: Predicting the Number of Skin Tones in Dress-Up Games With Linear Regression (Divya)

### 1. Data Collection/Standardization

Because we had a csv that already stored the data that we were using, I started with standardizing all the values in this spreadsheet to ensure that everything was consistent and then converted this csv into a dataframe to start conducting my analysis.

### 2. Model Development

#### Feature Selection

- **Year of Release (YOR)**

#### Model Choice

- A **Linear Regression** model is chosen to predict the continuous variable of the number of skin tones in the game.

#### Prediction

- After training, the model generates predictions for the number of skin tones for each game based on the year of release.

### 3. Model Evaluation

The model is evaluated using the following metric:

- **Mean Absolute Error (MAE)**: Measures the average magnitude of errors.

## Challenges Encountered

A major challenge in this process was the limited number of features used to train the model. The model relied only on the year of release to predict the number of skin tones in the game. While these features are important, they do not fully capture the complex factors that influence skin tone diversity in games. While the year a game is released provides some insight into societal trends and industry shifts, it alone doesn't account for the full range of factors that might influence skin tone representation. Cultural movements, industry standards, and the game’s narrative or artistic choices are also significant.

## Reflection

The model developed successfully predicted skin tone diversity based on the year of release , providing a solid foundation for understanding trends in game development. While the limited set of features used in the model presented challenges, it also highlighted the  potential for improving predictions with more comprehensive data.

One of the key takeaways from this project is that the right features can significantly enhance model accuracy. The experience reinforced the importance of feature selection and how adding additional data, could lead to even better predictions and deeper insights into diversity trends. This opens up opportunities for future improvements and refinement of the model.

