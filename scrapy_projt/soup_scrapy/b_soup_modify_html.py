from bs4 import BeautifulSoup
data ="""<a style="color:#85bc20" href="https://example.com?new=[sample]&hash=[hashkey]">
                                                         Unsubscribe
                                                     </a>"""
replace_link ="""<a style="color:#85bc20" href="https://example.com?new="samplevalue"&hash='123'">
                                                         Unsubscribe
                                                      </a>"""
soup = BeautifulSoup(data, 'html.parser')

link = soup.find("a", href=True)

link.replace_with(replace_link)

    # node.replace_with("samplevalue &hash='123'".format(node))

print(link.original_encoding)
# <a style="color:#85bc20" href="https://example.com?new=[sample]&hash=[hashkey]">
#                                                          Unsubscribe
#                                                      </a>
#
