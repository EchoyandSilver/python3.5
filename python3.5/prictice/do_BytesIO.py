#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from io import BytesIO

# write to BytesIO

f = BytesIO()
f.write(b'hello')
f.write(b' ')
f.write(b'world!')
print(f.getvalue())

# read from BytesIO
data = '诛仙，仙剑，问道，剑侠情缘'.encode('utf-8')
f = BytesIO(data)
print(f.read())
