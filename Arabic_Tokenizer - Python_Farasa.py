# This an Arabic tokenizer using the Farasa segmenter API
# Code is from here http://alt.qcri.org/farasa/
#Edited by Yousra Hesham
#Date 25/06/2019
# Result: Worked after adjudtment on the original code

import http.client

conn = http.client.HTTPSConnection("farasa-api.qcri.org")

payload = '{\"text\": \"السلام عليكم ورحمة الله و بركاته\"}'
# This is causing an error as the characters need to be identified as unicode


headers = { 'content-type': 'application/json', 'cache-control': 'no-cache', }

conn.request("POST", "/msa/webapi/segmenter", payload.encode('utf-8'), headers)

res = conn.getresponse()

data = res.read()

print(data.decode('utf-8'))
