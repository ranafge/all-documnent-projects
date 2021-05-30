import re
data = ['20W', '20W', '20W', '8W5K7W', '8W5K7W', '8W5K7W', '8W5K7W', '9W3K8W', '7W7R6W', '6W4R1Y4R5W', '6W1R1W5R1W1R5W',
    '6W1R1W2R1Y2R1W1R5W', '6W1R1W5R1W1R5W', '6W1R1W2R1Y2R1W1R5W', '9W3B8W', '9W3B8W', '9W3B8W', '9W3B8W', '9W3B8W', '8W5N7W']

for item in data:
    result = re.findall(r"\d+[A-Z]*", item)
    print(item, result, len(result))

