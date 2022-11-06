'''
面向对象：
程序        现实中
对象        具体的事务

现实中的事务-》转成电脑程序。
世间万物皆对象

好处：
    类
    对象
    属性
    方法

对象：关羽的手机
    张飞的手机
    刘备的手机
    ...
    对象的集合--->共同的特征：品牌 颜色 大小 价格     动作：打电话 发短信 上网 打游戏

    类别：手机类
        学生类

    多个对象--》提取对象的共同特征和动作-----》封装到一个类中

'''
# 所有的类名要求首字母大写，多个单词使用驼峰式命名法
'''
class 类名【(父类)】:
    属性: 特征
    
    
    方法: 动作
'''
class Phone(object):   # 默认继承object,可不写
    # 属性
    brand = 'huaiwei'


print(Phone)

# 使用类创建对象
yupeng = Phone()
print(yupeng)
print(yupeng.brand)
yupeng.brand = 'iPhone'
print(yupeng.brand)
feifei = Phone
print(feifei)
print(feifei.brand)
jj = feifei()
print(jj)

xiaowei = Phone()

'''
type class object之间的关系
type可以创建python中的对象 python一切皆对象
type继承了object, object由type创建，object是Python中最底层的基类 
type是由自身创建的
class 在Python中声明了一个类
'''
'''
type可以创建对象，所有的对象继承自object，type创建了object,type继承自object,type创建了自身
'''
'''
对象的三个特征：
    1.身份：可以通过id(对象)进行查询
    2.类型：可以通过type(对象)进行查看
    3.值
None(全局只要一个)

#创建对象必须有类型：
    数值
    迭代类型：迭代器和生成器
    序列类型：序列类型使用魔术方法
    映射
    集合
    上下文管理类型(with)
    其他
'''