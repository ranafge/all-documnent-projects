import re

print(re.search(r'(\d-\w)+.{2,3}', '1-a2-b').groups())
