def almost_matches(word1, word2):
    return sum(map(str.__eq__, word1, word2)) == 3

for word in "male sale tale pile pole pace page pane pave palm peal leap play help pack".split():
    print (almost_matches("pale", word))
