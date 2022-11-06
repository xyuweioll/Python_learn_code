# g = (3 * i for i in range(10))
#
# while True:
#     try:
#         e = next(g)
#         print(e)
#     except:
#         print('没有更多元素了！')
#         break
#
# # 定义生成器的方式二：借助函数实现
# # 只要函数中出现了yield关键字，说明函数就不是函数了，变成生成器了
#
# # 菲波那切数列
# '''
# 步骤：
# 1、定义一个函数，函数中使用yield函数
# 2、调用函数，接收调用的结果
# 3、得到的结果就是生成器
# 4、借助于next(),__next__()得到元素
# '''
#
#
# def func():
#     n = 0
#     while True:
#         n += 1
#         yield n
#
#
# g = func()
# print(next(g))
# print(g.__next__())


# 斐波那契
def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b              # return b+暂停
        a, b = b, a + b
        n += 1
    return '没有更多元素了'
g = fib(8)
print(next(g))
print(next(g))
print(next(g))
print(next(g))


