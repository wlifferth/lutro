from peewee import *

db = SqliteDatabase("lutro.db")


class Entry(Model):
    id = IntegerField(primary_key=True)
    word = CharField(unique=True)
    part_of_speech = CharField(null=True)
    definition = TextField()
    def to_string(self):
        return str(self.id) + "\n" + self.word + "\n" + self.part_of_speech + "\n" + self.definition

    class Meta:
        database = db

class EnglishEntry(Entry):
    pass

class EsperantoEntry(Entry):
    pass

class ChangeLogEntry(Model):
    id = IntegerField(primary_key=True)
    time_of_entry = DateTimeField()
    change_type = CharField()
    change = TextField()

    class Meta:
        database = db


def init_db():
    db.connect
    db.create_tables([EsperantoEntry, EnglishEntry, ChangeLogEntry], safe=True)
