import httplib2

from file_path_collect import output_cache_path_dir as cache

httplib2.debuglevel = 1
h = httplib2.Http(cache)
# 网址换成简书
jianshu = 'https://www.jianshu.com/'

# 首先 cache 一遍
response0, content0 = h.request(jianshu)

response, content = h.request(jianshu)

print(len(content))
print()

print(response.status)
print()

print(response.fromcache)

"""
connect: (www.jianshu.com, 443)
send: b'GET / HTTP/1.1\r\nHost: www.jianshu.com\r\nuser-agent: Python-httplib2/0.17.3 (gzip)\r\naccept-encoding: gzip, deflate\r\nif-none-match: W/"bbd77e231f5e58fa82c8623683fdc1a1"\r\n\r\n'
reply: 'HTTP/1.1 304 Not Modified\r\n'
header: Server: Tengine
header: Date: Mon, 27 Apr 2020 01:37:58 GMT
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
header: X-Request-Id: c1a52d8f-b6c4-446b-837b-b4a54305db67
header: X-Runtime: 0.008544
header: Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
send: b'GET / HTTP/1.1\r\nHost: www.jianshu.com\r\nuser-agent: Python-httplib2/0.17.3 (gzip)\r\naccept-encoding: gzip, deflate\r\nif-none-match: W/"bbd77e231f5e58fa82c8623683fdc1a1"\r\n\r\n'
reply: 'HTTP/1.1 304 Not Modified\r\n'
header: Server: Tengine
header: Date: Mon, 27 Apr 2020 01:37:58 GMT
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
header: X-Request-Id: 81ad9b86-c492-4366-93d4-57f74d232969
header: X-Runtime: 0.005701
header: Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
23483

200

True
"""
