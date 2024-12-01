import mysql.connector
from dotenv import load_dotenv
import os
from logger_setup import set_logger

load_dotenv()
logger=set_logger()

def get_connection():
    try:
        con=mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_USER_PASSWORD'),
            database=os.getenv('DB_SCHEMA')
        )
        logger.info("database connection is established!")
        cursor=con.cursor()
        return (con,cursor)
    except Exception as e:
        logger.error("get_connection() | "+str(e))

if __name__=="__main__":
    print(get_connection())