# Fraud Detection Case Study
Building a model that will enable an e-commerce company to better detect fraudulent users of their web hosting services. This is a serious problem for the company because fraudulent users are exhausting the companies available resources and not paying for their services. The end goal is to create a valuable model that is hosted on an AWS EC2 instance that is accessible via Flask App. The web application will also store newly predicted fraudulent users to an existing data base. 

### Results
Created a user friendly fraud detection web application by implementing an accessible pickled random forest classifier that holds a high predictive power of fraudulence as determined by an F1 score of .94. 

### The Data & EDA 
- Highly confidential so the true data is not available
- 55 Features 
  - Integers, categorical, string
- Roughly 14000 samples, approximately 2000 of which are labeled fraudulent users
- 13 Assessed key features 

|   |   |   |
|---|---|---|
|'body_length'| 'name_length'| 'num_order'|
|'num_payouts'|'payout_type'|'user_age'|
|'delivery_method'|'user_type'| 'gts'|
|'sale_duration'|'org_facebook'| 'org_twitter'|
|'hour'|'fraud'|| | 


### Pre-Processing
- Consolidate the three types of fraudulent users: 'fraudster_event', 'fraudster', 'fraudster_att' into one fraud group
- Convert user_created to a date time format
- Remove 


### Modeling & Evaluation

Behind the Metric:

F1 Score: In a statistical analysis of binary classification the F score is a measure of accuracy. This measure takes into consideration both the precision (true positives / total predicted positive) and recall (true positives / Total actual positive)

