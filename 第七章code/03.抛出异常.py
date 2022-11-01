#也可以自定义异常类，只要创建一个类继承Exception即可


def add(a,b):
 	#如果a和b中有负数，就向调用处抛出异常
 	if a<0 or b<0:
 		#raise用于向外部抛出异常，后边可以跟一个异常类，或异常类的实例
 		#抛出异常的目的是告诉调用者这里调用时出现问题，希望你自己处理一下
 		#亦可以用if else来代替异常的处理
 		raise Exception('两个参数中不能有负数！')
 	r=a+b
 	return r

print(add(-123,456))



