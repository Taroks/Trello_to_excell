
from os import link
from connection import Conection
import re
import time

class Pars():
    def __init__(self):
        self.conn = Conection()
        link = self.conn.card()
        self.page = self.conn.connection(link)
        

    def id_parsing (self): # id целевого обьекта запроса
        id_list = []
        for _ in range(len(self.page)):
            result = self.page[_]
            id = result['id']
            id_list.append(id)
        return id_list

    def name_parsing (self): #имя целевого объекта
        name_list = []
        for _ in range(len(self.page)):
            result = self.page[_]
            name = result['name']
            name_list.append(name)
        return name_list

    def url_parsing(self): # url целевого объекта
        url_list = []
        for _ in range(len(self.page)):
            result = self.page[_]
            url = result['url']
            url_list.append(url)
        return url_list
    
    def member_id_parsing(self): # id участников доски
        self.member_id_list=[]
        for _ in range(len(self.page)):
            result = self.page[_]
            member_id = result['idMembers']
            self.member_id_list.append(member_id)
        return self.member_id_list

    def member_name_parsing(self): # имя участников доски
        member_names = []
        result = self.member_id_parsing()
        link = self.conn.board_members()
        result1 = self.conn.connection(link)
        for i in range(len(result)):
            if len(result[i]) != 0:
                if len(result[i])>1:
                    list_of_members = []
                    for k in range(len(result[i])):
                        for j in range(len(result1)):
                            if result[i][k] == result1[j]['id']:
                                list_of_members.append(result1[j]['fullName'])
                    member_names.append(list_of_members)
                else:
                    for j in range(len(result1)):
                        if result[i][0] == result1[j]['id']:
                            member =[result1[j]['fullName']]
                    member_names.append(member)
            else:
                member = ["Пусто"]
                member_names.append(member)
        return member_names

    def change_parsing(self):
        change_list = []
        for _ in range(len(self.page)):
            result = self.page[_]
            change = result['dateLastActivity']
            change_list.append(change)
        return change_list

    def start_parsing(self): # время начала задачи
        start_list = []
        for _ in range(len(self.page)):
            result = self.page[_]
            start = result['start']
            start_list.append(start)
        return start_list

    def due_parsing(self): # срок сдачи задачи
        due_list = []
        for _ in range(len(self.page)):
            result = self.page[_]
            due = result['due']
            due_list.append(due)
        return due_list
    
    def list_id_parsing(self): # id колонки задачи
        self.list_id_list = []
        for _ in range(len(self.page)):
            result = self.page[_]
            list_id = result['idList']
            self.list_id_list.append(list_id)
        return self.list_id_list

    def list_name_parsing(self): # название колонки задачи 
        list_names = []
        for _ in range(len(self.list_id_parsing())):
            result = self.list_id_list[_]
            link = self.conn.lisst(result)
            pars = self.conn.connection(link)
            list_name = pars['name']
            list_names.append(list_name)
        return list_names

check = Pars()
check.change_parsing()
print(check.member_id_parsing()[0], check.member_name_parsing()[0])
print(len(check.member_id_parsing()), len(check.member_name_parsing()))
print(check.start_parsing(), check.due_parsing())