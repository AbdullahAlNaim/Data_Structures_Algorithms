word = "abcdcba"

size = len(word) - 1

newWord = ""

for i in range(len(word)):
    print(word[size])
    newWord += word[size]
    size -= 1

print(newWord == word)