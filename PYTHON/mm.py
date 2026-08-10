word_count={}
setence = "This is a sample sentence. This sentence is for testing."
words = setence.split()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)