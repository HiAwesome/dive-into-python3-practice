from pprint import pprint

import httplib2
from urllib.parse import urlencode
from file_path_collect import output_cache_path_dir as cache

httplib2.debuglevel = 1
h = httplib2.Http(cache)
identi_ca = 'https://identi.ca/api/statuses/update.xml'

data = {'status': 'Test update from Python 3'}
print(urlencode(data))

h.add_credentials('diveintomark', 'random_password', 'identi.ca')
resp, content = h.request(identi_ca,
                          'POST',
                          urlencode(data),
                          headers={'Content-Type': 'application/x-www-form-urlencoded'})
print()

print(resp.status)
print(len(content))

"""
status=Test+update+from+Python+3
connect: (identi.ca, 443)
send: b'POST /api/statuses/update.xml HTTP/1.1\r\nHost: identi.ca\r\nContent-Length: 32\r\ncontent-type: application/x-www-form-urlencoded\r\nuser-agent: Python-httplib2/0.17.3 (gzip)\r\naccept-encoding: gzip, deflate\r\n\r\n'
send: b'status=Test+update+from+Python+3'
reply: 'HTTP/1.1 404 Not Found\r\n'
header: X-Powered-By: Express
header: Vary: X-HTTP-Method-Override, Accept-Encoding
header: Server: pump.io/5.1.0 express/4.16.3 node.js/v4.2.6
header: Content-Security-Policy: default-src 'self'
header: X-Content-Security-Policy: connect-src 'self' wss://identi.ca; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdnjs.cloudflare.com ajax.googleapis.com; style-src 'self' 'unsafe-inline' cdnjs.cloudflare.com maxcdn.bootstrapcdn.com; font-src 'self' cdnjs.cloudflare.com; img-src *; object-src 'none'; media-src *; child-src 'self' www.youtube.com; frame-ancestors 'none'
header: X-WebKit-CSP: connect-src 'self' wss://identi.ca; script-src 'self' 'unsafe-inline' 'unsafe-eval' cdnjs.cloudflare.com ajax.googleapis.com; style-src 'self' 'unsafe-inline' cdnjs.cloudflare.com maxcdn.bootstrapcdn.com; font-src 'self' cdnjs.cloudflare.com; img-src *; object-src 'none'; media-src *; child-src 'self' www.youtube.com; frame-ancestors 'none'
header: X-Frame-Options: DENY
header: X-Download-Options: noopen
header: X-Content-Type-Options: nosniff
header: X-XSS-Protection: 1; mode=block
header: Content-Type: text/html; charset=utf-8
header: Content-Length: 163
header: Date: Mon, 27 Apr 2020 02:01:48 GMT
header: Connection: keep-alive

404
163
"""
