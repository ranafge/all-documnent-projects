import re

text = """{Hello}, [1234] (Test). This is sample data used to answer a question {Hello2} [Ch.8 p. 87 gives more information about...
"""

res = re.findall(r"\{[^{}]+\}[^{}]+p\. [0-9]+", text)
print(res)
