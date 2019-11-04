#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 马中华 https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 切片
# ====================================================

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素
# 第一种方式
result_l1 = [L[0], L[1], L[2]]
print(result_l1)

# 第二种方式
result_l2 = []
for i in range(3):
    result_l2.append(L[i])
print(result_l2)

# 第三种方式
result_l3 = [L[item] for item in range(3)]
print(result_l3)

# 第四种方式：正数取法
result_l4 = L[0:3]
print(result_l4)

# 第五种方式：倒数取法
result_l5 = L[-len(L):3-len(L)]
print(result_l5)

