# for data in response.css('div.product_meta'):
#     ...:     print(data.css('span.posted_in::text').get())
#     ...:     print(data.css('span.posted_in a::text').getall()[0])
#     ...:     print(data.css('span.posted_in a::text').getall()[1])
import datetime
import json

lst = [{'api_version': None,
        'kind': None,
        'metadata': {'annotations': {'components.gke.io/component-name': 'event-exporter',
                                     'components.gke.io/component-version': '1.0.9'},
                     'cluster_name': None,
                     'creation_timestamp': str(datetime.datetime(2020, 12, 25, 23, 17, 37)),
                     'deletion_grace_period_seconds': None,
                     'deletion_timestamp': None,
                     'finalizers': None}}]

print(json.dumps(lst, indent=4)[0]['api_version'])
