# 可迭代的对象：1、生成器  2、元组  列表  集合  字典  字符串
# 如何判断一个对象是否是可迭代的？
from collections.abc import Iterable

list1 = [1, 2, 3, 4, 5]
f = isinstance(list1, Iterable)
print(f)

f = isinstance('abc', Iterable)
print(f)

g = (x + 1 for x in range(10))

f = isinstance(g, Iterable)
print(f)

# 迭代器
'''
迭代是访问集合元素的一种方式。迭代器是一个可以记住遍历的位置的对象
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
迭代器只能往前不会后退。
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可迭代的 是不是肯定就是 迭代器？
生成器是可迭代的，也是迭代器
list是可迭代的，但不是迭代器

list--->迭代器
list--->iter(list)--->迭代器 next()
'''
list1 = [1, 2, 3, 4, 5]
list1 = iter(list1)    # 仍入可迭代的对象，返回迭代器
print(next(list1))  # 列表对象不是迭代器

'''
生成器与迭代器：


'''