#!/usr/bin/python3
# -*-coding:utf-8-*-
# author: https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 生成器相关
# ====================================================

"""
通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。
第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator

https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000
"""

# 列表生成式
L = [x * x for x in range(10)]
# 生成器
g = (x * x for x in range(10))
print(L)
print(g)
print(type(L), type(g))

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("-------------------1---------------------------------------------------")
"""
generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象
"""
for num in g:
    print(num)

print("-------------------2--------------------------------------------------")


# 利用列表生成式求 斐波那契 数列


def fibonacci(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1


fibonacci(10)
