from controller import insert_news
from scrapper import Scrapper
from logger_setup import set_logger

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

if __name__=="__main__":
    scrape_and_insert()