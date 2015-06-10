# -*- coding:utf8 -*-

import urllib2
import urllib

def post(url, data, header = {}):
    request = urllib2.Request(url)
    for k,v in header.items():
        request.add_header(k, v)

    f = urllib2.urlopen(
        request,
        data = urllib.urlencode(data))

    return f.read()

def get(url, header = {}):
    request = urllib2.Request(url)
    for k,v in header.items():
        request.add_header(k, v)

    f = urllib2.urlopen(request)

    return f.read()
