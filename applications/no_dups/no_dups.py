def no_dups(s):
    dictionary = {}

    words = s.split()
    new_s = ""

    for word in words:
        if word not in dictionary:
            dictionary[word] = word

    for key in dictionary:
        new_s = new_s + " " + dictionary[key]

    new_s = new_s.strip()
    return new_s


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
