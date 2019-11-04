#!/usr/bin/python3
# -*-coding:utf-8-*-
# author: https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 流程控制 -- for相关
# 迭代相关 for循环可以遍历任何序列的项目，如一个列表或者一个字符串
# ====================================================

# range函数
print(range(10))
for a in range(10):
    print(a, end="\t")
print()

print("---------------------------1-----------------------------")
print(range(3, 10))
for a in range(3, 10):
    print(a, end="\t")
print()

print("---------------------------2-----------------------------")
print(range(3, 10, 2))
for a in range(3, 10, 2):
    print(a, end="\t")
print()

print("---------------------------3-----------------------------")
for a in range(10, 0, -2):
    print(a, end="\t")
print()

print("---------------------------4-----------------------------")
aa = ["huangbo", "xuzheng", "wangbaoqiang", 44]
# for 遍历列表：第一种，使用in进行遍历
for a in aa:
    print(a)
# for 遍历列表：第二种，使用下标进行遍历
for i in range(len(aa)):
    print(aa[i])

print("---------------------------5-----------------------------")
# 遍历字符串
for letter in "huangbo":
    print(letter, end="\t")
print()
