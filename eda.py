from __future__ import division
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data/churn_train.csv')
df.isnull().sum(axis=0)

# What is 'today?' & type of column?
today = df.last_trip_date.max()
type(df.last_trip_date.max())

# Convert it from string to date-time, and check work
fmt = '%Y-%m-%d'
dates = []
for string in df.last_trip_date:
    dates.append(datetime.datetime.strptime(string, fmt))
df['last_trip_date'] = dates

# Make new column with max date - last_trip_date
from datetime import datetime, timedelta
df['last_trip_date'] = pd.to_datetime(df['last_trip_date'])
df['signup_date'] = pd.to_datetime(df['signup_date'])
today = df.last_trip_date.max()
df['Churn']= df['last_trip_date'].apply(lambda x : 1 if today-x> timedelta(days=30) else 0)

# What's the percentage of churn?
churn_percentage = sum(df.Churn) / len(df)
