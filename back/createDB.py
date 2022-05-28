from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgresql+psycopg2://postgres:Ощлук171@localhost:8888/Users")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = scoped_session(Session)
Base.query = session.query_property()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, unique=True, primary_key=True,  autoincrement=True)
    login = Column('login', String, unique=True)
    password = Column('password', String, unique=True)
    key = Column('key', String, unique=True)
    tokenn = Column('token', String, unique=True)

    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    def additional(self, key, token):
        self.key = key
        self.token = token

# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
# admin = Users('admin', "123")
# session.add(admin)
# session.commit()