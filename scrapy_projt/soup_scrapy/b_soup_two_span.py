from bs4 import BeautifulSoup

html="""<td valign="bottom" class="bottom-cell">
<div class="space rel">
    <p class="lheight16">
         <small class="breadcrumb x-normal">
               <span><i data-icon="location-filled"></i>Iasi</span>
               <span><i data-icon="location-filled"></i>Iasi</span>
         </small>
         <small class="breadcrumb x-normal">
               <span><i data-icon="clock"></i>Ieri 16:13</span>
               <span><i data-icon="clock"></i>Ieri 16:13</span>
          </small>
     </p>
 </div>
 </td>
"""
data = BeautifulSoup(html, 'lxml')
# print(data.prettify())
# print([data.find('p').find_all_next('small > i')][0])
for i in data.select('.lheight16 small span:nth-of-type(1)'):
    print(i.text)
