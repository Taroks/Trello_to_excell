from os import link
import requests
import time
import json
from input import Inp


class Conection:
    def __init__(self):
        self.sess = requests.session()
        incoming = Inp()
        self.yourKey = incoming.root()[0]
        self.yourToken = incoming.root()[1]


    def connection(self, link):
        user_agent_val = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
        accept_laguage = 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
        n_of_connection = 0 
        while n_of_connection <=4:
            try:
                con = self.sess.get(link, headers = {
    'user-agent': user_agent_val, 'accept-language': accept_laguage, "Accept": "application/json"})
                self.sess.headers.update({'Referer':link})
                con.raise_for_status()
                break
            except requests.exceptions.HTTPError as errh:
                print ("Http Error:",errh)
                time.sleep(5)
                print("reconnection")
                n_of_connection +=1
            except requests.exceptions.ConnectionError as errc:
                print ("Error Connecting:",errc)
                time.sleep(5)
                print("reconnection")
                n_of_connection +=1
            except requests.exceptions.Timeout as errt:
                print ("Timeout Error:",errt)
                time.sleep(5)
                print("reconnection")
                n_of_connection +=1
            except requests.exceptions.RequestException as err:
                print ("OOps: Something Else",err)
                time.sleep(5)
                print("reconnection")
                n_of_connection +=1
        return con.json()
    
    def list_of_boards(self):
        link = f"https://api.trello.com/1/members/me/boards?fields=name,url&key={self.yourKey}&token={self.yourToken}"
        return link

    def lisst(self, listid):
        link = f"https://api.trello.com//1/lists/{listid}?key={self.yourKey}&token={self.yourToken}"
        return link

    def card(self):
        link = f"https://api.trello.com/1/boards/5f328d1ee126fa48f1c586d3/cards?key={self.yourKey}&token={self.yourToken}"
        return link

    def member(self,memberid):
        link = f"https://api.trello.com//1/members/{memberid}?key={self.yourKey}&token={self.yourToken}"
        return link
     
    def board_members (self):
        link = f"https://api.trello.com/1/boards/5f328d1ee126fa48f1c586d3/members?key={self.yourKey}&token={self.yourToken}"
        return link

# check = Conection()
# print (check.connection(check.list_of_boards()))
# # with open ("test2.txt", "w") as f:
# #     f.write(str(type(check.connection())))
# #     f.write(check.connection())
# link = check.board()
# print(check.connection(link))

# url = "https://api.trello.com/1/lists//6231cb3f0b84d2653f62c885/cards?fields=id,name,badges,labels"

# response = requests.get(url)
