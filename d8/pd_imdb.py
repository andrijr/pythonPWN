import pandas as pd


df = pd.read_csv('movie_metadata.csv', index_col='movie_title')
print('describe\n', df.describe())
print('isnull\n',df.isnull().sum())
df.drop_duplicates(inplace=True)
# to samo
df = df.drop_duplicates()

print(df.shape)
asd = [4,1,2,3]
print(sorted(asd))
print(asd)
print(asd.sort())
print(asd)

print(df.describe())
print(df.info())
print(df.shape)
print(df.append(df.tail(1000)))
temp_df = df.append(df.tail(1000))
temp_df.drop_duplicates()
print(temp_df.shape)

print(df.columns)

budget = df['budget'].dropna()
print(budget.dropna())
print(budget.head())
print(budget.mean())

print(df['genres'].head)
print(df['genres'].value_counts().head(20))

print('Redley Scott')

redley_movies = df[df['director_name'] == 'Ridley Scott']
print(redley_movies.head())

print(df.columns)
print(df['actor_1_facebook_likes'].max())
# most_facebook_likes_actors = df[df['actor_1_facebook_likes']> 500000]
likes_mean = df['actor_1_facebook_likes'].mean()

most_facebook_likes_actors = df[df['actor_1_facebook_likes'] > likes_mean]
print(most_facebook_likes_actors.count())
print(most_facebook_likes_actors['actor_1_facebook_likes'].mean())
print(most_facebook_likes_actors['actor_1_facebook_likes'].count())



most_liked_actors_long_movies = df[
    (df['actor_1_facebook_likes'] >  likes_mean) &
    (df['duration'] > 60)
]
print(most_liked_actors_long_movies['actor_1_facebook_likes'].count())
# print(most_liked_actors_long_movies['actor_1_facebook_likes'].head())
# print(most_liked_actors_long_movies.head())

print(df['imdb_score'].head())
print(df['title_year'].head())

# median = df['imdb_score'].drop_duplicates().median()

df_movies = df[
    (df['title_year'] >= 2005) &
    (df['title_year'] <= 2010) &
    ( df['imdb_score'] > df['imdb_score'].drop_duplicates().median())
]

print(df_movies[['title_year', 'imdb_score']])
columns = ['title_year', 'imdb_score']
print(df_movies[columns])

print(df_movies.groupby('title_year').count()['imdb_score'])

def rating_function(x):
    if x >= 8:
        return 'good'
    else:
        return 'bad'

# count good nad bad movies
rated_movies = df_movies['imdb_score'].apply((rating_function))

print(rated_movies)
rated_movies.value_counts()
print(rated_movies.value_counts())

# get title of the max rated movie

# print(df_movies['imdb_score'].values.argmax())
max_rated_movie = df_movies['imdb_score'].values.argmax()
print(df_movies.iloc[max_rated_movie])



print('##################')





import matplotlib.pyplot as plt



# plot genres count as bar plot
genres = df['genres'].value_counts()
# genres.plot(kind='bar')
# plt.show()
print(genres)
df_genres_split = df['genres'].str.split('|', expand=True)[0].value_counts()
print(df_genres_split)

# TODO calculate splitted genres counts
df_genres_split = df['genres'].str.split('|', expand=True)[0]
print(df_genres_split)