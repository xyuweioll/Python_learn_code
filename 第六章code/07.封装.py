class Person:
	def __init__(self,name):
		self._name=name
    #property装饰器，用来将一个get方法，转换为对象的属性
    #添加完property装饰器以后，我们就可以像调用属性一样使用get方法
    #当不使用修饰器时setter和getter方法的名字不可设置成一样的，但当两者都使用修饰器
    #二者的名字应该一样，最后和变量的名字保存一致
	@property 
	def name(self):
		print('get方法执行了')
		return self._name

	# setter方法的装饰器：@属性名.setter
	@name.setter
	def name(self,name):
		self._name=name


p=Person('猪八戒')
p.name='sj'
print(p.name)

	 