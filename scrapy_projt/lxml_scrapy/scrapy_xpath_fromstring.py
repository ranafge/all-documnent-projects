from lxml import etree
html ="""<HTML>
 <BODY>
  <H1>Mr T for president</H1>
   <div>We believe the new president should be</div>
   <div>the awsome Mr T</div>
   <div>
    <H2>Mr T replies:</H2>
     <p>I pity the fool who doesn't vote</p>
     <p>for Mr T</p>
   </div>
  </BODY>
</HTML>"""

root = etree.fromstring(text=html)
print(root.xpath('//text()[contains(., "Mr T")]'))
