from faker import Faker
import time
import logging
from sqlalchemy import create_engine

fake_generator = Faker()
engine = create_engine('postgres://postgres:1234@pg_container:5432/postgres')
#### VERY IMPORTANT: THE HOST OR IP-ADDRESS IS THE SAME AS SERVICE NAME

create_query = """
DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
    text VARCHAR(500)
);
"""
engine.execute(create_query)

while True:
    #do this forever
    fake_text = fake_generator.text()
    logging.critical("---new tweet is coming---")
    #logging.critical(fake_text)
    insert_query = f"INSERT INTO tweets VALUES ('{fake_text}')"
    engine.execute(insert_query)
    logging.critical("---inserted into postgres---")
    time.sleep(2)
