djtext = "g o d  i s   gre at"
analyzed = ""
for index, char in enumerate(djtext):
    if djtext[index] != " " and djtext[index+1] !=" ":
        pass
    elif djtext[index] != " " and djtext[index+1] ==" ":
            analyzed += djtext[index] + djtext[index+1]

print(analyzed)