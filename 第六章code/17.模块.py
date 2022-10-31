# import m1
# # print(m1.a,m1.b)
# #访问模块中的变量：模块名.变量名

# m1.test()
# m1.test2()

# p=m1.Person()
# print(p.name)


#也可以只引入模块中的部分内容
#语法 from 模块名 import 	变量,变量,......
# from m1 import Person
# p1=Person()
# print(p1.name)



# from m1 import test 
# test()

from m1 import * #即可引入test中的所以内容，一般不会使用

#也可以为引入的变量使用别名
#语法：  from 模块名 import 变量 as 别名

