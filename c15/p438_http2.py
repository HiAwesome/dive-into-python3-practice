import urllib.request
from http.client import HTTPConnection

con = HTTPConnection('localhost')
con.set_debuglevel(0)
response = urllib.request.urlopen('https://weibo.com/')

"""
Nothing print.
"""
