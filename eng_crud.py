import models

"""
look_up function
"""

def look_up(query):
    models.init_db()
    try:
        result = models.EnglishEntry.get(models.EnglishEntry.word == query.lower())
        return result
    except:
        pass
    return None


"""
insert function
"""

def insert(word, definition, part_of_speech="", frequency=0):
        results = models.EnglishEntry.select(models.EnglishEntry.word.lower() == word.lower())
        try:
            result = results.get()
            return word + " already exists in database at location " + result.id
        except:
            new_entry = models.EnglishEntry.create(word=word, part_of_speech=part_of_speech, definition=definition, frequency=frequency)
            return word + " created in the database at location " + new_entry.id


"""
update function
"""


def update(id, definition, part_of_speech, frequency):
    try:
        result = models.EnglishEntry.get(models.EnglishEntry.id == id)
        result.definition = definition
        result.part_of_speech = part_of_speech
        result.frequency = frequency
        result.save()
        return result.word + " entry updated!"
    except:
        return "No word found at location " + str(id)


"""
delete function
"""

def delete(id,):
    try:
        entry = models.EnglishEntry.get(models.EnglishEntry.id == id)
        entry.delete()
        return entry.word + " was deleted from the database"
    except:
        return "There is no word at location " + str(id)
