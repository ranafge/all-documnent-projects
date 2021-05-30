list_of_word = ["The", "quick", "brown", "fox"]

output = []
for word in list_of_word:
    for letter in word:
        output.append(letter)
print(output)
