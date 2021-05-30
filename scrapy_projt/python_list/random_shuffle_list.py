import random

list_of_list_range = [[i] for i in range(5)]
print(list_of_list_range)

random.shuffle(list_of_list_range) # or
random.shuffle(list_of_list_range, random.random)
print(list_of_list_range) # genereate original list

sentence = ['this','is','a','sentence']

print('-'.join(sentence))
print(str.join(' ', sentence).join(['(',')']))

