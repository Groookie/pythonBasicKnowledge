#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 数据类型相关
# ====================================================


"""
Python3 中有六个标准的数据类型：

    Number（数字）
        int 整形
        float 浮点型
        bool 布尔型
        complex 复数形式
    String（字符串）
    List（列表）
    Tuple（元组）
    Sets（集合）
    Dictionary（字典）

    type(a) 求出a变量的类型
    isinstance(a,b) 判断变量a是否是b类型， a变量的类型可以是b变量的子类的类型

    isinstance和type的区别:
        type()不会认为子类是一种父类类型,
        isinstance()会认为子类是一种父类类型
"""

# 声明数值类型
num_1 = 1
num_2 = 3.1415926
num_3 = True
num_4 = 3 + 4j
print(num_1, num_2, num_3, num_4)
print(type(num_1), type(num_2), type(num_3), type(num_4))

print("---------------------------1-------------------------------")
# 声明字符串类型
str_1 = "huangbo"
str_2 = 'a'
print(str_1, str_2)
print(type(str_1), type(str_2))
# 类型判断
print(isinstance(str_1, str))

print("---------------------------2-------------------------------")
# 声明列表list
list1 = [1, 2, 3, 4, "huangbo", True, 3 + 4j]
print(list1)
print(type(list1))

print("---------------------------3-------------------------------")
# 声明元组Tuple
tuple1 = (1, 2, 3, 4, "huangbo", 3 + 4j)
print(tuple1)
print(type(tuple1))

print("---------------------------4-------------------------------")
# 声明集合Set
set1 = {"a", 1, "b", 2, "c", 3, 3, 3, 3}
print(set1)
print(type(set1))

print("---------------------------5-------------------------------")
# 声明字典Dict
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
print(type(dict1))
