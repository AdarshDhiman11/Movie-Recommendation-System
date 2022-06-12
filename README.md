# Movie-Recommendation-System
This is the simple recommendation system that will give you top movies.

### Abstract:
A movie recommendation is important in our social life due to its strength in providing enhanced entertainment. Such a system can suggest a set of movies to users based on their interest, or the popularities of the movies. Although, a set of movie recommendation systems have been proposed, most of these either cannot recommend a movie to the existing users efficiently or to a new user by any means. In this paper we propose a movie recommendation system that has the ability to recommend movies to a new user. It mines movie databases to collect all the important information, such as, popularity and attractiveness, required for recommendation. It generates movie swarms not only convenient for movie producer to plan a new movie but also useful for movie recommendation.

## Simple Recommender
The Simple Recommender offers generalized recommnendations to every user based on movie popularity and (sometimes) genre. The basic idea behind this recommender is that movies that are more popular and more critically acclaimed will have a higher probability of being liked by the average audience. This model does not give personalized recommendations based on the user.

The implementation of this model is extremely trivial. All we have to do is sort our movies based on ratings and popularity and display the top movies of our list. As an added step, we can pass in a genre argument to get the top movies of a particular genre.

I use the TMDB Ratings to come up with our Top Movies Chart. I will use IMDB's weighted rating formula to construct my chart. Mathematically, it is represented as follows:

Weighted Rating (WR) =  (vv+m.R)+(mv+m.C) 
where,

v is the number of votes for the movie,
m is the minimum votes required to be listed in the chart,
R is the average rating of the movie,
C is the mean vote across the whole report.

## Libraries Used
### Pandas
Pandas is a Python library for data analysis. Started by Wes McKinney in 2008 out of a need for a powerful and flexible quantitative analysis tool, pandas has grown into one of the most popular Python libraries. It has an extremely active community of contributors.

Pandas is built on top of two core Python libraries—matplotlib for data visualization and NumPy for mathematical operations. Pandas acts as a wrapper over these libraries, allowing you to access many of matplotlib's and NumPy's methods with less code. For instance, pandas' .plot() combines multiple matplotlib methods into a single method, enabling you to plot a chart in a few lines.

Before pandas, most analysts used Python for data munging and preparation, and then switched to a more domain specific language like R for the rest of their workflow. Pandas introduced two new types of objects for storing data that make analytical tasks easier and eliminate the need to switch tools: Series, which have a list-like structure, and DataFrames, which have a tabular structure.

### Streamlit 
A faster way to build and share data apps.Streamlit turns data scripts into shareable web apps in minutes.All in pure Python. No front‑end experience required.

Streamlit is an open source app framework in Python language. It helps us create web apps for data science and machine learning in a short time. It is compatible with major Python libraries such as scikit-learn, Keras, PyTorch, SymPy(latex), NumPy, pandas, Matplotlib etc.

## Dataset Used
### Movielens Dataset
Consists of 26,000,000 ratings and 750,000 tag applications applied to 45,000 movies by 270,000 users. Includes tag genome data with 12 million relevance scores across 1,100 tags.

## Proposed Solution

1. First download the libraries in our system.
2. Load the dataset by using the .csv file which include all the data of the movies.
3. Calculate the mean vote by using mean() function.
4. Calculate the cutoff value (minimum votes required to clear the cutoff to enter the list).
5. Filter the movies into another DataFrame.
6. Computing the weighted average using the formula:-
   (voters/(voters+minimumvote) * avg_vote) + (minimumvote/(minimumvote+voters) * meanvote)
7. Calculate the score with the weighted average in consideration.
8. Sort the DataFrame in the descending order.
9. Printing the top 15 movies.

### Programe:
```
# Importing the libraries
import pandas as pd
import streamlit as st

# Writing sreamlit codes of title and subheader to show our data on web app
st.title('Top Movies Recommendation')
st.subheader('Top 20 movies')

# Loading the dataset
moviemeta = pd.read_csv('movies_metadata.csv', low_memory=False)

# This will show us the first 4 rows of the dataset file
moviemeta.head(4)

# This will show us the total number of row
moviemeta.info()

# Calculating the mean vote 
meanvote = moviemeta['vote_average'].mean()
print(meanvote)

# Calculating the cutoff value (minimum votes)
minimumvote = moviemeta['vote_count'].quantile(0.90)
print(minimumvote)

# Filter the movies into another DataFrame
q_movies = moviemeta.copy().loc[moviemeta['vote_count'] >= minimumvote]

# Computing the weighted average using the formula
def weighted_rating(x, minimumvote=minimumvote, meanvote=meanvote):
  voters = x['vote_count']
  avg_vote = x['vote_average']
  return (voters/(voters+minimumvote) * avg_vote) + (minimumvote/(minimumvote+voters) * meanvote)

# Calculate the score with the weighted average in consideration
q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

# Sort the DataFrame in the descending order
q_movies = q_movies.sort_values('score' , ascending=False)

# Printing the top 15 movies
top=q_movies[['title','vote_count','vote_average','score']].head(20)
top = top.reset_index()
top = top.drop(['index'],axis=1)

# Streamlit code to print the data on the web app
st.write(top)
```
## Result

![This is an image](https://github.com/AdarshDhiman11/Movie-Recommendation-System/blob/main/final%20project%20images/Screenshot%20(111).png)
![This is an image](https://github.com/AdarshDhiman11/Movie-Recommendation-System/blob/main/final%20project%20images/Screenshot%20(112).png)
