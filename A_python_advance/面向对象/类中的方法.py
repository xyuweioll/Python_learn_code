# 类中的方法：动作
# 种类：普通方法   类方法    静态方法    魔术方法

'''
普通方法格式：
def 方法名(self[,参数,参数]):
    pass



'''


# class Phone():
#     brand = "xiaomi"
#     price = 4999
#     type = 'xiaomi 10'
#
#     # Phone类里面的方法：call
#     def call(self):  # self会把当前对象传进去
#         print('self------------->', self)
#         print('正在打电话...')
#
#
# phone1 = Phone()
# print(phone1.brand)
# phone1.call()   # 会把当前对象phoneq传到self中
#
# phone2 = Phone()
# print(phone2.brand)
# phone2.call()
# ===============================================

class Phone:
    # 魔术方法之一：   称作魔术方法  __名字__()
    def __init__(self):  # init 初始化，
        print('--------init')
        self.price = 3000
        self.brand = 'huawei'

    def call(self):  # self不断发生变化
        print('---------->>>')
        print('价格：', self.price)  # 不能保证每个self中都存在price


p = Phone()
p1 = Phone()











