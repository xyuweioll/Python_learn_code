print('异常出现前')

try:
	print(c)
	print(10/0)
except  NameError:
	#如果except后不跟任何的内容，则此时它会捕获到所有的异常
	#如果在except后跟着一个异常的类型，那么此时它只会捕获该类型的异常
	print('出现NameError 异常')
except  ZeroDivisionError:
	print('出现ZeroDivisionError 异常')

finally:
	print('无论是否出现异常，该子句都会执行')

print('异常出现后')

#Exception 是所有异常的父类，所以如果except后跟的是Exception,他也会捕获到所以的异常
#except 和finally 至少得有一个


##抛出异常
#    -可以使用raise语句抛出异常，
#        raise语句后需要跟一个异常类 或 异常的实例
