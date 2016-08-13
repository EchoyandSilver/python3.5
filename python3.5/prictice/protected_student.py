#!/usr/bin/env	python3
# _*_ coding: utf-8 _*-

class Student(object):
	
	def __init__(self, name, score):
		self.__name = name
		self.__score = score

	def get_name(self):
		return self.__name
	
	def get_score(self):
		return self.__score

	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'

xiaoA = Student('xiaoA', 59)
print('xiaoA.get_nam()=' , xiaoA.get_name())
xiaoA.set_score(68)
print('xiaoA.get_score()=' , xiaoA.get_score())
xiaoA.get_grade()

print('DO NOT use xiaoA._Student__name:' , xiaoA._Student__name)
