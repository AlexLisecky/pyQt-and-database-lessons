from sqlalchemy import create_engine, MetaData, Table, String, Integer, Column, ForeignKey, select
from sqlalchemy.orm import mapper, sessionmaker


class ChinookDatabase:
    class Artists:
        def __init__(self, name):
            self.Artistid = None
            self.Name = name

    class Albums:
        def __init__(self, title, artistid):
            self.Title = title
            self.Artistid = artistid
            self.id = None

    def __init__(self):
        # создание движка БД
        self.engine = create_engine('sqlite:///chinook.sqlite')

        # создание обьекта Metadata
        self.metadata = MetaData()

        artists_table = Table('artists', self.metadata,
                              Column('Artistid', primary_key=True),
                              Column('Name', String),
                              )

        albums_table = Table('albums', self.metadata,
                             Column('Title', String),
                             Column('Artistid', ForeignKey('artists.Artistid')),
                             Column('Albumid', primary_key=True)
                             )

        self.metadata.create_all(self.engine)

        mapper(self.Artists, artists_table)
        mapper(self.Albums, albums_table)

        Session = sessionmaker(bind=self.engine)

        self.session = Session()

        self.session.commit()
        print('дошел')

    def all_artists(self):
        query = self.session.query(
            self.Artists.Artistid,
            self.Artists.Name
        )

        return query.all()

    def all_album(self):
        query = self.session.query(
            self.Artists.Name,
            self.Albums.Title,
        ).join(self.Albums)

        return query.all()

    def choose_album(self, artist):
        artist_id = self.session.query(self.Artists.Artistid).filter_by(Name=artist)
        # альтернативный способ
        # sel = select([self.Albums.Title]).where(self.Albums.Artistid == artist_id.first()[0])
        # result = self.session.connection().execute(sel).fetchall()

        query = self.session.query(
            self.Artists.Name,
            self.Albums.Title
        ).filter_by(Artistid=artist_id.first()[0]).join(self.Artists)

        return query.all()


# > from sqlalchemy import select
# >>> sel = select([User.name, User.fullname]).\
# ...         where(User.name == 'ed').\
# ...         order_by(User.id)
# >>> session.connection().execute(sel).fetchall()

if __name__ == '__main__':
    db = ChinookDatabase()
    # print(db.all_artists())
    # print(db.all_album())
    print(db.choose_album('Accept'))
