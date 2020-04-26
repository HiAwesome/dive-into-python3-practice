import urllib.request
from pprint import pprint

a_url = 'https://weibo.com/'
data = urllib.request.urlopen(a_url).read()

print(type(data))
pprint(data)

"""
<class 'bytes'>
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
 b'(c) {\n                        c()\n                    }\n                '
 b'};\n                s.src = u;\n                document.getElementsByTagN'
 b'ame("head")[0].appendChild(s)\n            } catch (e) {\n            }\n  '
 b'      };\n    }).call(url);\n\n    // \xc1\xf7\xb3\xcc\xc8\xeb\xbf\xda\xa1'
 b'\xa3\n    wload(function () {\n\n        try {\n\n            var need_resto'
 b're = "1" == "1"; // \xca\xc7\xb7\xf1\xd7\xdf\xbb\xd6\xb8\xb4\xc9\xed'
 b'\xb7\xdd\xc1\xf7\xb3\xcc\xa1\xa3\n\n            // \xc8\xe7\xb9'
 b'\xfb\xd0\xe8\xd2\xaa\xd7\xdf\xbb\xd6\xb8\xb4\xc9\xed\xb7\xdd\xc1'
 b'\xf7\xb3\xcc\xa3\xac\xb3\xa2\xca\xd4\xb4\xd3 cookie \xbb\xf1\xc8\xa1\xd3'
 b'\xc3\xbb\xa7\xc9\xed\xb7\xdd\xa1\xa3\n            if (!need_restore || !Stor'
 b'e.CookieHelper.get("SRF")) {\n\n                // \xc8\xf4\xbb'
 b'\xf1\xc8\xa1\xca\xa7\xb0\xdc\xd7\xdf\xb4\xb4\xbd\xa8\xb7\xc3\xbf'
 b'\xcd\xc1\xf7\xb3\xcc\xa1\xa3\n                // \xc1\xf7\xb3\xcc\xd6'
 b'\xb4\xd0\xd0\xca\xb1\xbc\xe4\xb9\xfd\xb3\xa4\xa3\xa8\xb3\xac\xb9\xfd 3s'
 b'\xa3\xa9\xa3\xac\xd4\xf2\xc8\xcf\xce\xaa\xb3\xf6\xb4\xed\xa1\xa3\n       '
 b'         var error_timeout = window.setTimeout("error_back()", 5000);\n\n '
 b'               tid.get(function (tid, where, confidence) {\n             '
 b'       // \xc8\xa1\xd6\xb8\xce\xc6\xcb\xb3\xc0\xfb\xcd\xea\xb3\xc9'
 b'\xa3\xac\xc7\xe5\xb3\xfd\xb3\xf6\xb4\xed timeout \xa1\xa3\n              '
 b'      window.clearTimeout(error_timeout);\n                    incarnate('
 b'tid, where, confidence);\n                });\n            } else {\n      '
 b'          // \xd3\xc3\xbb\xa7\xc9\xed\xb7\xdd\xb4\xe6\xd4\xda\xa3\xac\xb3'
 b'\xa2\xca\xd4\xbb\xd6\xb8\xb4\xd3\xc3\xbb\xa7\xc9\xed\xb7\xdd\xa1\xa3\n      '
 b'          restore();\n            }\n        } catch (e) {\n            // '
 b'\xb3\xf6\xb4\xed\xa1\xa3\n            error_back();\n        }\n    });\n\n'
 b'    // \xa1\xb0\xb7\xb5\xbb\xd8\xa1\xb1 \xbb\xd8\xb5\xf7\xba\xaf\xca\xfd'
 b'\xa1\xa3\n    var return_back = function (response) {\n\n        if (resp'
 b'onse["retcode"] == 20000000) {\n            back();\n        } else {\n    '
 b'        // \xb3\xf6\xb4\xed\xa1\xa3\n            error_back(response["msg"]'
 b');\n        }\n    };\n\n    // \xcc\xf8\xd7\xaa\xbb\xd8\xb3\xf5'
 b'\xca\xbc\xb5\xd8\xd6\xb7\xa1\xa3\n    var back = function() {\n\n        va'
 b'r url = "https://weibo.com/";\n        if (url != "none") {\n            w'
 b'indow.location.href = url;\n        }\n    };\n\n    // \xbf\xe7\xd3\xf2'
 b'\xb9\xe3\xb2\xa5\xa1\xa3\n    var cross_domain = function (response) {\n'
 b'\n        var from = "weibo";\n        if (response["retcode"] == 20000000'
 b') {\n\n            var crossdomain_host = "login.sina.com.cn";\n           '
 b' if (crossdomain_host != "none") {\n\n                var cross_domain_int'
 b'r = window.location.protocol + "//" + crossdomain_host + "/visitor/visitor?a'
 b'=crossdomain&cb=return_back&s=" +\n                        encodeURICompo'
 b'nent(response["data"]["sub"]) + "&sp=" + encodeURIComponent(response["data"]'
 b'["subp"]) + "&from=" + from + "&_rand=" + Math.random();\n               '
 b' url.l(cross_domain_intr);\n            } else {\n\n                back();'
 b'\n            }\n        } else {\n\n            // \xb3\xf6\xb4\xed'
 b'\xa1\xa3\n            error_back(response["msg"]);\n        }\n    };\n\n  '
 b'  // \xce\xaa\xd3\xc3\xbb\xa7\xb8\xb3\xd3\xe8\xb7\xc3\xbf\xcd\xc9'
 b'\xed\xb7\xdd \xa1\xa3\n    var incarnate = function (tid, where, conficence)'
 b' {\n\n        var gen_conf = "";\n        var from = "weibo";\n        var i'
 b'ncarnate_intr = window.location.protocol + "//" + window.location.host + "/v'
 b'isitor/visitor?a=incarnate&t=" +\n                encodeURIComponent(tid)'
 b' + "&w=" + encodeURIComponent(where) + "&c=" + encodeURIComponent(conficence'
 b') +\n                "&gc=" + encodeURIComponent(gen_conf) + "&cb=cross_d'
 b'omain&from=" + from + "&_rand=" + Math.random();\n        url.l(incarnate'
 b'_intr);\n    };\n\n    // \xbb\xd6\xb8\xb4\xd3\xc3\xbb\xa7\xb6'
 b'\xaa\xca\xa7\xb5\xc4\xc9\xed\xb7\xdd\xa1\xa3\n    var restore = function ('
 b') {\n\n        var from = "weibo";\n        var restore_intr = window.locat'
 b'ion.protocol + "//" + window.location.host +\n                "/visitor/v'
 b'isitor?a=restore&cb=restore_back&from=" + from + "&_rand=" + Math.random'
 b'();\n\n        url.l(restore_intr);\n    };\n\n    // \xbf\xe7\xd3'
 b'\xf2\xbb\xd6\xb8\xb4\xb6\xaa\xca\xa7\xb5\xc4\xc9\xed\xb7\xdd\xa1\xa3\n    va'
 b'r restore_back = function (response) {\n\n        // \xc9\xed\xb7\xdd\xbb'
 b'\xd6\xb8\xb4\xb3\xc9\xb9\xa6\xd7\xdf\xb9\xe3\xb2\xa5\xc1\xf7\xb3'
 b'\xcc\xa3\xac\xb7\xf1\xd4\xf2\xd7\xdf\xb4\xb4\xbd\xa8\xb7\xc3\xbf'
 b'\xcd\xc1\xf7\xb3\xcc\xa1\xa3\n        if (response["retcode"] == 20000000)'
 b' {\n\n            var url = "https://weibo.com/";\n            var alt = re'
 b'sponse["data"]["alt"];\n            var savestate = response["data"]["sav'
 b'estate"];\n            if (alt != "") {\n                requrl = (url == '
 b'"none") ? "" : "&url=" + encodeURIComponent(url);\n                var pa'
 b'rams = "entry=sso&alt=" + encodeURIComponent(alt) + "&returntype=META" +'
 b'\n                    "&gateway=1&savestate=" + encodeURIComponent(savest'
 b'ate) + requrl;\n                window.location.href = "https://login.sin'
 b'a.com.cn/sso/login.php?" + params;\n            } else {\n\n               '
 b" cross_domain(response);\n            }\n        } else if(response['retco"
 b"de'] == 50111261 && isInIframe()) {\n            //do nothing\n        } e"
 b'lse {\n\n            tid.get(function (tid, where, confidence) {\n         '
 b'       incarnate(tid, where, confidence);\n            });\n        }\n    '
 b'};\n\n    // \xb3\xf6\xb4\xed\xc7\xe9\xbf\xf6\xb7\xb5\xbb\xd8\xb5'
 b'\xc7\xc2\xbc\xd2\xb3\xa1\xa3\n    var error_back = function (msg) {\n\n     '
 b'   var url = "https://weibo.com/";\n        var clientType = "pc";\n      '
 b'  if (url != "none") {\n\n            if (url.indexOf("ssovie4c55=0") === '
 b'-1) {\n                url += (((url.indexOf("?") === -1) ? "?" : "&") + '
 b'"ssovie4c55=0");\n            }\n            if (clientType == "mobile") {'
 b'\n            \twindow.location.href = "https://passport.weibo.cn/signin/l'
 b'ogin?r="+url;\n            } else{\n            \twindow.location.href = "h'
 b'ttp://weibo.com/login.php";\n            }\n        } else {\n\n            '
 b'if(document.getElementById("message")) {\n                document.getEle'
 b'mentById("message").innerHTML = "Error occurred" + (msg ? (": " + msg) : "."'
 b');\n            }\n        }\n    };\n\n    var isInIframe = function () '
 b'{\n        try {\n            return window.self !== window.top;\n        }'
 b' catch (e) {\n            return true;\n        }\n    };\n\n</script>\n</'
 b'body>\n</html>')
"""
