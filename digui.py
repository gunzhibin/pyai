#-*- coding:utf-8 -*-
# author:gunzhibin
# datetime:2018/6/6 11:13
# software: PyCharm Community Edition
def digui(x):
    return filter(x,1)

def filter(n,num):
    if n==1:
        return num
    return filter(n-1,num*n)

print(digui(100))
