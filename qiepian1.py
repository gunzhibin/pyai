#-*- coding:utf-8 -*-
# author:gunzhibin
# datetime:2018/6/6 15:15
# software: PyCharm Community Edition
#使用切片、递归实现去除字符串首尾空格
def trim(x):
    if len(x)==0:
        return x
    elif x[0]==' ':
        return trim(x[1:])
    elif x[-1]==' ':
        return trim(x[:-1])
    return x

print(trim('  拉屎的会计师  '))