#返回值就时函数执行以后返回的结果
#可以通过return指定函数的返回值	
#可以直接使用函数的返回值，也可以通过一个变量来接受函数的返回值

# def sum(*a):
# 	result=0
# 	for n in a:
# 		result+=n
# 	print(result)
# sum(123,456,789)

#return 后跟什么值函数就会返回什么值，
#return 后边可以跟任意的对象，返回值甚至可以是一个函数
#如果只写return,或者不写return,则相当于 return None
#在函数中，return后的代码都不会执行，return一旦执行函数自动结束
#break用来退出当前循环，continue用来跳过本次循环，return用来结束函数
# def fn():
# 	return 200

# r=fn()#这个函数的执行结果就是它的返回值
# print(fn())
# print(r)

def fn5():
	return 10

#fn5 和 fn5()的区别
print(fn5)#fn5是函数对象，打印fn5实际上是在打印函数对象<function fn5 at 0x00000198CE6C7F70>
print(fn5())#fn5()是在调用函数对象，打印fn5()实际上是在打印fn5()函数的返回值
