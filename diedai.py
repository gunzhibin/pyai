#-*- coding:utf-8 -*-
# author:gunzhibin
# datetime:2018/6/7 10:49
# software: PyCharm Community Edition
from collections import Iterable
def diedai():
    d = {'a':1,'b':2,'c':3,'d':4,'e':5}
    L = ('e','r','t')
    #判断一个操作对象是否可以迭代
    print(isinstance(d,Iterable))
    for key in d:
        print(key)
    for value in d.values():
        print(value)
    for k,v in d.items():
        print(k+'='+str(v))
    for k,v in enumerate(L):
        print(k,v)
diedai()