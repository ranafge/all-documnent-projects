from bs4 import BeautifulSoup

sample = """
<td class='tdtl'><a class='col' href='detail.php?id=1' target='_blank''>List 1<br>detail 1</a></td>
<td class='tdtl'><a class='col' href='detail.php?id=2' target='_blank''>List 2<br>detail 2</a></td>
<td class='tdtl'><a class='col' href='detail.php?id=3' target='_blank''>List 3<br>detail 3</a></td>
<td class='tdtl'><a class='col' href='detail.php?id=4' target='_blank''>List 4<br>detail 4</a></td>
<td class='tdtl'><a class='col' href='detail.php?id=5' target='_blank''>List 5<br>detail 5</a></td>
"""

details = [
    i.get_text() for i
    in BeautifulSoup(sample, "html.parser").find_all("a", class_="col")[1]
]

print(details)
