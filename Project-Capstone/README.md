# Final-Project-Movie Recommender Engine

## Project/Goals
The goal of this project is to build a recommender engine that can suggest movies based on the genre, tagline, cast, keywords, and directors

## Process
>### I gathered the data from Kaggle and my dataset had 4803 rows and 24 columns 
>### I preprocessed and performed some EDAs on the data to understand the individual columns and how important they are to my model
>### I also performed some visualizations on Tableau to see some relationships between the features and we can see that over the years the budget, popularity, and Revenue increased.

![image](https://github.com/Jagunmolu-dev/LIGHTHOUSELABS/assets/67484584/3621f77b-510e-44d9-9ef3-43e61652e69e)

>### I performed Feature Extraction using the Tfid Vectorizer which converts a bunch of words into a matrix i.e numerical values
>### I then got the user input for their desired movie 
>### And using the cosine similarity the top 30 similar movies to the user input is suggested to the user
## Results
The model accurately recommended movies similar to the user input
![image](https://github.com/Jagunmolu-dev/LIGHTHOUSELABS/assets/67484584/825ab15f-d25f-4999-90f0-64b32622ed5a)


## Challenges 
The major challenge was that the dataset was not updated it can only recommend movies made upto the year 2017

## Future Goals
If I had more time I would pull movies from a movie API and continually update my recommender engine
