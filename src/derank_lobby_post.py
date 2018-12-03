import requests
import time
from bs4 import BeautifulSoup

#####

derankme = "" #cookie from derank.me
sessidlegit = "" # sessionid from cookies from legitderank.me
lobbylink = "" #your lobbylink

#####

header1 = {'authority':'derank.me',
           'method':'POST',
           'scheme':'https',
           'content-length':'100',
           'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
           'path':'/lobbies/add',
           'cookie':derankme,
           'origin':'https://derank.me',
           'referer': 'https://derank.me/',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
           }

dat1 = {'lobby_link':lobbylink,
        'max_rank':'SEM', #preferred rank
        'afk':'1'} #afk or not

while True:
    newsess = requests.Session()
    auth = newsess.get("https://legitderank.me/lobby/").text
    ade = newsess.cookies.get_dict()
    newcook = "__cfduid=" + ade["__cfduid"] + "; " + "csrftoken=" + ade["csrftoken"] + "; " + "sessionid=" + sessidlegit
    soup = BeautifulSoup(auth, features="html.parser")
    hidden_tags = soup.find_all("input", type="hidden", value=True)
    for tag in hidden_tags:
        csrftoken = tag["value"]
    header2 = {'authority':'legitderank.me',
           'method':'POST',
           'path':'/post_lobby/',
           'scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
           'accept-encoding': 'gzip, deflate, br',
           'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
           'cache-control': 'max-age=0',
           'content-length': '183',
           'content-type': 'application/x-www-form-urlencoded',
           'cookie':newcook,
           'origin':'https://legitderank.me',
           'referer': 'https://legitderank.me/lobby/',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
           }
    dat2 = {'csrfmiddlewaretoken':csrftoken,
        'lobby_url':lobbylink,
        'rank':'Silvers only', #preferred rank
        'afk':'on'} #afk or not
    send1 = requests.post("https://derank.me/lobbies/add", headers = header1, data=dat1)
    print("posted derank.me")
    send2 = newsess.post("https://legitderank.me/post_lobby/", headers = header2, data=dat2)
    print("posted legit.me")
    time.sleep(5)


    
