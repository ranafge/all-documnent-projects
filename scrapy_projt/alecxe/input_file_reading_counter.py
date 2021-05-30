from collections import Counter

results = Counter()
with open('note.text', 'r') as f:
    for line in f:
        if line.strip().startswith('-'):
            continue
        results.update(line.strip())
print(results)
print(results.most_common(4))
