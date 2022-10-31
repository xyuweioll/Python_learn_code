#特殊方法，也称为魔术方法，
#特殊方法都是使用__开头和结尾的
#特殊方法一般不需要我们手动调用，需要在一些特殊情况下自动执行


#定义一个Person类
class Person():
	def __init__(self,name,age):
		self._name=name
		self._age=age


	#__str__()这个特殊方法会在尝试将对象转换为字符串的时候调用
	#它的作用可以用来指定对象转换为字符串的结果(print 函数)
	def __str__(self):
		return 'Person[name=%s,age=%d]'%(self._name,self._age)

	#__repr__()这个特殊方法会在对当前对象使用repr()函数时调用
	#它的作用是指定对象在'交换模式'中直接输出的结果
	def __repr__(self):
		return 'hello'

	#__gt__会在对象做大于比较时调用，该方法的返回值将会作为比较的结果
	#它需要两个函数，一个self表示当前对象，other表示和当前对象比较的对象
	#self>other
	def __gt__(self,other):
		return self._age>other._age

#创建两个Person类的实例
p1=Person('孙悟空',18)
p2=Person('猪八戒',25)

print(p1)
print(p2)
print(p2>p1)
#当我们打印一个对象时，实际上打印的是对象中的特殊方法__str__()的返回值
#