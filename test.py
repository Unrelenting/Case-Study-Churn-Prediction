import pandas as pd

df = pd.read_csv('data/churn_train.csv')
df['last_trip_date']=pd.to_datetime(df['last_trip_date'])
df['signup_date']=pd.to_datetime(df['signup_date'])
today = df.last_trip_date.max()

df['weekday_pct_bins'] = pd.cut(df['weekday_pct'], bins=4, labels=['0-25%','25-50%', '50-75%', '75-100%'])
WeekdayDummies = pd.get_dummies(df['weekday_pct_bins'])
results = pd.concat([df,WeekdayDummies], axis=1)
