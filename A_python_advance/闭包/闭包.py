# 闭包
'''
嵌套：
闭包：
函数只是一段可执行代码，编译后就“固化”了，每个函数在内存中只有一份实例，得到函数的入口便可以
执行函数了。函数还可以嵌套定义，即在一个函数内部可以定义另一个函数，有了嵌套函数这种结构，便会
产生闭包问题。
'''

# # 在函数里面话可以定义函数，可以嵌套多层，执行需要被调用
# def outer():
#     a = 100
#
#     def inner():
#         nonlocal a  # 表示引用局部变量外部的变量
#         b = 200
#         a += b  # 内部函数不能修改外部函数的变量，若需要修改则需要在内部函数中添加：nonlocal
#         print('我是内部函数', b)
#
#     result = locals()  # locals() 表示查看函数中的局部变量，以字典的形式返回
#     print(result)


# 变量查找顺序：内层函数-》外层函数-》全局-》系统 builfins
# a = 100
#
#
# def outer():
#     a = 200
#
#     def inner():
#         a = 300
#         print('内部函数', a)
#         a -= 50
#
#     print(a)
#     inner()
#
#
# outer()
# print(a)

'''
闭包：
1.嵌套函数
2.内部函数引用了外部函数的变量
3.返回值是内部函数
'''


def outer(n):
    a = 10

    def inner():
        b = a + n
        print('内部函数：', b)

    return inner


r = outer(5)
print(r)
r()  # 调用r


print(globals())  # globals()  查看全局变量