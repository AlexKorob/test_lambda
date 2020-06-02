# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import os

import psycopg2

env = os.environ

conn = psycopg2.connect(
    dbname=env.get("DB_NAME"),
    user=env.get("DB_USERNAME"),
    password=env.get("DB_PASSWORD"),
    host=env.get("DB_HOST")
)


class WeatherPipeline:
    def process_item(self, item, spider):
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO weather (weather, date) VALUES (%s, %s)",
            (item["weather"], datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        )
        conn.commit()
        return item
