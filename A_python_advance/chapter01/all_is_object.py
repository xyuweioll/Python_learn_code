# 2.1一切皆为对象
# python中类和函数也是对象，属于python的一等公民，具体现在：
# 1.可以赋值给一个变量
def ask(name="bobby1"):
    print(name)
my_func = ask  # 函数赋值给变量
my_func("weixianyu")


class Person:
    def __init__(self):
        print("bobby2")
my_class = Person
my_class()

# 2.可以添加到集合对象中
obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())
# 3.可以作为参数传递给函数
# 4.可以当作函数的返回值
def decorator_func():
    print("dec start")
    return ask

my_ask = decorator_func()  # 一个函数的返回值是另一个函数，是python装饰器实现的原理
my_ask("tom")
