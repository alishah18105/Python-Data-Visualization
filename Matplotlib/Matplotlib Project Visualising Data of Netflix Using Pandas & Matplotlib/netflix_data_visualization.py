import pandas as pd
import matplotlib.pyplot as plt

#Load the Netflix dataset
df = pd.read_csv('netflix_titles.csv')

#Data Cleaning: Filling missing values
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df.dropna(subset=["date_added","rating", "duration"], inplace=True)
print(df.isnull().sum())

#Bar Chart: Count of Movies vs TV Shows
type_count = df["type"].value_counts()
plt.figure(figsize=(6,4))
plt.bar(type_count.index, type_count.values, color=['blue', 'orange'])
plt.title("Number of Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("netflix_type_count.png")
plt.show()

#Pie Chart: Distribution of Ratings
rating_count = df['rating'].value_counts()
plt.figure(figsize=(8,8))
plt.pie(rating_count.values, labels=rating_count.index, autopct='%1.1f%%', startangle=120)
plt.title("Distribution of Ratings on Netflix")
plt.tight_layout()
plt.legend(title="Ratings", loc="best")
plt.savefig("netflix_rating_distribution.png")
plt.show()

#Histogram: Distribution of Movie Durations
movie_durations = df[df['type'] == 'Movie'].copy()
movie_durations['duration_int'] = movie_durations['duration'].str.replace(' min', '').astype(int)

plt.figure(figsize=(8,6))
plt.hist(movie_durations['duration_int'], bins=30, color ="purple", edgecolor='black')
plt.title("Distribution of Movie Durations on Netflix")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("netflix_movie_duration_distribution.png")
plt.show()

#Scatter Plot: Release Year vs Number of Shows
release_count = df['release_year'].value_counts().sort_index()
plt.figure(figsize=(8,6))
plt.scatter(release_count.index, release_count.values, color='green')
plt.title("Number of Shows Released Each Year on Netflix")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.grid(True)
plt.tight_layout()
plt.savefig("netflix_release_year_scater.png")
plt.show()

#Bar Horizontal Chart: Top 10 Countries with Most Netflix Titles:
country_count = df['country'].value_counts().head(10)
plt.figure(figsize=(8,6))
plt.barh(country_count.index, country_count.values, color='teal')
plt.title("Top 10 Countries with Most Netflix Titles")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("netflix_top_countries.png")
plt.show()


content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig, ax = plt.subplots(1,2, figsize=(12,5))

#First Subplot Movies:
ax[0].plot(content_by_year.index, content_by_year['Movie'], color='blue')
ax[0].set_title("Movies Released By Year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of Movies")

#Second Subplot: TV Shows:
ax[1].plot(content_by_year.index, content_by_year['TV Show'], color='orange')
ax[0].set_title("TV Shows Released By Year")
ax[0].set_xlabel("Year")
ax[0].set_ylabel("Number of TV Shows")

fig.suptitle("Comparision of Movies and TV Shows Released Over Years")
plt.tight_layout()
plt.savefig("movie_and_shows_comparision_plot.png")
plt.show()