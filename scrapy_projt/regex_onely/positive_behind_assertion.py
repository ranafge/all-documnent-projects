import re
"""need a positive lookbehind assertion, i.e., match a comma if it is preceded
by a $ (note that $ needs to be escaped as \$) followed by a digit (\d). Tr"""

s = 'AUDC,AUDIOCODES COM,+55,27.49,26.47,"$1,455.85",($56.10),($56.10),-3.71%'

# pattern = r'(?<=\$\d),'

print(re.sub(r"(?<=([COM|\)])),",'xxx', s))

text = 'RT @u1, @u2, u3, @u4, rt @u5:, @u3.@u1^, rt@u3'

print(re.findall(r"(?:^|[,.])\s*@(\w+)", text))
