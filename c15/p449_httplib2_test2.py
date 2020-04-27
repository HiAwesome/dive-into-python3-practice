from pprint import pprint

import httplib2

from file_path_collect import output_cache_path_dir as cache

httplib2.debuglevel = 1
h = httplib2.Http(cache)
# 网址换成简书
jianshu = 'https://www.jianshu.com/'

# 首先 cache 一遍
response0, content0 = h.request(jianshu)
print()

response, content = h.request(jianshu)
print()

print(len(content))
print()

print(response.status)
print()

print(response.fromcache)
print()

response2, content2 = h.request(jianshu, headers={'cache-control': 'no-cache'})
print()

print(response2.status)
print()

print(response2.fromcache)
print()

pprint(dict(response2.items()))

"""
connect: (www.jianshu.com, 443)
send: b'GET / HTTP/1.1\r\nHost: www.jianshu.com\r\nuser-agent: Python-httplib2/0.17.3 (gzip)\r\naccept-encoding: gzip, deflate\r\nif-none-match: W/"bbd77e231f5e58fa82c8623683fdc1a1"\r\n\r\n'
reply: 'HTTP/1.1 304 Not Modified\r\n'
header: Server: Tengine
header: Date: Mon, 27 Apr 2020 01:42:48 GMT
header: Connection: keep-alive
header: X-Frame-Options: SAMEORIGIN
header: X-XSS-Protection: 1; mode=block
header: X-Content-Type-Options: nosniff
header: Content-Security-Policy: script-src 'self' 'unsafe-inline' 'unsafe-eval' *.jianshu.com *.jianshu.io *.nkscdn.com *.huanqiu.com post.star-media.cn api.geetest.com static.geetest.com dn-staticdown.qbox.me zz.bdstatic.com *.google-analytics.com hm.baidu.com nkscdn.com push.zhanzhang.baidu.com res.wx.qq.com qzonestyle.gtimg.cn as.alipayobjects.com nbrecsys.4paradigm.com shared.ydstatic.com gorgon.youdao.com *.googlesyndication.com adservice.google.com www.googletagservices.com ;style-src 'self' 'unsafe-inline' *.jianshu.com *.jianshu.io api.geetest.com static.geetest.com shared.ydstatic.com ;
header: ETag: W/"bbd77e231f5e58fa82c8623683fdc1a1"
header: Cache-Control: max-age=0, private, must-revalidate
header: Set-Cookie: signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; path=/
header: Set-Cookie: read_mode=day; path=/
header: Set-Cookie: default_font=font2; path=/
header: Set-Cookie: locale=zh-CN; path=/
header: X-Request-Id: 7d5de11a-339b-4ef1-a3e6-ecdb96bf70a8
header: X-Runtime: 0.015455
header: Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

send: b'GET / HTTP/1.1\r\nHost: www.jianshu.com\r\nuser-agent: Python-httplib2/0.17.3 (gzip)\r\naccept-encoding: gzip, deflate\r\nif-none-match: W/"bbd77e231f5e58fa82c8623683fdc1a1"\r\n\r\n'
reply: 'HTTP/1.1 304 Not Modified\r\n'
header: Server: Tengine
header: Date: Mon, 27 Apr 2020 01:42:48 GMT
header: Connection: keep-alive
header: X-Frame-Options: SAMEORIGIN
header: X-XSS-Protection: 1; mode=block
header: X-Content-Type-Options: nosniff
header: Content-Security-Policy: script-src 'self' 'unsafe-inline' 'unsafe-eval' *.jianshu.com *.jianshu.io *.nkscdn.com *.huanqiu.com post.star-media.cn api.geetest.com static.geetest.com dn-staticdown.qbox.me zz.bdstatic.com *.google-analytics.com hm.baidu.com nkscdn.com push.zhanzhang.baidu.com res.wx.qq.com qzonestyle.gtimg.cn as.alipayobjects.com nbrecsys.4paradigm.com shared.ydstatic.com gorgon.youdao.com *.googlesyndication.com adservice.google.com www.googletagservices.com ;style-src 'self' 'unsafe-inline' *.jianshu.com *.jianshu.io api.geetest.com static.geetest.com shared.ydstatic.com ;
header: ETag: W/"bbd77e231f5e58fa82c8623683fdc1a1"
header: Cache-Control: max-age=0, private, must-revalidate
header: Set-Cookie: signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; path=/
header: Set-Cookie: read_mode=day; path=/
header: Set-Cookie: default_font=font2; path=/
header: Set-Cookie: locale=zh-CN; path=/
header: X-Request-Id: f5fbdb6f-da87-43e3-a5f4-6724b66d3b5f
header: X-Runtime: 0.006987
header: Strict-Transport-Security: max-age=31536000; includeSubDomains; preload

23483

200

True

send: b'GET / HTTP/1.1\r\nHost: www.jianshu.com\r\ncache-control: no-cache\r\nuser-agent: Python-httplib2/0.17.3 (gzip)\r\naccept-encoding: gzip, deflate\r\n\r\n'
reply: 'HTTP/1.1 200 OK\r\n'
header: Server: Tengine
header: Date: Mon, 27 Apr 2020 01:42:48 GMT
header: Content-Type: text/html; charset=utf-8
header: Transfer-Encoding: chunked
header: Connection: keep-alive
header: Vary: Accept-Encoding
header: X-Frame-Options: SAMEORIGIN
header: X-XSS-Protection: 1; mode=block
header: X-Content-Type-Options: nosniff
header: Content-Security-Policy: script-src 'self' 'unsafe-inline' 'unsafe-eval' *.jianshu.com *.jianshu.io *.nkscdn.com *.huanqiu.com post.star-media.cn api.geetest.com static.geetest.com dn-staticdown.qbox.me zz.bdstatic.com *.google-analytics.com hm.baidu.com nkscdn.com push.zhanzhang.baidu.com res.wx.qq.com qzonestyle.gtimg.cn as.alipayobjects.com nbrecsys.4paradigm.com shared.ydstatic.com gorgon.youdao.com *.googlesyndication.com adservice.google.com www.googletagservices.com ;style-src 'self' 'unsafe-inline' *.jianshu.com *.jianshu.io api.geetest.com static.geetest.com shared.ydstatic.com ;
header: ETag: W/"bbd77e231f5e58fa82c8623683fdc1a1"
header: Cache-Control: max-age=0, private, must-revalidate
header: Set-Cookie: signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; path=/
header: Set-Cookie: read_mode=day; path=/
header: Set-Cookie: default_font=font2; path=/
header: Set-Cookie: locale=zh-CN; path=/
header: X-Request-Id: efd5e128-4c05-4da6-87de-3a832d6375eb
header: X-Runtime: 0.004749
header: Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
header: Content-Encoding: gzip

200

False

{'-content-encoding': 'gzip',
 'cache-control': 'max-age=0, private, must-revalidate',
 'connection': 'keep-alive',
 'content-length': '23483',
 'content-location': 'https://www.jianshu.com/',
 'content-security-policy': "script-src 'self' 'unsafe-inline' 'unsafe-eval' "
                            '*.jianshu.com *.jianshu.io *.nkscdn.com '
                            '*.huanqiu.com post.star-media.cn api.geetest.com '
                            'static.geetest.com dn-staticdown.qbox.me '
                            'zz.bdstatic.com *.google-analytics.com '
                            'hm.baidu.com nkscdn.com push.zhanzhang.baidu.com '
                            'res.wx.qq.com qzonestyle.gtimg.cn '
                            'as.alipayobjects.com nbrecsys.4paradigm.com '
                            'shared.ydstatic.com gorgon.youdao.com '
                            '*.googlesyndication.com adservice.google.com '
                            "www.googletagservices.com ;style-src 'self' "
                            "'unsafe-inline' *.jianshu.com *.jianshu.io "
                            'api.geetest.com static.geetest.com '
                            'shared.ydstatic.com ;',
 'content-type': 'text/html; charset=utf-8',
 'date': 'Mon, 27 Apr 2020 01:42:48 GMT',
 'etag': 'W/"bbd77e231f5e58fa82c8623683fdc1a1"',
 'server': 'Tengine',
 'set-cookie': 'signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; path=/, '
               'read_mode=day; path=/, default_font=font2; path=/, '
               'locale=zh-CN; path=/',
 'status': '200',
 'strict-transport-security': 'max-age=31536000; includeSubDomains; preload',
 'transfer-encoding': 'chunked',
 'vary': 'Accept-Encoding',
 'x-content-type-options': 'nosniff',
 'x-frame-options': 'SAMEORIGIN',
 'x-request-id': 'efd5e128-4c05-4da6-87de-3a832d6375eb',
 'x-runtime': '0.004749',
 'x-xss-protection': '1; mode=block'}
"""
