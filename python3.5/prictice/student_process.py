#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'a test moudle'
__author__= 'Echoy'

std1 = {'name': 'XiaoA', 'score': 98}
std2 = {'name': 'XiaoB', 'score': 90}

def print_score(std):
	print('%s: %s' % (std['name'], std['score']))

xiaoA = print_score(std1)
print(xiaoA)
xiaoB = print_score(std2)
print(xiaoB)
