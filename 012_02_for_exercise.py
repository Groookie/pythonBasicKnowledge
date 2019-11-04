#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: 马中华 https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 
# ====================================================

# 条件语句和循环语句综合实例

# 打印99乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
        print("{0}*{1}={2}\t".format(i, j, i * j), end="")
    print()

print("---------------------------1-----------------------------")
# 一句话打印99乘法表
print('\n'.join([' '.join(['%s*%s=%-3s' % (y, x, x * y) for y in range(1, x + 1)]) for x in range(1, 10)]))

print("---------------------------2-----------------------------")
# 带索引位置的循环遍历
colors = ['red', 'green', 'blue', 'yellow']
for i, color in enumerate(colors):
    print(i, 'mapping', color)

print("---------------------------3-----------------------------")
# 强大的for循环
student = [['Tom', (98, 96, 100)], ['Jack', (98, 96, 100)]]
for name, (first, second, third) in student:
    print(name, first, second, third)

print("---------------------------4-----------------------------")
# 判断是否是 闰年
year = int(input("请输入一个年份: "))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0} 是闰年'.format(year))
else:
    print('{0} 不是闰年'.format(year))
