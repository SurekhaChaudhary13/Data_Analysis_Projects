import pandas as pd
import numpy as np

# Load the dataset into a Pandas DataFrame
data = pd.read_csv('C:/Surekha/Project dataset/Call_Center_data.csv')

# Explore the structure and contents of the dataset
print("Dataset Information:")
print(data.info())

# View sample records from the dataset
print("\nSample Records:")
print(data.head())

# Perform data cleaning tasks

# Convert 'Call Timestamp' column to datetime format
data['Call Timestamp'] = pd.to_datetime(data['Call Timestamp'], format='%d-%m-%Y')

# Convert 'Call Duration In Minutes' column to numeric
data['Call Duration In Minutes'] = pd.to_numeric(data['Call Duration In Minutes'], errors='coerce')

# Remove rows with missing values in 'Csat Score' column
data = data.dropna(subset=['Csat Score'])

# Fill missing values in 'Response Time' column with the mean
#data['Response Time'].fillna(data['Response Time'].mean(), inplace=True)

# Convert 'Response Time' column to numeric
data['Response Time'] = pd.to_numeric(data['Response Time'], errors='coerce')

# Fill missing values in 'Response Time' column with the mean
#data['Response Time'].fillna(data['Response Time'].mean(), inplace=True)
# Fill missing values in 'Response Time' column with the mean
data['Response Time'] = data['Response Time'].fillna(data['Response Time'].mean())


# Replace empty strings in 'Sentiment' column with 'Unknown'
#data['Sentiment']=data['Sentiment'].replace('', 'Unknown', inplace=True)
# Replace empty strings in 'Sentiment' column with 'Unknown'
#data['Sentiment'].replace('', 'Unknown', inplace=True)

# Replace empty strings in 'Sentiment' column with 'Unknown' inplace
data.replace({'Sentiment': {'' : 'Unknown'}}, inplace=True)



# Calculate total number of rows in the dataset
total_rows = len(data)

# Calculate total number of unique Ids and customer names
unique_ids = data['Id'].nunique()
unique_customers = data['Customer Name'].nunique()

# Data analysis

# Calculate average call duration
avg_call_duration = data['Call Duration In Minutes'].mean()

# Count total calls by channel
total_calls_by_channel = data.groupby('Channel').size()

# Count total calls by sentiment
total_calls_by_sentiment = data.groupby('Sentiment').size()

# Calculate average response time by city
avg_response_time_by_city = data.groupby('City')['Response Time'].mean()

# Count total calls by state with Csat Score less than or equal to 5
total_calls_by_state_low_csat = data[data['Csat Score'] <= 5].groupby('State').size()

# Find top 5 reasons for contacting the call center
top_5_reasons = data.groupby('Reason').size().nlargest(5)

# Calculate average Csat Score by Call-Centres City
avg_csat_score_by_city = data.groupby('Call-Centres City')['Csat Score'].mean()

# Count total calls by Call-Centres City and Channel
total_calls_by_city_channel = data.groupby(['Call-Centres City', 'Channel']).size()

# Count total calls with a duration greater than 30 minutes
total_calls_greater_than_30min = len(data[data['Call Duration In Minutes'] > 30])

# Display analysis results
print("\nAnalysis Results:")
print("Total number of rows in the dataset:", total_rows)
print("Total number of unique Ids:", unique_ids)
print("Total number of unique customers:", unique_customers)
print("Average call duration:", avg_call_duration)
print("\nTotal calls by channel:")
print(total_calls_by_channel)
print("\nTotal calls by sentiment:")
print(total_calls_by_sentiment)
print("\nAverage response time by city:")
print(avg_response_time_by_city)
print("\nTotal calls by state with Csat Score less than or equal to 5:")
print(total_calls_by_state_low_csat)
print("\nTop 5 reasons for contacting the call center:")
print(top_5_reasons)
print("\nAverage Csat Score by Call-Centres City:")
print(avg_csat_score_by_city)
print("\nTotal calls by Call-Centres City and Channel:")
print(total_calls_by_city_channel)
print("\nTotal calls with a duration greater than 30 minutes:", total_calls_greater_than_30min)
