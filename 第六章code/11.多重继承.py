class A(object):
	def test(self):
		print('AAA')

class B(object):
	def test2(self):
		print('BBB')

class C(B):
	pass

#类名.__bases__ 这个属性可以用来获取当前类的所有父类

print(C.__bases__)

#在Python中是支持多重继承的，也就是我们可以为一个类指定多个父类
#可以在类名的()里边添加多个类，来实现多重继承
#多重继承，会使子类同时拥有多个父类，并且会获取到所有父类中的方法
#在开发中没有特殊情况，应该尽量避免使用多重继承，因为多重继承会让代码
#过于复杂
#如果多个父类中有同名的方法，则会先在第一个父类中寻找，然后找第二个，然后找第三个
#前边父类的方法会覆盖后边父类的方法
#

class D(A,B):
	pass

d=D()
d.test()
d.test2()
