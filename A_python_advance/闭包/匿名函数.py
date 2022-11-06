'''
匿名函数：用lambda关键字能创建小型匿名函数。这种函数得名于省略了用def声明函数的标准步骤。
lambda函数的语法只包含一个语句，如下：
lambda函数的语法只包含一个语句，如下：
    lambda 参数列表:运算表达式
'''

def test(a):
    return a+1

r = lambda a:a+1

z = lambda x, y: x+y
result = z(1, 3)
print(result)