class Result:
    def __init__(self, word, entry=""):
        self.word = word
        self.entry = entry

def look_up(query):
    query = query.lower()
    if query in dictionary:
        return get_esp_result(query)
    elif get_root(query) in dictionary:
        return get_esp_result(get_root(query))
    elif get_infinitive(query) in dictionary:
        return get_esp_result(get_infinitive(query))
    else:
        return Result(word=query, entry="was not in the dictionary")


def print_result(result):
    print("\n")
    print(result)
    print("\n")


def get_esp_result(query):
    entry = dictionary[query]
    entry = entry[0:len(entry)-1]
    result = Result(word=query, entry=entry)
    return result

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


def search_english(query):
    relevant_keys = []
    for key, value in dictionary:
        if query in value:
            relevant_keys.append(key)
    if relevant_keys != []:
        return relevant_keys
    return None

f = open('esperanto-dict.txt')
dictionary = {}
while True:
    line = f.readline()
    if line == "":
        break
    esperanto, english = line.split(" : ")
    dictionary[esperanto] = english

print("Dictionary successfully read in.")
