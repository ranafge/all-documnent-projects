from lxml import etree
html ="""<Values>
   <Value Value="a" CustomAtr="1" />
   <Value Value="b" CustomAtr="2" />
   <Value Value="c" CustomAtr="3" />
</Values>"""

root = etree.fromstring(text=html)
print(etree.tostring(root, pretty_print=True))
print(root.xpath("string(//Value[@Value='b']/@CustomAttr)"))
