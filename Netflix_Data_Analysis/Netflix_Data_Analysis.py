# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = pd.read_csv('C:/Surekha/Project dataset/Netflix_Data.csv')

# Inspect the data
print(data.head())
print(data.info())
print(data.describe())

# Check for missing values
print("Missing values before handling:")
print(data.isnull().sum())

#Drop rows with missing values

data.dropna(inplace=True)

# Confirm missing values have been handled
print("Missing values after handling:")
print(data.isnull().sum())

#print(data.head(2))
#print(data.info())
#print(data.describe())

# Remove duplicates
data.drop_duplicates(inplace=True)
print(data.head())
print(data.describe())


# Convert 'Release_Date' column to datetime format with errors='coerce'
data['Release_Date'] = pd.to_datetime(data['Release_Date'], errors='coerce')

# Check for invalid date values (NaT)
invalid_dates = data[data['Release_Date'].isnull()]
print("Invalid Release Dates:")
print(invalid_dates)

# Drop rows with invalid dates
data.dropna(subset=['Release_Date'], inplace=True)


# Standardize text (example: convert titles to lowercase)
data['Title'] = data['Title'].str.lower()


#print(data.head())


# 1. Count the number of TV Shows and Movies
content_counts = data['Category'].value_counts()
print("Number of TV Shows and Movies:")
print(content_counts)

# 2. Find the top 5 countries with the highest number of TV Shows and Movies
top_countries = data['Country'].value_counts().head(5)
print("\nTop 5 countries with the highest number of TV Shows and Movies:")
print(top_countries)

# 3. In Which year highest number of TV shows & Movies were released? Show with bar graph.

print(data['Release_Date'].dt.year.value_counts())         # It counts the occurance of all individual years in Date column.

data['Release_Date'].dt.year.value_counts().plot(kind='bar')  # Bar graph
plt.show()

#4. How many Movies & TV Shows are in the dataset? Show with Bar graph.

print(data.groupby('Category').Category.count())  # To group all unique items of a column and show their counts
sns.countplot(data['Category'])                   #Bar graph for each category

plt.show()

#5. Show all the Movies that were released in year 2000
data['Year']=data['Release_Date'].dt.year
#print(data.head(2))

print(data[(data['Category']=='Movie') & (data['Year']==2020)])

#6. Show all the records,where Category is Movie and Type is comedies or Country is United kingdom.
print(data[(data['Category']=='Movie') & (data['Type']=='Comedies') |(data['Country']=='United Kingdom')])

#7. What is the maximum Duration of a Movie/Show on Netflix?

print(data.Duration.unique())   #Display unique values for Duration field
print(data.Duration.dtypes)     # Datatype of Duration field
data[['Minutes','Unit']]=data['Duration'].str.split(' ', expand=True) # Splitting Duration field into two separate columns
print(data.head(2))
print(data.Minutes.max())

# 8. Calculate the average duration of Movies

# Convert 'Minutes' column to numeric
data['Minutes'] = pd.to_numeric(data['Minutes'], errors='coerce')
average_duration_movies = data[data['Category'] == 'Movie']['Minutes'].mean()
print("\nAverage duration of Movies (in minutes):", average_duration_movies)

# 9. Filter the dataset for movies with a duration greater than 120 minutes
long_movies = data[data['Minutes'] > 120]
print(long_movies)

# 10. Group the dataset by country and count the number of entries for each country
country_counts = data['Country'].value_counts()
print(country_counts)

# 11.  Filter the dataset for TV shows with more than 5 seasons
tv_shows_5_seasons = data[(data['Type'] == 'TV Show') & (data['Duration'].apply(lambda x: int(x.split(' ')[0])) > 5)]
print(tv_shows_5_seasons)

# 12. Visualize the distribution of numerical columns
numerical_cols = ['Release_Date', 'Duration']
for col in numerical_cols:
    plt.figure(figsize=(8, 6))
    sns.histplot(data[col], kde=True)
    plt.title(f'Distribution of {col}')
    plt.show()

# 13. Explore categorical columns
categorical_cols = ['Category', 'Country', 'Rating', 'Type']
for col in categorical_cols:
    plt.figure(figsize=(8, 6))
    sns.countplot(data[col])
    plt.title(f'Count of {col}')
    plt.xticks(rotation=45)
    plt.show()

# 14. Explore relationships between categorical and numerical columns
for col in categorical_cols:
    plt.figure(figsize=(10, 8))
    sns.boxplot(x=col, y='Duration', data=data)
    plt.title(f'{col} vs Duration')
    plt.xticks(rotation=45)
    plt.show()

# 15. Explore outliers
plt.figure(figsize=(8, 6))
sns.boxplot(data['Duration'])
plt.title('Boxplot of Duration')
plt.show()