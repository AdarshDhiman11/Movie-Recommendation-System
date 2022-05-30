import pandas as pd
import streamlit as st

st.title('Top Movies Recommendation')
st.subheader('Top 20 movies')

moviemeta = pd.read_csv('movies_metadata.csv', low_memory=False)

moviemeta.head(4)

moviemeta.info()

meanvote = moviemeta['vote_average'].mean()
print(meanvote)

minimumvote = moviemeta['vote_count'].quantile(0.90)
print(minimumvote)

q_movies = moviemeta.copy().loc[moviemeta['vote_count'] >= minimumvote]

def weighted_rating(x, minimumvote=minimumvote, meanvote=meanvote):
  voters = x['vote_count']
  avg_vote = x['vote_average']
  return (voters/(voters+minimumvote) * avg_vote) + (minimumvote/(minimumvote+voters) * meanvote)

q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

q_movies = q_movies.sort_values('score' , ascending=False)


top=q_movies[['title','vote_count','vote_average','score']].head(20)
top = top.reset_index()
top = top.drop(['index'],axis=1)

st.write(top)