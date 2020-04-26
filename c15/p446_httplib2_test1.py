from pprint import pprint

import httplib2

from file_path_collect import output_cache_path_dir as cache

h = httplib2.Http(cache)
weibo = 'https://weibo.com/'
response, content = h.request(weibo)

print(response.status)
print()

pprint(content[:1000])
print()

print(len(content))
print()

# 第二遍，所有的内容和上次一样
response2, content2 = h.request(weibo)

print(response2.status)
print()

pprint(content2[:1000])
print()

print(len(content2))

"""
200

(b'<!DOCTYPE html>\n<html>\n<head>\n    <meta http-equiv="Content-type" conten'
 b't="text/html; charset=gb2312"/>\n    <title>Sina Visitor System</title>\n<'
 b'/head>\n<body>\n<span id="message"></span>\n<script type="text/javascript" '
 b'src="/js/visitor/mini_original.js?v=20161116"></script>\n<script type="te'
 b'xt/javascript">\n    window.use_fp = "1" == "1"; // \xca\xc7\xb7\xf1\xb2'
 b'\xc9\xbc\xaf\xc9\xe8\xb1\xb8\xd6\xb8\xce\xc6\xa1\xa3\n    var url = url || {'
 b'};\n    (function () {\n        this.l = function (u, c) {\n            try'
 b' {\n                var s = document.createElement("script");\n           '
 b'     s.type = "text/javascript";\n                s[document.all ? "onrea'
 b'dystatechange" : "onload"] = function () {\n\n                    if (docu'
 b'ment.all && this.readyState != "loaded" && this.readyState != "complete"'
 b') {\n                        return\n                    }\n               '
 b'     this[document.all ? "onreadystatechange" : "onload"] = null;\n      '
 b'              this.parentNode.removeChild(this);\n                    if '
 b'(c) {\n                        c()\n          ')

6117

200

(b'<!DOCTYPE html>\n<html>\n<head>\n    <meta http-equiv="Content-type" conten'
 b't="text/html; charset=gb2312"/>\n    <title>Sina Visitor System</title>\n<'
 b'/head>\n<body>\n<span id="message"></span>\n<script type="text/javascript" '
 b'src="/js/visitor/mini_original.js?v=20161116"></script>\n<script type="te'
 b'xt/javascript">\n    window.use_fp = "1" == "1"; // \xca\xc7\xb7\xf1\xb2'
 b'\xc9\xbc\xaf\xc9\xe8\xb1\xb8\xd6\xb8\xce\xc6\xa1\xa3\n    var url = url || {'
 b'};\n    (function () {\n        this.l = function (u, c) {\n            try'
 b' {\n                var s = document.createElement("script");\n           '
 b'     s.type = "text/javascript";\n                s[document.all ? "onrea'
 b'dystatechange" : "onload"] = function () {\n\n                    if (docu'
 b'ment.all && this.readyState != "loaded" && this.readyState != "complete"'
 b') {\n                        return\n                    }\n               '
 b'     this[document.all ? "onreadystatechange" : "onload"] = null;\n      '
 b'              this.parentNode.removeChild(this);\n                    if '
 b'(c) {\n                        c()\n          ')

6117
"""
