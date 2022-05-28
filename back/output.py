import pandas as pd
from parsing import Pars

class Excell():
    def __init__(self):
        self.pars = Pars()



    def out_to_excel(self):
        df = pd.DataFrame({"Имя карточки:": self.pars.name_parsing(),
        "Сслыка на карточку": self.pars.url_parsing(), "Дата начала задачи:": self.pars.start_parsing(),
        "Дедлайн задачи":self.pars.due_parsing(),"Стадия задачи": self.pars.list_name_parsing(),"Дата последнего изменения": self.pars.change_parsing(),
        "Участники задачи":self.pars.member_name_parsing()})
        df.to_excel('otchet.xlsx', index = False)


check = Excell()
check.out_to_excel()

# df = pd.DataFrame({'Карточка №',_+1,"\ncard id:", self.pars.id_parsing()[_],"\ncard name:", self.pars.name_parsing()[_],"\ncard url", self.pars.url_parsing()[_], 
#             "\nmembers name:",self.pars.member_name_parsing()[_],"\nstart date:", self.pars.start_parsing()[_],
#             "\ndue date",self.pars.due_parsing()[_],"\nlist name:", self.pars.list_name_parsing()[_]})