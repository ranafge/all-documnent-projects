n_pword = "hello"
split_n_pword = []
n=0

for letter in n_pword:
    split_n_pword.append(letter)

print(split_n_pword)

encrypt = 'abcdefghijklmnopqrstuvwxyz'
for letter in n_pword:
    index = encrypt.index(split_n_pword[n])
    print(index)
#     ceaser = 2
#     encrypted_letter = encrypt[index-ceaser]
#     n=n+1
# print(encrypted_letter)
