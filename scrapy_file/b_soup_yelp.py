import requests

#  section of Review Highlights
# urls = ["https://www.yelp.ie/biz/y0pllLqKVUQi2IkhYYf9ug/review_feed?hrid=WqGBt4VQfr1vvGzie-QjLw&rh_type=phrase&rh_ident=oliver&rl=en",
# "https://www.yelp.ie/biz/y0pllLqKVUQi2IkhYYf9ug/review_feed?hrid=nlmFH44VXXAmqnKAnm0P1A&rh_type=phrase&rh_ident=dublin",
# "https://www.yelp.ie/biz/y0pllLqKVUQi2IkhYYf9ug/review_feed?hrid=OD-NXvs88PBfRaLgXPZrRQ&rh_type=phrase&rh_ident=model_s"
#         ]

# ALL the reviews down the page

urls = ["https://www.yelp.ie/biz/y0pllLqKVUQi2IkhYYf9ug/review_feed?rl=en&sort_by=relevance_desc&q=&start={}".format(i) for i in range(0,20)]

reviews = []
for url in urls:
    r=requests.get(url)
    data = r.json()
    reviews.append(data['reviews'][0]['comment']['text'])

print('length', len(reviews))
for review in reviews:
    print(review, '\n')


