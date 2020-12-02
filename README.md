# data_pipeline
Docker-pipeline collecting tweets and storing them in MongoDB. Next, the sentiment of tweets is analyzed and the result stored in PostgreSQL. Finally, the best sentiment tweets are sent to Slack automatically.

This repo is a result of my 6th weekly project at SPICED Academy Berlin.

## The Goal of the Project:
Build a Dockerized Data Pipeline that analyzes the sentiment of tweets.

![Pipeline schema (c) SPICED Academy](https://github.com/asyaparfenova/data_pipeline/blob/main/images/pipeline.png?raw=true)

The pipeline should collect tweets and store them in a database. Next, the sentiment of tweets is analyzed and the result stored in a second database. Finally, the best or worst sentiment for a given time interval is put on Slack automatically.

## Challenges of the project:
- Get Docker running
- Build a skeleton pipeline
- Collect Tweets
- Store Tweets in a Mongo DB
- Create an ETL task
- Run sentiment analysis
- Build a Slack bot

## What is what in this repo?
- besides the readme, license and image/ in the root directory we have docker-compose file, which makes all the pipeline running;
- to start, use "docker-compose build" and/or "docker-compose up -d" commands
- docker-containers for MongoDB and Postgres were built with pre-made images
- docker containers for tweepy, etl and slackbot were built from custom made docker-files (placed on folders accordingly)
- the tweeter API, etl and Slackbot programs are written in python (placed on folders accordingly)

## passwrods and credential
- to run this programm you would need .env files with:
  - postgres password
  - twitter developer api credentials
  - slackbot url
(not copied to this repo)
  
