import requests
import time
from sqlalchemy import create_engine
from decouple import config
import logging

webhook_url = password = config('URL')

# connecting to postgres
password = config('POSTGRES_PASSWORD', cast=int)
engine = create_engine(f'postgres://postgres:{password}@postgres:5432/postgres')
logging.critical('\nConnected to Postgres')

while True:
    time.sleep(3600)
    select_query = '''SELECT id, text, polarity_score FROM berlin_tweets WHERE status = 1 ORDER BY polarity_score DESC LIMIT 1'''
    result = engine.execute(select_query).fetchall()
    update_query = f"UPDATE berlin_tweets SET status = 2 WHERE id = '{result[0][0]}'"
    logging.critical(f'\n\n{result[0][1]} WITH SCORE {result[0][2]}\n\n')
    message = f':robot_face: New tweet about Berlin with score {result[0][2]} arrived:\n\nTEXT: {result[0][1]}'
    data = {'text': message}
    requests.post(url=webhook_url, json = data)
    engine.execute(update_query)