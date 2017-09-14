# Case Study: Churn Prediction


# Overview

This project was aimed at predicting customer churn rate and looking at possible actions to increase retention rate. We needed to identify which features were the greatest predictors of churn rate and create a model that would predict our churn rate for our data.  We started with a logistic regression model for our baseline with some of the features we thought would be the best predictors for churn.  Then we built a random forest and a gradient boosted model and iterated over those with other features that helped improve our model's predictive power.


# Motivation

Customer churning is one of the biggest problems that businesses encounter, and being able to predict churn rate is one of the more common applications of data science. Predicting churn and determining the common characteristics of churning customers allows businesses to use their resources more efficiently and make data informed decisions.  Businesses could offer promotions or target specific audiences with their advertisements to increase businesses or retain customers.  This project was meant to replicate real world applications and how machine learning can impact businesses.


# Data

The data was from a ride-sharing company.  It had 11 features of varying types, which were categorical, numerical, and text.


# EDA

Some of the initial features we thought might be good predictors of churn were surge percentages, the average surge rate, the usage on weekends, and the distance travelled.  We also looked at how many trips the user took within the first 30 days of signing up.  After further EDA, we found that the city location, type of phone, as well as if people took luxury rides actually were pretty good predictors of churn.


# Models

We started of with a logistic regression model as a baseline model. Following the CRISP-DM methodology, we iterated over adding multiple features and compared them with a Random Forest model.  Since the random Random Forest model seemed to perform better we just stuck with that and a Gradient Boosted model, which were comparable in results.  We decided to use accuracy as the metric for comparison.


# Credits

Thank you to Camilla Nawaz, Jeremy Gozlan, and Urmi Mukherjee for collaborating on this project.
