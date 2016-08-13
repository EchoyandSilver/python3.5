#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

class Student(object):
	__slots__ = ('name','age') #用tuple定义容许绑定的属性

class GraduateStudent(Student):
	pass

s = Student() #创建新的实例
s.name = 'Michael' #绑定属性‘name’
s.age = 25 #绑定属性‘name’
#ERROR:AttributeError:'Student' object has no attribute 'score'
try:
	s.score = 99
except AttributeError as e:
	print('AttributeError', e)

g = GraduateStudent()
g.score = 99
print('g.score = ', g.score)
