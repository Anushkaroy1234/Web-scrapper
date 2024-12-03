from controller import insert_news
from scrapper import Scrapper
from logger_setup import set_logger
import schedule
import time

logger=set_logger()

def scrape_and_insert():
    sc=Scrapper()
    news=sc.scrapper()

    for index,n in enumerate(news):
        res=insert_news(
            heading=n.get('heading'),
            date=n.get('date'),
            news=n.get('news')
        )
        logger.info(f"====== {index+1} DATA INSERTED ====== {res}")
def start_scheduler():
    schedule.every().day.at("05:00").do(scrape_and_insert)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    scrape_and_insert()
    start_scheduler()