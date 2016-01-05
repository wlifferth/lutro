from peewee import *

db = SqliteDatabase("esp-eng-dictionary.db")


class Entry(Model):
    id = IntegerField(primary_key=True)
    word = CharField(unique=True)
    part_of_speech = CharField(null=True)
    definition = TextField()
    class Meta:
        database = db

class EsperantoEntry(Entry):
    pass

db.connect

db.create_tables([EsperantoEntry], safe=True)

import esperanto

dictionary = esperanto.dictionary

duplicates = []
added_count = 0
for key, value in sorted(dictionary.items()):
    if key[len(key)-1] == "o":
        part_of_speech = "noun"
        EsperantoEntry.create(word=key, definition=value, part_of_speech=part_of_speech)
    elif key[len(key)-1] == "i":
        part_of_speech = "verb"
        EsperantoEntry.create(word=key, definition=value, part_of_speech=part_of_speech)
    elif key[len(key)-1] == "a":
        part_of_speech = "adjective"
        EsperantoEntry.create(word=key, definition=value, part_of_speech=part_of_speech)
    elif key[len(key)-1] == "e":
        part_of_speech = "adverb"
        EsperantoEntry.create(word=key, definition=value, part_of_speech=part_of_speech)
    else:
        EsperantoEntry.create(word=key, definition=value)

print(duplicates)
print(str(added_count) + " total words added")
