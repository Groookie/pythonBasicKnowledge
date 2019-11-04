#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 变量定义相关
# ====================================================


# 定义变量，不用声明类型， python是一种动态语言。具有类型推断功能， 能自动识别出aa变量是字符串类型
aa = "huangbo"
aa = 11

# 自动识别 bb变量 为  数值类型
bb = 11

# python的优良特性，可以在一行声明多个变量
cc, dd = "xuzheng", 22
print(cc, dd)

# 实现cc和dd变量的交换
cc, dd = dd, cc
print(cc, dd)

# 连环声明
ee = ff = gg = hh = 12
print("-----------------------------------------------------------------------")

# 声明list
list1 = [1, 2, 3, 4, "huangbo", True]
print(list1)
print(type(list1))

# 声明元组
tuple1 = (1, 2, 3, 4, "huangbo")
print(tuple1)
print(type(tuple1))

# 声明集合
set1 = {"a", 1, "b", 2, "c", 3, 3, 3}
print(set1)
print(type(set1))

# 声明字典
dict1 = {"a": 1, "b": 2, "c": 3}
print(dict1)
print(type(dict1))

print("-----------------------------------------------------------------------")
p = 'huangbo', True, 30
print(type(p))
name = p[0]
gender = p[1]
age = p[2]
name1, gender1, age1 = p
print(name, gender, age)
print(name1, gender1, age1)

print("-----------------------------------------------------------------------")
num_list = [100, 19, 20, 98]
first, *left_num_list, last = num_list
print(first, left_num_list, last)
