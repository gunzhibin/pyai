#-*- coding:utf-8 -*-
# author:gunzhibin
# datetime:2018/6/6 14:30
# software: PyCharm Community Edition
L=['tu','ru','qu','wu','yu']
r=[]
n=3
for i in range(3):
    r.append(L[i])
print(r)

slice=L[0:3]
print(slice)

#倒数切片
bslice = L[-1]
print(bslice)
bslice1 = L[-3:-1]
print(bslice1)
bslice2 = L[-2:]
print(bslice2)

#创建数列
List1 = list(range(100))
slice1 = List1[:10]
print(slice1)
slice2 = List1[-10:]
print(slice2)
#第10个到第20个，步长为2
slice3 = List1[10:20:2]
print(slice3)
#所有数字每10个取一个
slice4 = List1[::10]
print(slice4)

#tuple型list
tuple = (1,2,3,4,5,6,7,8,9,10)
print(tuple)
tslice = tuple[:3]
print(tslice)

#字符串当list，也可用切片操作
str = '我是打不死的小强'
s1 = str[2:5]
print(s1)
#取步长为3的所有字符
s2 = str[::3]
print(s2)
