from bs4 import BeautifulSoup
import requests
response = """<div class="snapshot__body-content">
	<div class="snapshot__col1">
		<ul class="snapshot__details list-unstyled">
			<li class="snapshot__details-price">
				<sup>
                  $
                 </sup>
                 41,991
                 
				
				<!-- -->
				<a class="btn-link snapshot__details-monthly hidden-xs hidden-sm" href="/vehicle/details/73082384">
					<sup>
                   $
                  </sup>
					<span>
                   550
                  </span>
                  /mo*
                 
				
				</a>
			</li>
		</ul>
	</div>
</div>"""
soup = BeautifulSoup(response, 'lxml')

for data in soup.find_all('li',{"class":"snapshot__details-price"}):
    print(data.get_text(strip=True).rsplit('$', maxsplit=1)[0])
