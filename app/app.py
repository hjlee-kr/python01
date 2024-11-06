import pymongo
import requests
import datetime
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.request import urlopen


def ex_tag(sid, page):
    ### 뉴스 분야(sid)와 페이지(page)를 입력하면 그에 대한 링크들을 리스트로 추출하는 함수 ###
    
    ## 1.
    url = f"https://news.naver.com/section/{sid}"
    html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"\
    "(Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "\
    "Chrome/110.0.0.0 Safari/537.36"})
    soup = BeautifulSoup(html.text, "lxml")
    a_tag = soup.find_all("a")
    
   ##print(a_tag);

    ## 2.
    tag_lst = []
    for a in a_tag:
        if "href" in a.attrs:  # href가 있는것만 고르는 것
            if ("article" in a["href"]):
                tag_lst.append(a["href"])

    ## 중복제거
    re_set = set(tag_lst)
    tag_lst = list(re_set)
                
    return tag_lst


def re_tag(sid):
    ### 특정 분야의 100페이지까지의 뉴스의 링크를 수집하여 중복 제거한 리스트로 변환하는 함수 ###
    re_lst = []
    for i in tqdm(range(100)):
        lst = ex_tag(sid, i+1)
        re_lst.extend(lst)

    # 중복 제거
    re_set = set(re_lst)
    re_lst = list(re_set)
    
    return re_lst


##print(ex_tag(101,1))
##print(re_tag(100))

nowDate = datetime.datetime.now()

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

    title_lst = []
    date_lst = []
    for title in headline_list:
        title_lst.append(title.text)
        date_lst.append(nowDate.strftime("%Y%m%d"))
    press_lst = []
    for press in headline_press:
        press_lst.append(press.text)
    link_lst = []
    for link in headline_link:
        link_lst.append(link["href"])

    resultList = [{"title": title, "press": press, "link": link, "date": date}
         for title, press, link, date in zip(title_lst, press_lst, link_lst, date_lst)]

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

resultList = ex_news(101)

x = mycol.insert_many(resultList)

print(x.inserted_ids)