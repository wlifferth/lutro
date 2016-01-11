import models

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

def insert(word, definition, part_of_speech="", frequency=0, lang="esp"):
    results = models.EsperantoEntry.select(models.EsperantoEntry.word.lower() == word.lower())
    try:
        result = results.get()
        return word + " already exists in database at location " + result.id
    except:
        new_entry = models.EsperantoEntry.create(word=word, part_of_speech=part_of_speech, definition=definition, frequency=frequency)
        return word + " created in the database at location " + new_entry.id

"""
update function
"""

def update(id, definition, part_of_speech, frequency):
    try:
        result = models.EsperantoEntry.get(models.EsperantoEntry.id == id)
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

def delete(id):
    try:
        entry = models.EsperantoEntry.get(models.EsperantoEntry.id == id)
        entry.delete()
        return entry.word + " was deleted from the database"
    except:
        return "There is no word at location " + str(id)
