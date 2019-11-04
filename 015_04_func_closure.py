#!/usr/bin/python3
# -*- coding:utf-8 -*-
# author: https://blog.csdn.net/zhongqi2513

# ====================================================
# 内容描述： 闭包
# 1、闭包无法修改外部函数的局部变量
# 2、闭包无法直接访问外部函数的局部变量
# ====================================================

# python中闭包从表现形式上看，如果在一个内部函数里，
# 对在外部作用域（但不是在全局作用域）的变量进行引用，那么内部函数就被认为是闭包(closure)。

"""
闭包：https://zhuanlan.zhihu.com/p/21346046
Closures are functions that refer to independent (free) variables (variables that are used locally, but defined in an enclosing scope). In other words, the function defined in the closure 'remembers' the environment in which it was created.
"""


def outer(x):
    def inner(y):
        result = x + 22
        return x + y

    return inner


result_f = outer(3)
print(type(result_f))
result = result_f(4)
print(result)

"""
结合这段简单的代码和定义来说明闭包： 
1、inner(y)就是这个内部函数，对在外部作用域（但不是在全局作用域）的变量进行引用：
x就是被引用的变量，x在外部作用域outer里面，但不在全局作用域里，则这个内部函数inner就是一个闭包。

2、再稍微讲究一点的解释是，闭包=函数块+定义函数时的环境，inner就是函数块，x就是环境，当然这个环境可以有很多，不止一个简单的x。

3、在函数outer中定义了一个inner函数，inner函数访问外部函数outer的（参数）变量，并且把inner函数作为返回值返回给outer函数。

作用：
1、用途1：当闭包执行完后，仍然能够保持住当前的运行环境。
2、用途2：闭包可以根据外部作用域的局部变量来得到不同的结果

"""
