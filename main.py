def main():
    # let's start with the oxford 3000, and then maybe do 3of6game or 2of12inf
    #
    print(shorten("palace", 4))
    return


def shorten(word, reveal_from_left=1, reveal_from_right=1, middle_treshold=1):
    middle_length = len(word) - reveal_from_left - reveal_from_right
    if middle_length <= middle_treshold:
        return word
    return word[:reveal_from_left] + str(middle_length) + word[-reveal_from_right:]


if __name__ == "__main__":
    main()
