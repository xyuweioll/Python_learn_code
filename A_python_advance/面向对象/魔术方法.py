# 魔术方法
# __init__
'''
初始化的魔术方法
触发时机：初始化对象时触发（不是实例化触发，但是和实例化在一个操作中）
参数：至少有一个self，接收对象
返回值：无
作用：初始化对象的成员
注意：使用该方式初始化的成员都是直接写入对象当中，类中无法具体
# '''


# class Person:
#     def __init__(self, name):
#         self.name = name
#         print('-------------->init')
#
#     def __new__(cls, *args, **kwargs):
#         print('-------------->new')
#         super()
#
# p = Person('JACK')
#
# # __new__
# '''
# 实例化魔术方法
# 触发时机：在实例化时触发
# '''
# ================================================================

class Student:
    def __init__(self, student_list):
        self.student = student_list

    # 魔法函数
    def __getitem__(self, item):  # item 从0开始，直到Python运行抛出异常自动结束for循环
        return self.student[item]

    def __len__(self):
        return len(self.student)



student = Student(['固安', '夏洛', '大海'])
print(type(student))
student_1 = student[:2]
print(type(student_1))
print(len(student_1))
print(len(student))
students = student.student

# for item in students:
#     print(item)

for item in student:
    print(item)

'''
魔术方法是Python定义的
魔术方法是名称不能随意更改
对当前的类进行了功能拓展
item 从0开始，直到Python运行抛出异常自动结束for循环


魔法方法可以更改当前类的类型
如果要对一个对象进行迭代的话
    当前对象一定是一个迭代器
'''
# 魔术方法一览
