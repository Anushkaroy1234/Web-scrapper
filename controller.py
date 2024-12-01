from db import get_connection
from logger_setup import set_logger

logger=set_logger()

"""
create table if not exists scrapper(
	id int auto_increment primary key,
    news_heading varchar(255) not null,
    news_date varchar(100) not null,
    news text not null,
    inserted_at timestamp default current_timestamp
);
"""

def insert_news(heading:str,date:str,news:str)->dict:
    try:
        con,cursor=get_connection()
        query="""
            Insert into scrapper(news_heading,news_date,news) values("%s","%s","%s")
        """%(heading,date,news) # --> parameterized query = sql injection safe
        cursor.execute(query)
        con.commit()
        return {
            "heading":heading,
            "date":date,
            "news":news
        }
    except Exception as e:
        logger.error("insert_news() | "+str(e))
        con.rollback()
        return {}
    
if __name__=="__main__":
    res=insert_news()
    print(res)