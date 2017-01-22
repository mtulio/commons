from urllib2 import urlopen as net_url_open

def getMyPublicIp():
    #List http://stackoverflow.com/questions/9481419/how-can-i-get-the-public-ip-using-python2-7
    default_pub_ip = '1.1.1.1'
    url_options = ['http://ip.42.pl/raw', 'http://ifconfig.me' ]

    for url in url_options:
        try:
            return net_url_open(url, timeout=5).read().decode('utf-8')
        except:
            continue
    return default_pub_ip
