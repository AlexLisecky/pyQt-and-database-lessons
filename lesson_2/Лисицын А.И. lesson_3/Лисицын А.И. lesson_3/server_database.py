from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker, query
import datetime


class ServerStorage:
    class All_client:
        def __init__(self, name):
            self.name = name
            self.last_login = datetime.datetime.now()
            self.id = None

    class History_client:
        def __init__(self, user_id, ip, port, last_login):
            self.user_id = user_id
            self.ip = ip
            self.port = port
            self.last_login = last_login
            self.id = None

    class Active_client:
        def __init__(self, user_id, ip, port, login_time):
            self.user_id = user_id
            self.ip = ip
            self.port = port
            self.login_time = login_time
            self.id = None

    def __init__(self):
        self.ENGINE = create_engine('sqlite:///server_database.sqlite', echo=False, pool_recycle=7200)
        self.metadata = MetaData()

        all_client = Table('all_client', self.metadata,
                           Column('id', Integer, primary_key=True),
                           Column('name', String, unique=True),
                           Column('last_login', DateTime),
                           )

        active_client = Table('active_client', self.metadata,
                              Column('id', Integer, primary_key=True),
                              Column('user_id', ForeignKey('all_client.id'), unique=True),
                              Column('ip', String),
                              Column('port', Integer),
                              Column('login_time', DateTime),
                              )

        history_client = Table('history_client', self.metadata,
                               Column('id', Integer, primary_key=True),
                               Column('user_id', ForeignKey('all_client.id')),
                               Column('ip', String),
                               Column('port', Integer),
                               Column('last_login', DateTime),
                               )

        self.metadata.create_all(self.ENGINE)

        mapper(self.All_client, all_client)
        mapper(self.Active_client, active_client)
        mapper(self.History_client, history_client)

        SESSION = sessionmaker(bind=self.ENGINE)
        self.SESSION_OBJ = SESSION()

        self.SESSION_OBJ.query(self.Active_client).delete()
        self.SESSION_OBJ.commit()

    def user_login(self, name, ip, port):

        result = self.SESSION_OBJ.query(self.All_client).filter_by(name=name)

        if result.count():
            user = result.first()
            user.last_login = datetime.datetime.now()
        else:
            user = self.All_client(name)

            self.SESSION_OBJ.add(user)

            self.SESSION_OBJ.commit()
            # USER = User("Вася", "Василий", "qweasdzxc")

        new_active_user = self.Active_client(user.id, ip, port, datetime.datetime.now())
        self.SESSION_OBJ.add(new_active_user)

        new_history_user = self.History_client(user.id, ip, port, datetime.datetime.now())
        self.SESSION_OBJ.add(new_history_user)

        self.SESSION_OBJ.commit()

    def user_logout(self, username):

        user = self.SESSION_OBJ.query(self.All_client).filter_by(name=username).first()

        self.SESSION_OBJ.query(self.Active_client).filter_by(user_id=user.id).delete()

        self.SESSION_OBJ.commit()

    def users_list(self):
        query = self.SESSION_OBJ.query(
            self.All_client.name,
            self.All_client.last_login,
        )

        return query.all()

    def active_users_list(self):
        query = self.SESSION_OBJ.query(
            self.All_client.name,
            self.Active_client.ip,
            self.Active_client.port,
            self.Active_client.login_time
        ).join(self.All_client)
        return query.all()

    def login_history(self, username=None):
        query = self.SESSION_OBJ.query(
            self.All_client.name,
            self.History_client.ip,
            self.History_client.port,
            self.History_client.last_login
        ).join(self.All_client)

        if username:
            query = query.filter(self.All_client.name == username)

        return query.all()


if __name__ == '__main__':
    test_db = ServerStorage()
    test_db.user_login('client_1', '192.168.1.4', 8888)
    test_db.user_login('client_2', '192.168.1.5', 7777)
    test_db.user_login('alex', '192.168.1.5', 7777)
    test_db.user_logout('client_1')
    test_db.user_logout('client_2')
    print(test_db.users_list())
    print(test_db.active_users_list())
    print(test_db.login_history('client_1'))
