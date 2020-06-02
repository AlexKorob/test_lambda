import json
import os

import psycopg2


env = os.environ

conn = psycopg2.connect(
    dbname=env.get("DB_NAME"),
    user=env.get("DB_USERNAME"),
    password=env.get("DB_PASSWORD"),
    host=env.get("DB_HOST")
)


def lambda_show_daily_logs(event, context):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT
            worker.name AS worker_name,
            project.name AS project_name,
            vacancy.name AS vacancy_name,
            CASE WHEN extract(dow from daily_log.date) = 1 THEN SUM(daily_log.spend_time) END AS Monday,
            CASE WHEN extract(dow from daily_log.date) = 2 THEN SUM(daily_log.spend_time) END AS Tuesday,
            CASE WHEN extract(dow from daily_log.date) = 3 THEN SUM(daily_log.spend_time) END AS Wednesday,
            CASE WHEN extract(dow from daily_log.date) = 4 THEN SUM(daily_log.spend_time) END AS Thursday,
            CASE WHEN extract(dow from daily_log.date) = 5 THEN SUM(daily_log.spend_time) END AS Friday,
            CASE WHEN extract(dow from daily_log.date) = 6 THEN SUM(daily_log.spend_time) END AS Saturday,
            CASE WHEN extract(dow from daily_log.date) = 0 THEN SUM(daily_log.spend_time) END AS Sunday
        FROM daily_log
        LEFT JOIN worker ON daily_log.worker_id=worker.id
        LEFT JOIN project ON daily_log.project_id=project.id
        LEFT JOIN vacancy ON daily_log.work_type_id=vacancy.id
        GROUP BY daily_log.date, worker_name, project_name, vacancy_name
        ORDER BY daily_log.date ASC;
    """)
    data = {num + 1: {description[0]: col_value for description, col_value in zip(cursor.description, row)}
            for num, row in enumerate(cursor.fetchall())}
    return {
        "statusCode": 200,
        "body": json.dumps(data, default=str, indent=4, ensure_ascii=False)
    }
