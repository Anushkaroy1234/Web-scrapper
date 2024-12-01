import requests
from bs4 import BeautifulSoup
from typing import List
from logger_setup import set_logger

logger=set_logger()

class Scrapper:

    def __init__(self):
        self.url="https://timesofindia.indiatimes.com/topic/Terrorist-Attack"
        self.__data=[]

    def __hit_endpoint(self):
        try:
            req=requests.get(self.url)
            return req.content
        except Exception as e:
            logger.error("__hit_endpoint() | "+str(e))
    
    def scrapper(self)->List[dict]:
        try:
            content=self.__hit_endpoint()
            b=BeautifulSoup(content,'html.parser')
            for div in b.find_all(class_="uwU81"):
                if div!=None:
                    heading_div=div.find(class_="fHv_i o58kM")
                    date_div=div.find(class_="ZxBIG")
                    news_para=div.find(class_="oxXSK o58kM")
                    self.__data.append({
                        "heading":heading_div.span.text.strip(),
                        "date":date_div.text.strip(),
                        "news":news_para.span.text.strip()
                    })
            return self.__data
        except Exception as e:
            logger.error("scrapper() | "+str(e))

if __name__=="__main__":
    sc=Scrapper()
    print(sc.scrapper()[0])