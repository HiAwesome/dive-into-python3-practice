from pprint import pprint

import httplib2

from file_path_collect import output_cache_path_dir as cache

httplib2.debuglevel = 1
h = httplib2.Http(cache)
jianshu = 'https://www.jianshu.com/'

response, content = h.request(jianshu, headers={'cache-control': 'no-cache'})
print()

pprint(dict(response.items()))
print()

print(len(content))
print()

print(response.fromcache)
print(response.status)
print(response.dict['status'])

"""
connect: (www.jianshu.com, 443)
send: b'GET / HTTP/1.1\r\nHost: www.jianshu.com\r\ncache-control: no-cache\r\nuser-agent: Python-httplib2/0.17.3 (gzip)\r\naccept-encoding: gzip, deflate\r\n\r\n'
reply: 'HTTP/1.1 200 OK\r\n'
header: Server: Tengine
header: Date: Mon, 27 Apr 2020 01:52:02 GMT
header: Content-Type: text/html; charset=utf-8
header: Transfer-Encoding: chunked
header: Connection: keep-alive
header: Vary: Accept-Encoding
header: X-Frame-Options: SAMEORIGIN
header: X-XSS-Protection: 1; mode=block
header: X-Content-Type-Options: nosniff
header: Content-Security-Policy: script-src 'self' 'unsafe-inline' 'unsafe-eval' *.jianshu.com *.jianshu.io *.nkscdn.com *.huanqiu.com post.star-media.cn api.geetest.com static.geetest.com dn-staticdown.qbox.me zz.bdstatic.com *.google-analytics.com hm.baidu.com nkscdn.com push.zhanzhang.baidu.com res.wx.qq.com qzonestyle.gtimg.cn as.alipayobjects.com nbrecsys.4paradigm.com shared.ydstatic.com gorgon.youdao.com *.googlesyndication.com adservice.google.com www.googletagservices.com ;style-src 'self' 'unsafe-inline' *.jianshu.com *.jianshu.io api.geetest.com static.geetest.com shared.ydstatic.com ;
header: ETag: W/"d6b5630144393686a994679694f76474"
header: Cache-Control: max-age=0, private, must-revalidate
header: Set-Cookie: signin_redirect=https%3A%2F%2Fwww.jianshu.com%2F; path=/
header: Set-Cookie: read_mode=day; path=/
header: Set-Cookie: default_font=font2; path=/
header: Set-Cookie: locale=zh-CN; path=/
header: X-Request-Id: bc8f5200-e6b8-44f1-96b3-69603167956b
header: X-Runtime: 0.017585
header: Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
header: Content-Encoding: gzip

{'-content-encoding': 'gzip',
 'cache-control': 'max-age=0, private, must-revalidate',
 'connection': 'keep-alive',
 'content-length': '22385',
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
 'date': 'Mon, 27 Apr 2020 01:52:02 GMT',
 'etag': 'W/"d6b5630144393686a994679694f76474"',
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
 'x-request-id': 'bc8f5200-e6b8-44f1-96b3-69603167956b',
 'x-runtime': '0.017585',
 'x-xss-protection': '1; mode=block'}

22385

False
200
200
"""
