import models
import log_crud

"""
look_up function
"""

def look_up(query):
    models.init_db()
    try:
        result = models.EsperantoEntry.get(models.EsperantoEntry.word == query.lower())
        return result
    except:
        pass
    try:
        result = models.EsperantoEntry.get(models.EsperantoEntry.word == get_root(query).lower())
        return result
    except:
        pass
    try:
        result = models.EsperantoEntry.get(models.EsperantoEntry.word == get_infinitive(query).lower())
        return result
    except:
        pass
    return None

def get_root(word):
    if word[len(word) - 2:len(word)] == "jn":
        return word[0:len(word)-2]
    elif word[len(word) - 1] == "n":
        return word[0:len(word)-1]
    elif word[len(word) - 1] == "j":
        return word[0:len(word)-1]
    else:
        return None

def get_infinitive(word):
    verb_suffixes = ["as", "is", "os", "us", "u", "ant", "int", "ont", "at", "it", "ot"]
    for suffix in verb_suffixes:
        if word[len(word) - len(suffix):len(word)] == suffix:
            return word[0:len(word)-len(suffix)] + "i"
    return None

"""
insert function
"""

def insert(word, definition, part_of_speech="", frequency=0):
    results = models.EsperantoEntry.select(models.EsperantoEntry.word.lower() == word.lower())
    try:
        result = results.get()
        return word + " already exists in database at location " + result.id
    except:
        new_entry = models.EsperantoEntry.create(word=word, part_of_speech=part_of_speech, definition=definition, frequency=frequency)
        log_crud.log_change(type='esp_ins', change=(word + "\n" + part_of_speech + "\n" + definition))
        return word + " created in the database at location " + new_entry.id

"""
update function
"""

def update(id, definition=None, part_of_speech=None, frequency=None):
    try:
        result = models.EsperantoEntry.get(models.EsperantoEntry.id == id)
        old_result = result
        if definition != None:
            result.definition = definition
        if part_of_speech != None:
            result.part_of_speech = part_of_speech
        if frequency != None:
            result.frequency = frequency
        result.save()
        log_crud.log_change(type='esp_upd', change=(old_result.to_string() + "\n==========\n" + result.to_string()))
        return result.word + " entry updated!"
    except:
        return "No word found at location " + str(id)



"""
delete function
"""

def delete(id):
    try:
        entry = models.EsperantoEntry.get(models.EsperantoEntry.id == id)
        log_crud.log_change(type='esp_del', change=(entry.word + "\n" + entry.part_of_speech + "\n" + entry.definition))
        entry.delete()
        return entry.word + " was deleted from the database"
    except:
        return "There is no word at location " + str(id)
