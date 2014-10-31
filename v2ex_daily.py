#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import urllib2

# copy your v2ex cookies here after login
V2EX_COOKIE = ''

V2EX_URL_START = r'https://v2ex.com'
V2EX_MISSION = V2EX_URL_START + r'/mission/daily'
V2EX_COIN_URL = r'/mission/daily/redeem?once='

def get_once_url(data):
    p = '/mission/daily/redeem\?once=\d+'
    m = re.search(p, data)
    if m:
        return m.group()
    else:
        return None
        
if __name__ == '__main__':
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0'),
                         ('Cookie', V2EX_COOKIE)]
    
    data = opener.open(V2EX_MISSION).read()
    once = get_once_url(data)
    if None == once:
        print '"once" not found, maybe you already got coins'
        sys.exit(-1)
    
    v2ex_coin_url = V2EX_URL_START + once
    print v2ex_coin_url

    opener.open(v2ex_coin_url).read()
