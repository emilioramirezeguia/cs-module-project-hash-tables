import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    words = words.split()


# iterate through that list of words
# check whether that word is in dictionary as a key
# if key alredy exists, append to list value
# use 2 lists to keep track of words that start and stop

# -- sentence generator --
# helper function that chooses random word based on an input
# second helper function used first helper function to generate a sentence until end word is chosen (contains input word and loop)

# -- hint --

# keep track of the word next to index in a list
# if the word is already in dictionary

# TODO: analyze which words can follow other words
dictionary = {}
start = []
stop = []
stop_characters = [".", "?", "!"]
for i in range(len(words) - 1):

    if words[i] not in dictionary:
        dictionary[words[i]] = [words[i + 1]]
        if words[i].isupper() or words[i][0:2] == '"':
            start.append(words[i])
        if words[i][-1] in stop_characters or words[i][-2:] == '"':
            stop.append(words[i])
    else:
        dictionary[words[i]].append(words[i + 1])

random_word = random.choice(words)

print("Dictionry", dictionary)
print("Start", start)
print("Stop", stop)
print("Random Word", random_word)

# TODO: construct 5 random sentences
# Your code here
