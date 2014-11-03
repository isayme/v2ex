import sys
import urllib2
import md5
import json

# get v2ex registered user count
def get_user_count():
    try:
        resp = urllib2.urlopen('http://www.v2ex.com/api/site/stats.json')
    except urllib2.URLError, e:
        return -1

    data = resp.read()
    jrel = json.loads(data)
    
    return jrel['member_max']

# get avatar
def get_user_avatar(user_id):
    m = md5.new(str(user_id))
    m.digest()
    md5_val = m.hexdigest()
    jpgurl = 'http://cdn.v2ex.com/avatar/' \
            + md5_val[0:4] + '/' \
            + md5_val[4:8] + '/' \
            + str(user_id) + '_large.png'

    localjpg = str(user_id) + '.png'

    try:
        resp = urllib2.urlopen(jpgurl)
    except urllib2.URLError, e:
        print jpgurl, '[', e.code, '] => ', localjpg
        return jpgurl

    data = resp.read()
    with open(localjpg, 'wb') as code:
        code.write(data)

    print jpgurl, ' => ', localjpg
    return jpgurl

if __name__ == '__main__':
    v2ex_user_count = get_user_count()
    if -1 == v2ex_user_count:
        print 'get v2ex user count error.'
        sys.exit(-1)
        
    print 'total registered user number of v2ex is :', v2ex_user_count

    for i in range(1, v2ex_user_count + 1):
        get_user_avatar(i)   
