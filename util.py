import binascii
import base64

def str2base64(data):
    d = data.replace(' ', '')#去空格
    s = binascii.unhexlify(d)#16进制转字符串
    r = base64.b64encode(s)#base64编码
    return r

def b64tostr(data):
    r = base64.b64decode(data)#base64解码
    s = binascii.hexlify(r)#字符串转16进制数
    return bytes.decode(s)#bytes转string
