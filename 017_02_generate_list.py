#!/usr/bin/python3
# -*-coding:utf-8-*-
# author: https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 列表生成式
# ====================================================

import os
from random import randint

"""
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431779637539089fd627094a43a8a7c77e6102e3a811000
"""

list1 = []
for x in range(1, 10):
    list1.append(x)
print(list1)

print("\n", "---------------------------1-----------------------------")
# 以上操作太繁琐。如此操作
list2 = [x for x in range(1, 10)]
print(list2)

print("\n", "---------------------------2-----------------------------")
# 需求1： 求1-10的每个数的平方组成的列表
list3 = [x * x for x in range(1, 10)]
print(list3)

print("\n", "---------------------------3-----------------------------")
# 需求2： 求1-100中能被5除尽的数的平方组成的列表
list4 = [x * x for x in range(1, 30) if x % 5 == 0]
print(list4)

print("\n", "---------------------------4-----------------------------")
# 需求3： 两层循环嵌套
list5 = [m + n for m in 'ABC' for n in 'XYZ']
print(list5)

print("\n", "---------------------------5-----------------------------")
# 需求4： 列举出C盘下的所有文件
list6 = [d for d in os.listdir('c:/')]
print(list6)

print("\n", "---------------------------6-----------------------------")
# 需求5:  {'x': 'A', 'y': 'B', 'z': 'C' } 变成 ['y=B', 'x=A', 'z=C']
dict1 = {'x': 'A', 'y': 'B', 'z': 'C'}
list7 = [k + '=' + v for k, v in dict1.items()]
print(list7)

print("\n", "---------------------------7-----------------------------")
# 需求6： L = ['Hello', 'World', 18, 'Apple', None] 转小写
L = ['Hello', 'World', 18, 'Apple', None]
list8 = [x.lower() for x in L if isinstance(x, str)]
print(list8)

print("\n", "---------------------------8-----------------------------")
print([(x, y, x * y) for x in (0, 1, 2, 3) for y in (0, 1, 2, 3) if x < y])

print("\n", "---------------------------9-----------------------------")
# 根据value值进行删选
d = {x: randint(50, 100) for x in range(1, 21)}
print(d)
res = {s: c for s, c in d.items() if c >= 90}
print(res)
print(type(res))
