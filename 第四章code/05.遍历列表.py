#遍历列表指定是将列表中的所有元素取出来
#创建一个列表
# stus=['孙悟空','猪八戒','沙和尚','唐僧','蜘蛛精','白骨精']
#一般通过循环来便利列表
# i=0
# a=len(stus)
# while i<a:
# 	print(stus[i])
# 	i+=1

#通过for循环遍历列表
#语法：
#     for 变量 in 序列:
#          代码块
#for循环的代码块会执行多次,序列中有几个元素就会执行几次
#每执行一次就会将序列中的一个元素赋值给变量
# for s in stus:
 # print(s)

 ##EMS练习(employee Manger System 员工管理系统) 练习
 #-做命令行版本的员工管理系统
 #-功能有四个：
              1.查询员工
                  -显示当前系统中的所有员工
              2.添加员工
                  -将员工添加到当前系统中
              3.删除员工
                  -将员工从系统中删除
              4.退出
                  -退出系统
   -员工信息保存到列表中