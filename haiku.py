import random

def init_dict(filename, syll, dict):
    f = open(filename)
    for line in f:
        dict[line.strip()] = syll
    f.close()

def make_haiku(bank):
    haiku = ""
    words = list(bank.keys())
    syll_max = 5
    stanza_count = 0

    while stanza_count != 3:
        choice = random.choice(words)
        if bank.get(choice) <= syll_max:
            haiku += choice + " "
            syll_max -= bank.get(choice)
            if syll_max != 0:
                continue
            else:
                haiku += "\n"
                stanza_count += 1
                if stanza_count == 1:
                    syll_max = 7
                else:
                    syll_max = 5

    return haiku


def init_bank():
    bank = {}

    init_dict("1-syllable.txt", 1, bank)
    init_dict("2-syllable.txt", 2, bank)
    init_dict("3-syllable.txt", 3, bank)
    init_dict("4-syllable.txt", 4, bank)

    return bank
