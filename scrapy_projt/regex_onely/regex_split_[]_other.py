import re
formula = '[var1]+[v/ar/2]^var3/var4'

res = re.split(r"(\[[^][]+])|[-+^/]" , formula)
print(res)
final_res = list(filter(None,res))
print(final_res)
