
## Dataset Overview

The dataset contains call center records with various attributes such as Id, Call Timestamp, Call-Centres City, Channel, City, Customer Name, Reason, Response Time, Sentiment, State, Call Duration In Minutes, and Csat Score.

## Data Loading and Preprocessing

- Loaded the dataset into a Pandas DataFrame.
- Explored the structure and contents of the dataset.
- Converted 'Call Timestamp' column to datetime format.
- Converted 'Call Duration In Minutes' column to numeric.
- Removed rows with missing values in 'Csat Score' column.
- Filled missing values in 'Response Time' column with the mean.
- Replaced empty strings in 'Sentiment' column with 'Unknown'.

## Data Analysis

- Calculated total number of rows in the dataset.
- Calculated total number of unique Ids and customer names.
- Analyzed average call duration.
- Counted total calls by channel.
- Counted total calls by sentiment.
- Calculated average response time by city.
- Counted total calls by state with Csat Score less than or equal to 5.
- Found top 5 reasons for contacting the call center.
- Calculated average Csat Score by Call-Centres City.
- Counted total calls by Call-Centres City and Channel.
- Counted total calls with a duration greater than 30 minutes.

## Conclusion

This README provides an overview of the data loading, preprocessing, and analysis steps performed on the call center dataset using Python and Pandas. 
