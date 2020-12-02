# data_pipeline
Docker-pipeline collecting tweets and storing them in MongoDB. Next, the sentiment of tweets is analyzed and the result stored in PostgreSQL. Finally, the best sentiment tweets are sent to Slack automatically.

This repo is a result of my 6th weekly project at SPICED Academy Berlin.

The Goal of the Project:
Build a Dockerized Data Pipeline that analyzes the sentiment of tweets.
The pipeline should collect tweets and store them in a database. Next, the sentiment of tweets is analyzed and the result stored in a second database. Finally, the best or worst sentiment for a given time interval is put on Slack automatically.

Challenges of the project:
- Get Docker running
- Build a skeleton pipeline
- Collect Tweets
- Store Tweets in a Mongo DB
- Create an ETL task
- Run sentiment analysis
- Build a Slack bot