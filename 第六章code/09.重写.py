class Animal:

	def run(self):
		print('动物会跑')

	def sleep(self):
		print('动物睡觉')



class Dog(Animal):
	def run(self):
		print('狗子跑的飞快')

	def bark(self):
		print('狗狗会叫')
#如果在子类中有和父类同名的方法，则通过子类实例去调用方法时，会调用子类的方法，
#而不是父类的方法，这个特性我们称为方法的重写（覆盖，override）
#创建Dog类实例
#

# d=Dog()
# d.run()

#当我们调用一个对象的方法时，会优先去当前对像中寻找是否具有该方法，如果有则直接
#调用，如果没有，则去当前对象的父类中寻找，如果父类中有则直接调用父类中的方法
#如果没有，则去父类的父类中寻找，以此类推，直到找到object,如果依然没有找到则报错


