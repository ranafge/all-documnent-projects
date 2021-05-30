from bs4 import BeautifulSoup
import re
import requests

html = """<select id="raff_size" name="size" class="required-entry">
                                    <option value="">Storlek</option>
                                    <option value="e8f7f9e31e2adb7ca18db3845b95a666">US 6.5</option>
                                    <option value="450b7ef575236df96a42816c448a03e0">US 7</option>
                                    <option value="c4d38ec34a0203c9799730fa75760162">US 7.5</option>
                                    <option value="3678a4bc494138c62c529f15b4103e45">US 8</option>
                                    <option value="655e5c520a63a7fd1592ea088b051e69">US 8.5</option>
                                    <option value="cb3f80e1babc079d802ca92d0760b2bd">US 9</option>
                                    <option value="ffc6670037f7ba5356247cea0537957d">US 9.5</option>
                                    <option value="7d6cde0d2cb6262febe73a0f5fef924a">US 10</option>
                                    <option value="6891a4d31dc5516e3b9fb7177bca001d">US 10.5</option>
                                    <option value="458aa765ade8646f71fb11721788454c">US 11</option>
                                    <option value="ced2d3d4b613b8a9f9bd8118bff92afe">US 11.5</option>
                            </select>"""

soup = BeautifulSoup(html,  'lxml')
# print(soup.prettify())
print(soup.find_all('option'))
values = [x['value'] for x in soup.find_all('option') if x['value']]
texes = [x.getText(strip=True, separator='|') for x in soup.find_all('option')]
print(*values)
print()
print(*texes)
values = [re.findall(r'"(.*)"',str(x))[0] for x in soup.find_all('option')]

print(*values)
