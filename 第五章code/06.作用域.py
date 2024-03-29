#作用域与命名空间
#作用域(scope)
#作用域指的是变量生效的区域
# def fn():
# 	a=10 # a定义在了函数内部，即它的作用域在函数内部，函数外部无法访问
# 	print('函数内部:','a=',a)

# fn()
# print('函数外部a=',a)
# NameError: name 'a' is not defined
#在Python中有两种作用域：全局作用域，函数作用域
#全局作用域：
#		在程序执行时创建，在程序执行结束时销毁
#		所有函数以外的区域都是全局作用域
#		在全局作用域中定义的变量，都属于全局变量，全局变量可以在程序的任意位置
#		被访问
#函数作用域：
#		-函数作用域在函数调用时创建，在调用结束时销毁
#		-函数每调用一次就会产生一个新的函数作用域
#		-在函数作用域中定义的变量，都是局部变量，它只能在函数内部被访问
#		-当我们使用变量时，会优先在当前作用域中寻找该变量，如果有则使用，如果没有
#		则继续去上一级作用域中寻找，直到找到全局作用域依然没有，则会抛出异常
#如果希望在函数内部修改全局变量，则需要使用global关键字来声明变量





#命名空间（namespace)
#命名空间指的是变量存储的位置，每一个变量都需要存储到指定的命名空间当中
#每一个作用域都会有一个它对应的命名空间
#全局命名空间，用来保存全局变量，函数命名空间用来保存函数中的变量
#命名空间实际上就是一个专门用来存储变量的字典
#locals()用来获取当前作用域的命名空间
#如果在全局作用域中调用locals()则获取全局命名空间，如果在函数作用域中调用locals()
#则获取函数命名空间，	返回的是一个字典
# scope=locals()#当前命名空间
# print(scope)

def fn4():
	#scope=locals()#在函数内部调用locals()会获取到函数的命名空间
	#globals()函数可以在任意位置获取全局命名空间
	global_scope=globals()
	print(global_scope)
    #print(scope)

fn4()
