#创建一列表
a=[1,2,3]
#修改前
print('修改前',a,id(a))

# a[0]=10
# #修改后
# print('修改后',a,id(a))

#执行结果：修改前 [1, 2, 3] 2638460292224
#修改后 [10, 2, 3] 2638460292224
#[Finished in 0.1s]
#可以发现id值未发生改变
#改对象，会影响所有指向该对象的变量

a=[10,2,3]
print('重新赋值后',a,id(a))
#修改前 [1, 2, 3] 2446702742656
#重新赋值后 [10, 2, 3] 2446702742080
#[Finished in 0.1s]
#可以发现前后的id值发生了改变
#为一个变量重新赋值时都不会影响其他变量
#一般只有在为变量赋值时才是修改变量，其余的都是修改对象


# == ！=  is  is not
# ==  != 比较的是对象的值是否相等
# is  is not 比较的是对象的id是否相当（比较两个对象是否是同一个对象）