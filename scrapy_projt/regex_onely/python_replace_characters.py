import re
a = ["%!It depends%% on what you m\\ean by dying.",
     "It is widely~ read and at the top_x000D_ of all the search%%__ engines.",
     "\\H~owever, Wikipedia has internal problems",
     "%%a+b!=a-b"]
print(len(a))
print([x[i] for x in a for i in range(len(a))])
# after_modified = [x.replace(i,'') for x in a ]
print([re.sub(r"%!|%|__|\\|~|_x000D_", '', str(a[i])) for i in range(len(a)) if a[i] != ''])
print([re.sub(r"%!|%|~|_x000D_|__|\\", "", str(a[i])) for i in range(len(a)) if a[i] != ""])

a = ['Champiñón 200 g',
     'Zapallo italiano Unid.',
     'Bolsa de zanahoria 1 kg',
     'Papa malla 2 Kg',
     'Palta Hass granel',
     'Limón malla 1 kg',
     'Tomate granel',
     'Brócoli 1 un.',
     'Tomate  unid']
import re

data = ['Champiñón 200 g',
'Zapallo italiano Unid.',
'Bolsa de zanahoria 1 kg',
'Papa malla 2 Kg',
'Palta Hass granel',
'Limón malla 1 kg',
'Tomate granel',
'Brócoli 1 un.',
'Tomate  unid']


splitted = []

for line in data:
    value, unit, *_ = *re.split(' ((\d|unid).*)', line, flags=re.IGNORECASE), ''

    splitted.append(value)

    if unit:
        splitted.append(unit)

print(splitted)
