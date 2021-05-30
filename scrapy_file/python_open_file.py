# def ini(dna):
#     symbols = ["A", "C", "G", "T"]
#     symbols_count = {i: dna.count(i) for i in symbols}
#     return symbols_count
#
# if __name__ == "__main__":
#     with open('requirements.txt', 'r') as file:
#         dna = file.readline()
#     symbols_count = ini(dna)
#     for k, v in symbols_count.items():
#         print(v, end=" ")
with open('required_text_stackoverflow.txt', 'r') as file:
    data = file.readlines()
    for d in data:
        print(d.strip('\n'))
