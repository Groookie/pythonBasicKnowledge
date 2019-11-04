#!/usr/bin/python3
# -*-coding:utf-8-*-
# author: https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 数据类型 --- Tuple类型
# ====================================================

"""
## 通过观察结果发现：
1、tuple (元组) 使用小括号
2、list (列表)  使用中括号
3、set  (集合)  使用大括号
4、dict (字典)  使用大括号
   dict 也是无序的，只不过 dict 保存的是 key-value 键值对值，而 set 可以理解为只保存 key 值。
"""

# 另一种有序列表叫元组：tuple 。tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改。
# tuple 不可变是指当你创建了 tuple 时候，它就不能改变了，
# 也就是说它也没有 append()，insert() 这样的方法，但它也有获取某个索引值的方法，但是不能赋值。
# 那么为什么要有 tuple 呢？那是因为 tuple 是不可变的，所以代码更安全。
# 所以建议能用 tuple 代替 list 就尽量用 tuple 。

# 元组操作相关
t1 = 1, 2, 3, 4
print(t1)
print(type(t1))
print(t1[0], t1[1], t1[2], t1[3])

print("---------------------------1-----------------------------")
t2 = (1.1, 2, "abc")
print(t2)
print(type(t2))
print(t2[0], t2[1], t2[2])

print("---------------------------2-----------------------------")
t3 = 1
print(t3)
print(type(t3))

t4 = 2,
print(t4)
print(type(t4))

print("---------------------------4-----------------------------")
# 注意：元组是不可更改的, 如果每一个item是简单类型的话，那么值是不可以更改的，
# 但是如果是复杂类型，比如是list列表，那么列表不可以更改，但是列表中的元素不可以更改
# t2[2] = 3
# print(t2[2])
t5 = (1, 2, [3, 4])
print(t5)
print(type(t5))
t5[2][0] = "X"
t5[2][1] = "Y"
print(t5)
print(type(t5))

print("---------------------------5-----------------------------")
# 元组其他操作
list1 = [1, 2, 3]
t6 = (1, 2.0, "huangbo", list1)
t7 = (1, 2.0, "huangbo", list1)
print(len(t6))
print((1, 2, 3) + (4, 5, 6))
print(("huangbo",) * 4)
print("huangbo" in t6)

print("---------------------------6-----------------------------")
# 元组遍历
for x in t6:
    print(x)

print("---------------------------7-----------------------------")
# 元组高级技巧
p = 'huangbo', True, 30
print(type(p))
name = p[0]
gender = p[1]
age = p[2]
name1, gender1, age1 = p
print(name, gender, age)
print(name1, gender1, age1)
