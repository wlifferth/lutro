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
