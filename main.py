from random import shuffle
file = open("words.txt", "r")
data = file.readlines()
file.close()

words = []
for word in data:
  words.append(word.rstrip())

shuffle(words)
print(words[0:5])
