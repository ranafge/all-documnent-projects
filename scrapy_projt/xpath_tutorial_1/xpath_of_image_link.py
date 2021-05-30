from scrapy.selector import Selector

html ="""<div class="lookInsideDiv" style="display: block;">
                <div class="exitBtn"><i class="ion-close-round"></i></div>
                <div class="pagesArea">
                    <ul class="list-unstyled pages">
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/fc955fd4b_117698-1.jpg"></li>
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/11f94595e_117698-2.jpg"></li>
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/555959ec2_117698-3.jpg"></li>
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/81b071d0c_117698-4.jpg"></li>
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/30ef8b806_117698-5.jpg"></li>
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/6cb40391f_117698-6.jpg"></li>
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/a41c97880_117698-7.jpg"></li>
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/d1a4bff6e_117698-8.jpg"></li>
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/9503cfda1_117698-9.jpg"></li>
                            <li><img src="https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/54f1774ee_117698-10.jpg"></li>
                    </ul>
                </div>
            </div>"""


data = Selector(text=html)
look_inside_image_urls = data.xpath('//*/ul[@class="list-unstyled pages"]/li/img/@src').extract()
for i in look_inside_image_urls:
    print("============> look_inside_image_urls ===============>", i)


============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/fc955fd4b_117698-1.jpg
============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/11f94595e_117698-2.jpg
============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/555959ec2_117698-3.jpg
============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/81b071d0c_117698-4.jpg
============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/30ef8b806_117698-5.jpg
============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/6cb40391f_117698-6.jpg
============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/a41c97880_117698-7.jpg
============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/d1a4bff6e_117698-8.jpg
============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/9503cfda1_117698-9.jpg
============> look_inside_image_urls ===============> https://s3-ap-southeast-1.amazonaws.com/rokomari110/LookInside20190827/54f1774ee_117698-10.jpg

Process finished with exit code 0

from scrapy import Request
req = Request(url, headers={"USER-AGENT" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 OPR/45.0.2552.888"})
fetch(req)
