import re
print(re.sub(r"\d(?![GJK])", "", "On 11 December 2008, India entered the 3G arena 1A 3J 5K"))

print(re.findall(r"\d+(?![GJK])","On 11 December 2008, India entered the 3G arena 1A 3J 5K" ))
