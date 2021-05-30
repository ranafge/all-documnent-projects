book_title =  ['great', 'expectations','the', 'adventures', 'of', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']
word_counter = {}
for words in book_title:
    if words not in word_counter:
        word_counter[words] = 1
    else:
        word_counter[words] += 1

print(word_counter)
