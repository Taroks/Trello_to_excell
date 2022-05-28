from createDB import Users
from createDB import session
from sqlalchemy.orm import query
import hashlib
class Inp():
    def choose(self):
        pass

    def root(self):
        yourKey = "9e47dcc934e0e0bf83c017d79f7fc0d2"
        yourToken = "7c63091f95e7cc219c038c546f9eb018dce8c5e86237ac37102c1e1a53450c70"
        # yourKey = "ca7e9b65eb6e9aa992c1a7f608e408a6"
        # yourToken = "55d89f320ca6b0e95e24660551550445118cc21d428a44f2cad4394eef6d89b1"
        root_list = [yourKey,yourToken]
        return root_list

class database():
    def searching(username, passwordik):
        user = Users.query.filter_by(login = username).first()
        Password = Users.query.filter_by(password = passwordik).first()
        if user != None:
            flaq = True
            if Password != None:
                flak = True
                return flak
            else:
                flak = False
                return flak
        else:
            flaq = False
            return flaq

    def registraiton(username, passwordik):
        hash_object = hashlib.sha256(passwordik)
        polzovatel = Users(username, hash_object)
        session.add(polzovatel)
        session.commit()

# check = database()
# user = 'Олег'
# Password = 'Comma'
# check.registraiton(user, Password)
