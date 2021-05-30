import re
import json
from bs4 import BeautifulSoup

html = '''<tr id="12590559" class="">
<td>
<span class="he16-1 tip-top" title="Cracker"></span>
</td>
<td>
cracker.crc
</td>
</tr>'''

soup = BeautifulSoup("""<folder name="folder1">
     <folder name="folder2">
          <bookmark href="link.html">
     </folder>
</folder>
""", 'lxml')

print(soup.find('href').find_parent())
