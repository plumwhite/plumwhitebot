import random

def create_reply(verb,noun):
    choice = random.randint(0,10)

    if choice < 5:
        return "Yes, " + noun + " does " + verb + ".\n#answer"
    else:
        return "No, " + noun + " does not " + verb + ".\n#answer"

def create_question(verb,noun):
    return "Does " + noun + " " + verb + "?\n#question"

def init_sets() -> tuple:
    verb_set = set()
    noun_set = set()

    verbs = open("verbs.txt")

    for line in verbs:
        verb_set.add(line.strip())

    verbs.close()

    nouns = open("nouns.txt")

    for line in nouns:
        noun_set.add(line.strip())

    nouns.close()

    return verb_set, noun_set