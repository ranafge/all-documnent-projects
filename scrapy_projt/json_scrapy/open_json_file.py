import json

json_file =  """{"delete":{"status":{"id":509743302972043264,"id_str":"509743302972043264","user_id":1366812392,"user_id_str":"1366812392"},"timestamp_ms":"1410368494532"}}
{"delete":{"status":{"id":64472572007428096,"id_str":"64472572007428096","user_id":31473446,"user_id_str":"31473446"},"timestamp_ms":"1410368494565"}}
{"created_at":"Wed Sep 10 17:01:34 +0000 2014","id":509748529070616576,"id_str":"509748529070616576","text":"Metin \u015eent\u00fcrk 
Twitterda @metinsenturk MUHTE\u015eEM \u00dc\u00c7L\u00dc; SEN, BEN, M\u00dcZ\u0130K","source":"\u003ca href=\"http:\/\/www.twitter.com\" 
rel=\"nofollow\"\u003eTwitter for Windows\u003c\/a\u003e","truncated":false,"in_reply_to_status_id":null,"in_reply_to_status_id_str":
null,"in_reply_to_user_id":null,"in_reply_to_user_id_str":null,"in_reply_to_screen_name":null,"user":{"id":2748960160,"id_str":"2748960160","name":"Enise Erkuzu\n",
"screen_name":"eniseerkuzu38","location":"Denizli\n","url":null,"description":"Tipe bakarak a\u015f\u0131k olanlar , am\u0131n\u0131za koyay\u0131m.",
"protected":false,"verified":false,"followers_count":36,"friends_count":32,"listed_count":0,"favourites_count":75,"statuses_count":595,"created_at":
"Thu Aug 21 10:17:18 +0000 2014","utc_offset":null,"time_zone":null,"geo_enabled":false,"lang":"en","contributors_enabled":false,"is_translator":false,
"profile_background_color":"C0DEED","profile_background_image_url":"http:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_image_url_https":
"https:\/\/abs.twimg.com\/images\/themes\/theme1\/bg.png","profile_background_tile":false,"profile_link_color":"0084B4","profile_sidebar_border_color":"C0DEED",
"profile_sidebar_fill_color":"DDEEF6","profile_text_color":"333333","profile_use_background_image":true,"profile_image_url":
"http:\/\/pbs.twimg.com\/profile_images\/502399080686190592\/tRqoEQyM_normal.jpeg","profile_image_url_https":"https:\/\/pbs.twimg.com\/profile_images\/502399080686190592\/tRqoEQyM_normal.jpeg",
"default_profile":true,"default_profile_image":false,"following":null,"follow_request_sent":null,"notifications":null},"geo":null,"coordinates":null,"place":null,"contributors":null,
"retweet_count":0,"favorite_count":0,"entities":{"hashtags":[],"trends":[],"urls":[],"user_mentions":[{"screen_name":"metinsenturk","name":"Metin \u015eent\u00fcrk","id":523497734,"id_str":"523497734","indices":[24,37]}],
"symbols":[]},"favorited":false,"retweeted":false,"possibly_sensitive":false,"filter_level":"medium","lang":"tr","timestamp_ms":"1410368494662"}"""


data = json.loads(json_file)

print(data)
