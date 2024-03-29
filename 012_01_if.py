#!/usr/bin/python3
# -*-coding:utf-8-*-
# author: https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 流程控制--if相关
# ====================================================

"""
Python 条件语句跟其他语言基本一致的，都是通过一条或多条语句的执行结果（ True 或者 False ）来决定执行的代码块。
Python 程序语言指定任何非 0 和非空（null）值（非零数值、非空字符串、非空 list）为 True，0 或者 null为 False。

Python中if的基本语法为：

    if 判断条件1:
        执行语句1……
    elif 判断条件2:
        执行语句2……
    elif 判断条件3:
        执行语句3……
    else:
        执行语句4……

Python 语言有着严格的缩进要求，因此这里也需要注意缩进，也不要少写了冒号":"
if 语句的判断条件可以用>（大于）、<(小于)、==（等于）、>=（大于等于）、<=（小于等于）来表示其关系。
"""

# 第一个例子： 一个分支
value = 55
if value >= 60:
    print("及格")
else:
    print("不及格")

print("---------------------------1-----------------------------")
if value:
    print("不是0分")

value = 0
if value:
    print("不是0分")
else:
    print("是0分")

print("---------------------------2-----------------------------")
# 第二个例子： 多个分支
score = 99
if score > 90:
    print('优秀')
elif score > 80:
    print('良好')
elif score > 60:
    print('及格')
else:
    print('不及格')

print("---------------------------3-----------------------------")
# 多个判断条件
java = 86
python = 68
if java > 80 and python > 80:
    print('优秀')
else:
    print('不优秀')

if ((java >= 80) and java < 90) or ((python >= 80) and python < 90):
    print('良好')

print("---------------------------4-----------------------------")
x = [True, True, False]
if any(x):
    print("At least one True")
if all(x):
    print("Not one False")
if any(x) and not all(x):
    print("At least one True and one False")
