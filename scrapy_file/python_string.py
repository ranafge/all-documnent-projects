import re
import string
from collections import Counter
text = """Georges is my name and I like python. Oh ! your name is georges? And you like Python!
    Yes is is true, I like PYTHON
    and my name is GEORGES
"""
def make_count(text,word):
    text=text.lower()
    word= word.lower()
    dico=Counter(text.split())
    return dico[word]

if __name__ == '__main__':
    print(make_count("I am a senior citizen and I live in the Fun-Plex 'Reflexion Mirror' in Sopchoppy, Florida","'reflexion mirror'")) # should return 1
    print(make_count(text,"Python")) # should return 3
    print(make_count("James O'maley is my friend ","maley")) # should return 0
