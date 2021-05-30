from bs4 import BeautifulSoup as bs

html = '''<div id="column2_A415"> 
   <h2 class="content_header content_header_yellow"><strong>Date</strong></h2> 
   <p><strong>Case</strong></p> 
   <p>Summary</p> 
   <h2 class="content_header content_header_yellow"><strong>Date</strong></h2> 
   <p><strong>Case</strong></p> 
   <p>Summary</p>
  </div>'''

soup = bs(html, 'lxml') # 'html.parser'
cases = [p.text for p in soup.select('p:has(strong)')]
summaries = [p.text for p in soup.select('p:not(:has(strong))')]
print('cases: ', cases, ' summaries: ', summaries)
