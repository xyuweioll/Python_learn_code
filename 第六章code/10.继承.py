class Animal:
	def __init__(self,name):
		self._name=name

	def run(self):
		print('动物会跑')

	def sleep(self):
		print('动物睡觉')

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self,name):
		self._name=name
	
#父类中的所有方法都会被子类继承，包括特殊方法，也可以重写特殊方法

class Dog(Animal):
	def __init__(self,age):
		#希望可以直接调用父类的__init__来初始化父类中定义的属性
		#super() 可以用来获取当前类的父类,并且通过super()返回对象调用父类方法时不需要
		#传递self
		super().__init__(name)
		self._age=age
	def run(self):
		print('狗子跑的飞快')

	def bark(self):
		print('狗狗会叫')

	@property
	def age(self):
		return self._age

	@age.setter
	def age(self,age):
		self._age=age
	
	
d=Dog('hashiqi',18)
d.run()
print(d.age)

