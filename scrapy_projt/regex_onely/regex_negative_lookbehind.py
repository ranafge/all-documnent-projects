import re

text ="Today _asf was a null_word day__and __bla__bla"

print(re.findall(r"(?<!\bnull)_+",text))
