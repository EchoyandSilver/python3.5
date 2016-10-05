#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('	size	Last Modified	Name')
print('-----------------------------')

for f in os.listdir(pwd):
	fsize = os.path.getsize(f)
	mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
	flag = '/' if os.path.isdir(f) else''
	print('%10d %s %s%s' % (fsize, mtime, f, flag))
