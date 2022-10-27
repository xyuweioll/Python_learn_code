#if-elif-else
#语法：
#  if 条件表达式:
#      代码块1
#  elif 条件表达式:
#      代码块2
#  elif 条件表达式:
#      代码块3
#  elif 条件表达式:
#      代码块4
#  elif 条件表达式:
#      代码块5
#  else :
#     代码块6
#执行流程：由上至下依次对条件表达式进行求值判断,
#如果条件表达式的结果为True,则执行当前代码块,然后语句结束
#如果条件表达式的结果为False,则继续向下判断,直到True为止
#如果所有的条件表达式结果都为False,则执行else后的代码块
#if-elif-else 中只会有一个代码块会执行
#if age > 200 :
#	print('活着可真没意思啊')
#elif 100 < age <= 200 :
#	print('活着有点无聊了')
#elif 50 < age <= 100 :
#	print('活着还比较有意思')
#elif 20 < age <= 50 :
#	print('人间值得')
#elif 5 < age <= 20 :
#	print('英年早逝')
#else :
#	print('不要迷恋哥，哥只是传说！')
#练习
#1.编写一个程序，获取一个用户输入的整数。然后通过程序显示这个数
#是奇数还是偶数
#number = int(input('请输入一个整数->'))
#if number % 2 == 0:
#	print(number,'是偶数')
#else:
#	print(number,'是奇数')

#2编写一个程序，检查任意一个年份是否是闰年
#如果一个年份可以被4整除不能被100整除，或者可以被400整除就是闰年
#year = int(input('请输入年份->'))
#if (year % 4 ==0 ) and (year % 100 !=0):
#	print('年份',year,'是闰年！')
#elif year % 400 ==0:
#	print('年份',year,'是闰年！')
#else:
#	print('年份',year,'不是闰年！')

#3编写一个程序，获取用户输入的狗的年龄，然后通过程序显示其相当
#于人类的年龄，如果用户输入负数，显示一个提醒信息（狗的前两年
#每一年相当于人类的10.5岁，然后每增长1岁相当于人类4岁
#age = float(input('请输入狗狗的年龄->'))
#if  0<= age <=2:
#	print('狗狗的人类年龄是;',10.5 * age)
#elif age > 2:
#	print('狗狗的人类年龄是：',21+(age-2)*4)
#else:
#	print('请输入正确的年龄格式')

#4从键盘键入小明期末考试的成绩
#      当成绩为100时,奖励一辆BMW
#      当成绩为[80-99]时奖励一台iphone
#      当成绩为[60-79]时奖励一本参考书
#      其他时，什么奖励也没有
#score = float(input('请输入成绩：'))
#if score ==100:
#	print('奖励一辆BMW')
#elif    80<=score<=99:
#	print('奖励一台iPhone')
#elif    60<=score<=79:	
#	print('奖励一本参考书')
#elif    0<=score<60:
#	print('什么奖励也没有')
#else:
#	print('请输入正确的分数格式')
#5大家都知道男大当婚，女大当嫁，那么女方家长要嫁女儿，当然要提出一定的
#条件：
#高：180cm以上；富1000万以上；帅500以上；
#如果三个条件都满足，则“我一定要嫁给他”
#如果三个条件有为真的情况，则“嫁吧，比上不足比下有余”
#如果三个条件都不满足，则“不嫁”
# hight = float(input('请输入你的身高(cm)->'))
# money = float(input('请输入你的资产(万)->'))
# charming = float(input('请输入你的颜值分->'))
# if hight>=180 and money>=1000 and charming>=500:
# 	print('我一定要嫁给你！')
# elif hight>=180 or money>=1000 or charming>=500:
# 	print('嫁，比上不足比下有余')
# else:
# 	print('不嫁!')
