def main():
    # let's start with the oxford 3000, and then maybe do 3of6game or 2of12inf

    word_set = {"bicycle", "because", "balance", "breathe", "believe"}
    print(shorten_set(word_set))
    return


def shorten(word, reveal_from_left=1, reveal_from_right=1, middle_threshold=1):
    middle_length = len(word) - reveal_from_left - reveal_from_right
    if middle_length <= middle_threshold:
        return word
    return word[:reveal_from_left] + str(middle_length) + word[-reveal_from_right:]


def shorten_set(word_set, reveal_from_left=1, reveal_from_right=1, middle_threshold=1):
    shorthand_map = {
        word: shorten(
            word=word,
            reveal_from_left=reveal_from_left,
            reveal_from_right=reveal_from_right,
            middle_threshold=middle_threshold,
        )
        for word in word_set
    }
    subsets = {}
    for word, shorthand in shorthand_map.items():
        subsets.setdefault(shorthand, set()).add(word)

    result = {}
    for shorthand, words in subsets.items():
        if len(words) == 1:
            result[next(iter(words))] = shorthand
        elif len(words) > 1:
            # consider checking left and right letters, and choosing the direction with the most unique letters
            result.update(
                shorten_set(
                    word_set=words,
                    reveal_from_left=reveal_from_left + 1,
                    reveal_from_right=reveal_from_right,
                    middle_threshold=middle_threshold,
                )
            )

    return result


if __name__ == "__main__":
    main()
