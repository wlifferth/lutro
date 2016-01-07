from peewee import *

db = SqliteDatabase("lutro.db")


class Entry(Model):
    id = IntegerField(primary_key=True)
    word = CharField(unique=True)
    part_of_speech = CharField(null=True)
    definition = TextField()

    class Meta:
        database = db

class EsperantoEntry(Entry):
    pass

def init_db():
    db.connect
    db.create_tables([EsperantoEntry], safe=True)
