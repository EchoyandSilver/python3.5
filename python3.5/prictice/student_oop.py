#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

'a test moudle'
__author__= 'Echoy'

import sys

class student(object):

	def __init__(self, name, score):
		self.name = name
		self.score = score

	def print_score(self):
		print('%s: %s' % (self.name, self.score))

xiaoA = student('xiaoA', 80)
xiaoB = student('xiaoB', 85)
xiaoA.print_score()
xiaoB.print_score()
