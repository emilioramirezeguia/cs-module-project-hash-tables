def word_count(s):
    dictionary = {}

    # if the input is empty return empty dictionary
    if not s or '":;,.-+=/\|[]{}()*^&' in s:
        return dictionary

    # turn string to lowercase
    lowercase = s.lower()
    # split words into a list removing whitespace
    split = lowercase.split()

    # for every word in the list
    for word in split:
        # remove non-alphabet characters in the front or back of the word
        word = word.strip('":;,.-+=/\|[]{}()*^&')
        # if the word isn't in the dictionary, add it and assign it
        # the count of 1
        if word not in dictionary:
            dictionary[word] = 1
        # if it's already there, update it's count by 1
        else:
            dictionary[word] += 1

    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
