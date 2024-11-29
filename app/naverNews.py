# pymongo 설치 : pip install pymongo
# BeautifulSoup 설치 : pip install beautifulsoup4


import pymongo
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen

def ex_news(sid):
    html = urlopen(f"https://news.naver.com/section/{sid}")
    bs = BeautifulSoup(html.read(), 'html.parser')
    headline_list = bs.find_all("strong", "sa_text_strong")
    headline_press = bs.find_all("div", "sa_text_press")
    headline_link = bs.find_all("a", "sa_text_title")
    print(headline_list) 
    print(headline_press) 
    print(headline_link)
    print(len(headline_list)) 
    print(len(headline_press)) 
    print(len(headline_link)) 

    nowDate = datetime.datetime.now()

    title_lst = []
    date_lst = []
    section_lst = []
    for title in headline_list:
        title_lst.append(title.text)
        date_lst.append(nowDate.strftime("%Y%m%d"))
        section_lst.append(f"{sid}")
    press_lst = []
    for press in headline_press:
        press_lst.append(press.text)
    link_lst = []
    for link in headline_link:
        link_lst.append(link["href"])

    resultList = [{"title": title, "press": press, "link": link, "date": date, "section": section}
         for title, press, link, date, section in zip(title_lst, press_lst, link_lst, date_lst, section_lst)]

    print(resultList);
    return resultList;

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

print(myclient.list_database_names())
dblist = myclient.list_database_names()
if "test" in dblist:
  print("The database exists.")
  mydb = myclient["test"]

print(mydb.list_collection_names())
collist = mydb.list_collection_names()
if "new" in collist:
  print("The collection exists.")
  mycol = mydb["new"]

## 100: 정치, 101: 경제, 102: 사회, 103: 생활/문화, 104: 세계, 105: IT/과학
resultList = ex_news(101)

x = mycol.insert_many(resultList)

print(x.inserted_ids)