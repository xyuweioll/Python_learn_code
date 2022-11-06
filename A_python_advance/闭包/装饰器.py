# 装饰器
'''

'''

# def foo():
#     print('foo')
#
#
# def func():
#     print('func')
#
#
# # foo()
# foo = func()
# foo()


'''
装饰器：
遵循开放封闭原则，在不改变原函数的情况下扩展了函数的功能
'''


# 定义一个装饰器 (带参数)
# 如果被装饰的函数有参数则装饰器内部函数也要有参数
def decorater(func):
    def wrapper(*args, **kwargs):  # 可变参数，args是一个元组,kwargs关键字参数
        func(*args, **kwargs)
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')

    return wrapper


@decorater
def house(address):
    print('毛坯房...')
    print("地址:", address)


@decorater
def changfang(address, area):
    print('房子的的地址是：', address, "面积是：", area)


house('北京四合院')
changfang('123', 1000)



