WORDS_BY_LENGTH = {}
WORDS_BY_STARTS_WITH = {}
WORDS_BY_ENDS_WITH = {}

with open("word_lists/oxford_3000.txt", "r") as file:
    for word in file.readlines():
        word = word.strip("\n")
        length = len(word)
        starts_with = word[0]
        ends_with = word[-1]

        WORDS_BY_LENGTH.setdefault(length, set()).add(word)
        WORDS_BY_STARTS_WITH.setdefault(starts_with, set()).add(word)
        WORDS_BY_ENDS_WITH.setdefault(ends_with, set()).add(word)

print(WORDS_BY_LENGTH[5] & WORDS_BY_STARTS_WITH["b"] & WORDS_BY_ENDS_WITH["e"])
