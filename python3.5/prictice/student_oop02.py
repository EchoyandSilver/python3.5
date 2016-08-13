#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'a  Student  moudle'
__author__= 'Echoy'

class Student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s : %d - %s' % (self.name, self.score, self.get_grade()))

	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

xiaoA = Student('xiaoA' , 95)
xiaoB = Student('xiaoB' , 65)
xiaoC = Student('xiaoC' , 55)

xiaoA.print_score()
xiaoB.print_score()
xiaoC.print_score()


