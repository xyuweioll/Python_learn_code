# class Person:
#     #在类中可以定义一些特殊方法(魔术方法)
#     #特殊方法都是以__(双下划线)开头，__结尾
#     #特殊方法不需要我们自动调用，不要尝试调用这种方法
#     #特殊方法将会在特殊的时刻自动调用
#     #学习特殊方法：
#     #    1、特殊方法什么时候调用
#     #    2特殊方法有什么作用
#     #  init会在对象创建以后离开执行
#     #  init可以向新创建的对象中初始化属性
#     #通过self向新创建的对象中初始化属性
#     #调用类创建对象时，类后变得所以参数都会依次传递到init()中
# 	def __init__(self,name):
# 		self.name=name
# 	def say_hello(self):
# 		print('大家好，我是%s' % self.name)
# #目前对于Person类来说name是必须的，并且每一个对象中的name属性基本上都是不同的
# #而我们现在是将name属性在定义完对象以后，手动添加到对象中，这种方式很容易出现
# #错误
# #我们希望，在创建对象时，必须设置name属性，如果不设置对象将无法创建
# #并且属性的创建是自动完成的，而不是在创建对象以后手动完成 
# p1=Person()
# # #手动向对象添加name属性
# # p1.name='孙悟空'
# # p1.say_hello()
# # p2=Person()
# # p2.name='猪八戒'
# # p2.say_hello()
# p1.say_hello()



##类的基本结构
 # class 类名([父类])：
 #     公共的属性
 #      #对象的初始化方法
 #     def __init__(self,...):
 #       ...
 #   #其他方法
 #     def method_1(self,...):
 #       ...


 #练习：
     #尝试自定义一个表示狗的类（Dog)
     #       属性：
     #             name
     #             age
     #             gender
     #             height
     #        方法：
     #             jiao()
     #             yao()
     #             pao()
class Dog:
	def __init__(self,name,age,gender,height):
		self.name=name
		self.age=age
		self.gender=gender
		self.height=height
	def g_jiao(self):
		print('狗狗%s'%self.name,'会叫')

	def g_yao(self):
		print('狗狗%s'%self.name,'会咬人')

	def g_pao(self):
		print('狗狗%s'%self.name,'跑的很快')


p1=Dog('tom',25,'男',100)
p1.g_pao()	
#目前我们可以直接通过 对象.属性 的方式来修改属性的值，这种方式导致对象中的属性可以
#随意修改，非常的不安全，值可以任性修改，不论对错
#现在我们需要一种方式来增强数据的安全性
#  1.属性不能随意修改（我让你改你才能改，不让你改你就不能改）
#  2.属性不能修改为任意的值(如年龄不能是负数)
print(p1.gender)