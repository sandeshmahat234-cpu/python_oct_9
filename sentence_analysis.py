text = input("Enter a sentence: ")
words = text.split()
lowercase_words = [word.lower() for word in words]
python_count = lowercase_words.count("python")
print("Words in the sentence:", words)
print("converting all words to lowercase:", lowercase_words)
print("count of words in the sentence:", len(words))
print("count of the word 'python':", python_count)
print("The longest word in the sentence is:", max(words, key=len))

