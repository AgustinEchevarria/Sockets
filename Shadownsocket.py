import socket, ssl 
def GeneratePost(data,host,uri,content_type='',user_agent='',cookie='',others=''):
    content_length = len(data)
    if content_type == '':
        content_type = 'application/x-www-form-urlencoded;charset=UTF-8'
    if user_agent == '':
        user_agent = '''Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'''
    datas = str('POST {} HTTP/1.1\r\nHost: {}\r\nUser-Agent: {}\r\nConnection: Keep-Alive\r\nAccept: */*\r\nContent-type: {}\r\nContent-length: {}\r\nCookie: {}\r\n').format(uri,host,user_agent,content_type,content_length,cookie)
    if others != '':
        datas = datas + others + '\r\n'
    datas = datas + '\r\n' + data
    return datas

def SearchIp(hostname):
    return socket.gethostbyname(hostname)

def CreateTcpIpv4Sock(ip,port,adrr='127.0.0.1',t=10,portr=8080):
    soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if adrr != '127.0.0.1':
        adr = True
        while adr == True:
            try:
                soc.bind((adrr,portr))
                adr = False
                break
            except OSError:
                portr += + 1
                continue
    soc.settimeout(int(t))
    soc.connect((ip,port))
    return soc

def Cifrate(soc,host):
    context = ssl._create_unverified_context()
    soc = context.wrap_socket(soc,server_hostname=str(host))
    return soc

def Showdatarecived():
    x = open('recivedcache.rslt','r').read()
    print(x)
    
def SandRData(datas,_socketname_,time=3):
    cache = open('recivedcache.rslt','wb')
    dtrlist = []
    print('sending')
    try:    
        _socketname_.settimeout(time)
        _socketname_.send(datas.encode())
        connection = True
    except:
        connection = False
    while connection:
        try: 
            _socketname_.settimeout(time)
            dtr = _socketname_.recv(65000)
            if len(dtr) > 2:
                connection = True
            if len(dtr) < 2:
                connection = False
                break
            dtrlist.append(dtr)
        except socket.timeout:
            connection = False
            print('Socket Timeout')
            break
        except:
            print('ERROR')
            connection = False
            break
    for i in dtrlist:
        cache = open('recivedcache.rslt','ab')
        cache.write(i)
    o = b''
    for i in range(0,len(dtrlist)):
        o = o + dtrlist[i]
    return o
def HttpRequests(host,location='/',cookie='',others=''):#others='\r\nExample-Header: Key'
    version = 'HTTP/1.1'
    useragent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537 Chrome/91.0.4472.11 Safari/537.36'
    datas = str('GET' + ' ' + location + ' ' + version + '\r\nHost: ' + host + '\r\nUser-Agent: ' + useragent + '\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nConnection: Keep-Alive\r\n')
    if others != '':
        datas = datas + '{}\r\n'.format(others)
    if cookie != '':
        datas = datas + 'Cookie: {}\r\n'.format(cookie)
    datas = datas + '\r\n'
    return datas
