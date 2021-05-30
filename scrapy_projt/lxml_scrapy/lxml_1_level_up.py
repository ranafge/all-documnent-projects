from lxml import etree
t = '''<a>
  <b>
    <c>X:1 Y:0</c>
    <c>X:1 Y:0</c>
    <c>X:2 Y:0</c>
  </b>
  <b>
    <c>X:1 Y:0</c>
    <c>X:2 Y:0</c>
  </b>
</a>'''
r = etree.fromstring(text=t)
print(r.xpath('//a/b[2]/c/[./c/text()]'))
