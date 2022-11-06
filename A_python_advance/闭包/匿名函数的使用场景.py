# 作为函数的参数使用
def func1(a, f):
    print('+++++++++>', a)
    r = f(a)
    print('=======>', r)


func1(8, lambda x: x ** 2)

'''
高阶函数：
一个函数的参数是另一个函数，高阶函数
系统的高阶函数：
sorted、min、max
filter类：用来过滤一个列表里符合规定的元素，得到的结果是一个迭代器
map类：将列表里的每一项数据都执行相同的操作，得到的结果是一个迭代器
reduce：对一个序列进行压缩运算，得到一个值。python3后，这个方法被移到了functools模块
'''
list = [('tom', 19), ('tony', 20), ('lily', 18), ('daniel', 21), ('rose', 22)]
m = max(list, key=lambda x: x[1])
print(m)