from collections import Counter
with open('fich_teste.txt',  'r') as f:
    word_per_line = [len(line.split(';')) for line in f.readlines()]
    print(len(word_per_line))
    print(sum(word_per_line))
    # lines = [l.strip() for l in f.readlines()]
    # mywords = []
    # for w in lines:
    #     mywords.extend(w.split(';'))
    # print(mywords)
    # print(len(mywords))
    # print('Lines: %s and \n total lines: %s' %(lines, len(lines)))


def leftover(letter_set, string):
    lcount, scount = Counter(letter_set), Counter(string)
    print(lcount)
    # print(scount)
    repeat = min(scount[l] // lcount[l] for l in lcount)
    print(repeat, 'xx')
    for l in lcount:
        string = string.replace(l, "", lcount[l] * repeat)
    return f"{repeat} {letter_set}, left over is {string}"


print(leftover("reindeer", "ierndeBeCrerindAeer"))
print(leftover("reindeer", "ierndeBeCrerindAeere"))
print(leftover("reindeer", "ierndeBeCrerindAee"))
