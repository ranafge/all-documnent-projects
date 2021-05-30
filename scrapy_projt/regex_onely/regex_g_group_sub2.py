import re
name = 'XYZ'
value = '5'
content = 'XYZ.Value = 5'
res = re.sub(r'(%s\.Value\s+=\s+)([^;])' %name, r'\g<1>' + value,content)
print(res)












