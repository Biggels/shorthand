def main():
    # let's start with the oxford 3000, and then maybe do 3of6game or 2of12inf
    words = set()
    with open("word_lists/oxford_3000.txt", "r") as file:
        for word in file.readlines():
            word = word.strip("\n").lower()
            words.add(word)

    # word_set = {"bicycle", "because", "balance", "breathe", "believe"}
    result = shorten_words(words, middle_threshold=2)
    print({word: result[word] for word in sorted(result)})
    return


def shorten_word(word, reveal_from_left=1, reveal_from_right=1, middle_threshold=1):
    middle_length = len(word) - reveal_from_left - reveal_from_right
    if middle_length <= middle_threshold:
        return word
    return word[:reveal_from_left] + str(middle_length) + word[-reveal_from_right:]


def shorten_words(
    word_set, reveal_from_left=1, reveal_from_right=1, middle_threshold=1
):
    words = sorted(word_set)
    shorthand_map = {
        word: shorten_word(
            word=word,
            reveal_from_left=reveal_from_left,
            reveal_from_right=reveal_from_right,
            middle_threshold=middle_threshold,
        )
        for word in words
    }
    subsets = {}
    for word, shorthand in shorthand_map.items():
        subsets.setdefault(shorthand, []).append(word)

    result = {}
    for shorthand in sorted(subsets):
        words = subsets[shorthand]
        if len(words) == 1:
            result[words[0]] = shorthand
        elif len(words) > 1:
            next_reveal_from_left = reveal_from_left
            next_reveal_from_right = reveal_from_right
            left_letters = {word[reveal_from_left] for word in words}
            right_letters = {word[-(reveal_from_right + 1)] for word in words}
            if len(left_letters) >= len(right_letters):
                next_reveal_from_left += 1
            else:
                next_reveal_from_right += 1
            result.update(
                shorten_words(
                    word_set=words,
                    reveal_from_left=next_reveal_from_left,
                    reveal_from_right=next_reveal_from_right,
                    middle_threshold=middle_threshold,
                )
            )

    return result


if __name__ == "__main__":
    main()
