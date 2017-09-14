from __future__ import division
from eda import *

from sklearn.linear_model import LogisticRegression
from statsmodels.tools import add_constant
from sklearn.model_selection import train_test_split

df = df.dropna()

df['luxury_car_user'] = df['luxury_car_user'].apply(lambda x: 1 if x==True else 0)
df['iphone']=df['phone'].apply(lambda x: 1 if x=='iPhone' else 0)
df['SurgxDist']=df['avg_dist']*df['avg_surge']
df['weekday_pct_bins'] = pd.cut(df['weekday_pct']*df['surge_pct'], bins=4, labels=['0-25%','25-50%', '50-75%', '75-100%'])
WeekdayDummies = pd.get_dummies(df['weekday_pct_bins'])
df['daysSinceSignup']=today-timedelta(days=30)-df['signup_date']
df['daysSinceSignup']=df['daysSinceSignup'].astype('timedelta64[D]').astype(int)

dummies=pd.get_dummies(df.city)
df=pd.concat([df, dummies], axis=1)
df=pd.concat([df,WeekdayDummies], axis=1)



y = df['Churn'].values
X = df.drop('Churn', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# data for model 1
X1 = X_train[['avg_rating_of_driver', 'avg_surge', 'trips_in_first_30_days']].values
# data for model 2
X2 = X_train[['avg_dist', 'avg_rating_of_driver', 'avg_surge', 'trips_in_first_30_days']].values
# data for model 3
X3 = X_train[['luxury_car_user', 'iphone', 'SurgxDist', 'avg_rating_by_driver','avg_dist','avg_surge', "King's Landing",'0-25%','25-50%','50-75%','75-100%']].values
X3test = X_test[['luxury_car_user', 'iphone', 'SurgxDist', 'avg_rating_by_driver','avg_dist','avg_surge', "King's Landing",'0-25%','25-50%','50-75%','75-100%']].values


#second model
logit_model2 = LogisticRegression()
logit_model2.fit(X2, y_train)

#third model
logit_model3 = LogisticRegression()
logit_model3.fit(X3, y_train)
print logit_model3.score(X3test, y_test)
