#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import pickle

d = dict(name='Bob', age=20, score=88)
date = pickle.dumps(d)
print(date)

reborn = pickle.loads(date)
print(reborn)
