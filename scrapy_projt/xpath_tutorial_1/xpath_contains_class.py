from scrapy.selector import Selector

html ="""<li class="ProfileNav-item ProfileNav-item--followers"><a href="/profileurl/followers" data-nav="followers" title="796,433 Followers" class="ProfileNav-stat ProfileNav-stat--link u-borderUserColor u-textCenter js-tooltip js-openSignupDialog js-nonNavigable u-textUserColor" target=""><span class="ProfileNav-label">Followers</span> <span data-is-compact="true" class="ProfileNav-value">796K</span></a></li>
<table id="my_id">
    <tbody>
        <tr>
            <th>Location:</th>
            <td>
                1600 Parkway Ave
                Los Angels
                California
            </td>
        </tr>
    </tbody>
</table>
<span>foo
  <strong>bar</strong>
</span>
"""

data = Selector(text=html)
# print(data.xpath('//*[@id="my_id"][descendant::td]/text()').getall())
# print(data.xpath('//td[contains(.,"Los Angels")]/text()').get())
# print(data.getall())
# res = data.xpath('//li[contains(@class, "ProfileNav-item")]/a/@title').get()
# print(res)
print(data.xpath("//span/text()[1]").get())
