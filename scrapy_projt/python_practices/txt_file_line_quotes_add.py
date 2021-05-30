my_list = ["hello", "bye", "good morning", "good evening", "'yes", "''no'"]

with open('foo.txt', 'w') as writefile:
    writefile.writelines(f'"{w.strip()}"\n'for w in my_list)
with open('foo2.txt', 'w') as f:
    f.write('"'+ "'\n'".join(my_list) + '"')
