#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from io import StringIO

# write to StringIO:
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

# read from StringIO
f = StringIO('诛仙,\n仙剑,\n问道,\n剑侠情缘。')
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
