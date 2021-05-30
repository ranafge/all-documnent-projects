import pandas as pd
# unique in insertion ordered.
items = [1,2,0,1,3,2]
print(list(dict.fromkeys(items)))

print(list(dict.fromkeys('ab3fwoifnsdnajefwfjweae')))

print(pd.Series([1,2,3,4,2,2,34,2,]).drop_duplicates().tolist())
