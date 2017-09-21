import hashlib


def md5(value):
    m = hashlib.md5()
    m.update(value)
    pwd = m.hexdigest()
    return pwd

if __name__ == '__main__':
    a = md5(b'123456')
    print(a)
