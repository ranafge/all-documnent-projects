import string
import random

pass_range = random.randint(6,10)
password=string.punctuation+string.ascii_letters+string.digits
password_choice = random.choice(password)
print(password_choice)


mygenpass = ""
for i in range(pass_range):
    mygenpass += password[i]
print(mygenpass)
print(len(mygenpass))
