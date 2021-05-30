html = """<table>
    <tbody>
        <tr>
            <th colspan="8">
                <span>
                    <a href="/link">Table Title</a>
                </span>
            </th>
        </tr>
        <tr>
            <th>Info1</th>
            <th>Info2</th>
            <th>Info3</th>
            <th>Info4</th>
            <th>Info5</th>
        </tr>
        <tr>
            <td>Value1</td>
            <td>Value2</td>
            <td>Value3</td>
            <td>Value4</td>
            <td>Value5</td>
        </tr>
    </tbody>
</table>"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
value = "Value4"
trs = soup.find_all('tr')
for td in trs:
    # print(td.text.strip())
    if td.text.strip() == value:
        print(td)
