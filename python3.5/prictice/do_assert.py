#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

def foo(s):
	n = int(s)
	assert n != 0, 'n is zero!'

def main():
	foo('0')

main()
