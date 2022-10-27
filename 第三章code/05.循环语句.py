# 循环语句
# 循环语句可以使指定的代码块重复指定的次数
# 循环语句分为两种，while循环和for循环
# while循环
# 语法：
#    while  条件表达式:
#        代码块
#  执行流程：
# while语句执行时先对while后的条件表达式进行求值判断，True执行循环体（代码块），
# 循环体执行完毕后，继续对条件表达式进行求值判断，以此类推，直到判断结果为False
# 则循环终止，如果循环有对应的else，则执行else后的代码块
# 条件表达式恒为True是称为死循环
# 循环的三个要件（表达式）
# 初始化表达式，通过初始化表达式初始化一个变量
# i=0
# 条件表达式，条件表达式用来设置循环执行的条件
# while i<10:
# 更新表达式,修改初始化变量的值
#    i+=1
#    print('hello')


# 练习1.求100以内所有的奇数之和

# i=1
# a=1
# b=0
# while i<100:
# 	b=b+i
# 	print('此时的i=',i,'此时的b=',b,'这是第',a,'次循环')
# 	i+=2
# 	a+=1
# else:
# 	print('100内的奇数之和为',b)

#练习2.求100以内所有7的倍数之和以及个数

# i=7
# a=0
# b=0
# while i<100:
# 	b=b+i
# 	a+=1
# 	print('此时i=',i,'此时b=',b,'此时7倍数的个数为',a,'个')
# 	i+=7
# else:
# 	print('100内7的倍数之和为',b,'个数为',a,'个')

#练习3：水鲜花数是指一个n位数（n大于等于3），它的每个
#每个位上的数字的n次幂之和等于它本身（例如：1**3+5**3
#+3**3=153，求出1000以内所有的水鲜花数

# i=1
# while i<=1000:
# 	a=1#用于判断该数是几位数
# 	b=i
# 	while b/10 >=1:
# 		a+=1
# 		b/=10
# 	if (i%10)**a+(int(i/10)%10)**a+(int(i/100)%10)**a+(int(i/1000)%10)**a==i:
# 		print(i,'是水鲜花数')
# 	i+=1


#练习4：获取用户输入的任意数，判断其是否为质数
# num=int(input('请随机输入一整数->'))
# i=2
# a=0
# while i<num:
# 	if num%i==0:
# 		a+=1
# 	i+=1

# if a>0:
# 		print(num,'不是质数')
# else:
# 		print(num,'是质数')
	

#循环嵌套练习
#1打印99乘法表


# row=1
# while row<=9:
#     a=1
#     while a<=row:
#         print(a,'*',row,'=',a*row,'  ',end='')
#         a+=1
#     row+=1
#     print()

# 2 求100以内所有的质数
from time import *
begin=time()
print('本程序可求出n以内的所有质数')
n=int(input('请输入n->'))
i=1
while i<n:
    b=0
    a=2
    while a<i:
        if i%a==0:
            b=1
        a+=1
    if b==0:
        print(i,'是质数')
    i+=1
end=time()
print('程序执行花费了',end-begin,'秒')
