'''
装饰器修饰有返回值的函数
'''


def decorator(func):
    def wrapper(*args, **kwargs):
        r = func(*args, **kwargs)
        print(f'预计装修费用是:{r}元')
        print('刷漆')
        print('铺地板')
        print('买家具')
        print('精装修房子')
        return r

    return wrapper

@decorator
def house():
    print('我是一个毛坯房')
    return 50000


r = house()  # house就是wrapper
print(r)
