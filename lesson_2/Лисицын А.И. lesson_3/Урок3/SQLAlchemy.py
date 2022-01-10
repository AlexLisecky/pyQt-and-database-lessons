import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper

print(sqlalchemy.__version__)

ENGINE = create_engine('sqlite:///:memory:', echo=True, pool_recycle=7200)

metadata = MetaData()

users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String),
                    Column('fullname', String),
                    Column('password', String)
                    )

metadata.create_all(ENGINE)


class User:
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


mapper = mapper(User, users_table)

user = User("Вася", "Василий", "qweasdzxc")
print(user)
print(user.id)
print(ENGINE)
