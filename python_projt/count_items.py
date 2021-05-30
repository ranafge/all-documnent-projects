import webbrowser
webbrowser.open_new('http://www.python.org/')
count = 0
value = 0
sentences = 'this is'
occurrence = {}
while count < len(sentences):
    print(sentences[count])
    if not occurrence[sentences[count]] in occurrence.keys():
        occurrence[sentences[count]] = value
    else:
        occurrence[sentences[count]] = value + 1
    count += 1

print(occurrence)
