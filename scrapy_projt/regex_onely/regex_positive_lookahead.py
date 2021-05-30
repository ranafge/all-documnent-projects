import re
text ="""SAMAndMAX 
SAMAndMax 
SamAndMax 
SamAndMAX"""

res = re.split(r"(?=[A-Z][a-z])|(?=[a-z])(?=[A-Z])|[\n]", text)
print(res)
