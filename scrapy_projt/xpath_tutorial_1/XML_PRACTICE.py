import xml.etree.ElementTree as ET
xml = '''<tr>
 <td>111</td>   
 <td>222</td>                                   
 <td>20201208</td>                                 
 <td></td>                                  
 <td>26</td>                                   
 <td>1431</td>                                 
 <td></td>
</tr>'''

root = ET.fromstring(xml)
data = [td.text if td.text else "" for td in root.findall('.//td')]
print(data)
