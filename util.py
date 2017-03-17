def str2base64(data):
    d = data.replace(' ', '')
    s = binascii.unhexlify(d)
    r = base64.b64encode(s)
    print(r)
