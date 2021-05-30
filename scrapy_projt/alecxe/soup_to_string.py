from collections import Counter

results = {}
dict_list = [{"rp": 1, "vi": 100}, {"rp": 2, "vi": 70}, {"rp": 1, "vi": 200}, {"rp": 1, "vi": 150},
             {"rp": 2, "vi": 300}, {"rp": 3, "vi": 120}]
print([*{d['rp']:d for d in sorted(dict_list, key=lambda d: d['vi'])}.values()])
