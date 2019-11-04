#!/usr/bin/python3
# -*-coding:utf-8-*-
# author: https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 数据类型 --- List类型
# ====================================================

import copy

# Python 内置的一种数据类型是列表：list。 list 是一种有序的集合，可以随时添加和删除其中的元素。
# 创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可，且列表的数据项不需要具有相同的类型


print("---------------------------8-----------------------------")
# list的其他函数
list1 = [3, 4, 5, 6, 7, 6, 6]
# len(list)	列表元素个数
print(len(list1))
# max(list)	返回列表元素最大值
print(max(list1))
# min(list)	返回列表元素最小值
print(min(list1))
# list(seq)	将元组转换为列表
print(list(range(1, 10)))
# list.count(obj)	统计某个元素在列表中出现的次数
print(list1.count(6))
print(list1.count(1))
# list.index(obj)	从列表中找出某个值第一个匹配项的索引位置
print(list1.index(4))
# list.append(obj)	在列表末尾添加新的对象
list1.append(44)
print(list1)

print("---------------------------9-----------------------------")
# list.insert(index, obj)	将对象插入列表
list1.insert(1, 1111)
print(list1)
# list.pop(obj=list[-1])	移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(list1.pop())
print(list1)
print(list1.pop(1))
print(list1)
# list.reverse()	反向列表中元素
list1.reverse()
print(list1)
# list.sort([func])	对原列表进行排序
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)

print("---------------------------10-----------------------------")
# list反转
list_name = ["huangbo", "xuzheng", "wangbaoqiang"]
print(list_name[::-1])
# 同样，也可以反转字符串
print("huangbo"[::-1])

print("---------------------------11-----------------------------")
# 深拷贝， 浅拷贝
list_a = [1, 2, [3, 4]]
list_b = copy.copy(list_a)      # 浅拷贝
list_c = copy.deepcopy(list_a)  # 深拷贝
list_a[2][1] = 5
print(list_a)       # 原始列表
print(list_b)       # 浅拷贝列表
print(list_c)       # 深拷贝列表
