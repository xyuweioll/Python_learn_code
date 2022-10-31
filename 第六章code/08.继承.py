#继承
class Animal:

	def run(self):
		print('动物会跑')

	def sleep(self):
		print('动物睡觉')

#定义一个类 animal
#这个类中有两个方法run() sleep()



#定义一个类Dog,该类中有三个方法 run() sleep() bark()
#有一个现成的类可以实现我们需要的大部分功能，但不能实现全部功能
#如何能让这个现成的类实现我们需要的全部功能？
#    方法一：直接修改这个类，在这个类中添加我们需要的功能
#             -但修改起来比较麻烦，并且会违反OCP原则
#    方法二：直接创建一个新的类
#             -创建一个新的类比较麻烦，并且需要大量的进行复制粘贴，会出现大量的
#              重复性代码
#    方法三：直接从Animal类中继承他的属性和方法
#           -继承是面向对象的三大特征之一
#           -通过继承我们可以使一个类获取到其他类中的属性和方法
#           -在定义类时，可以在类名后的括号中指定当前类的父类（超类、基类,，super）
#             子类（衍生类）可以直接继承父类中的所以的属性和方法
#通过继承可以直接让子类继承到父类的属性和方法，避免编写重复性的代码，并且也符合
#OCP原则，所以我们经常需要通过继承来对一个类进行扩展	

class Dog(Animal):
	def run(self):
		print('狗子跑的飞快')

	def bark(self):
		print('狗狗会叫')
	
d=Dog()
d.run()

#isinstance() 用于检查一个对象是否是一个类的实例,如果这个类是这个对象的父类，也会
#返回True

# r=isinstance(d,Dog)
# r=isinstance(d,Animal)
# print(r)

# class Hashiqi(Dog):
# 	def fansha(self):
# 		print('我是一只傻狗！')
# h=Hashiqi()
# h.fansha()

#在创建类时，如果省略了父类，则默认父类为object
#   object是所有类的父类，所有类都继承自object，也就有所有对象都是object的实例
#issubclass(C,B)，用于检查C是不是B的子类，并返回布尔值
# print(issubclass(Dog,Animal))
