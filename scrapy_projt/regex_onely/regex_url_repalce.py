import re

text = 's t http://www.example.com/somestuff.html?query=python ggg'

print(re.sub(r"https?:[^][]+\s", ' ', text))
