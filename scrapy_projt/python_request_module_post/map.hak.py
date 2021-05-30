import requests
import json
import requests

headers = {
    'authority': 'firebaselogging-pa.googleapis.com',
    'pragma': 'no-cache',
    'cache-control': 'no-cache',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'content-type': 'text/plain;charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://www.myntra.com',
    'x-client-data': 'CJC2yQEIorbJAQipncoBCPjHygEIo83KAQjc1coBCKicywEIxZzLAQjknMsBCKmdywE=',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.myntra.com/',
    'accept-language': 'en-US,en;q=0.9',
}

params = (
    ('key', 'AIzaSyCx80ru6-RXeTi3GvqkFsMVyMf-vpgIoVw'),
)

data = '{"request_time_ms":"1613876175998","client_info":{"client_type":1,"js_client_info":{}},"log_source":462,"log_event":[{"source_extension_json_proto3":"{\\"application_info\\":{\\"google_app_id\\":\\"1:787245060481:web:d39d481d3b10f7e0a51880\\",\\"app_instance_id\\":\\"fy2lHhsQcQR5KsGJy5euMo\\",\\"web_app_info\\":{\\"sdk_version\\":\\"0.4.5\\",\\"page_url\\":\\"https://www.myntra.com/men\\",\\"service_worker_status\\":2,\\"visibility_state\\":1,\\"effective_connection_type\\":4},\\"application_process_state\\":0},\\"network_request_metric\\":{\\"url\\":\\"https://sslwidget.criteo.com/event\\",\\"http_method\\":0,\\"http_response_code\\":200,\\"response_payload_bytes\\":444,\\"client_start_time_us\\":1613876166428681,\\"time_to_response_initiated_us\\":270389,\\"time_to_response_completed_us\\":271824}}","event_time_ms":"1613876166704"}]}'

response = requests.post('https://firebaselogging-pa.googleapis.com/v1/firelog/legacy/log', headers=headers, params=params, data=data)
print(response.status_code)
print(response.text)
