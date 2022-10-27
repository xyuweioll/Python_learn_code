#模块，通过模块可以对python进行扩展
#引入一个time模块，来统计程序执行的时间
#from time import *
#time()函数可以用来获取当前的时间，返回的单位是秒
#
#2 求100以内所有的质数


#优化1
from time import *
begin=time()
print('本程序可求出n以内的所有质数')
n=int(input('请输入n->'))
i=1
while i<n:
    b=0
    a=2
    while a<=int(i**(1/2)):#优化点2
        if i%a==0:
            b=1
            break#（优化点1）
        a+=1
    if b==0:
        print(i,'是质数')
    i+=1
end=time()
print('程序执行花费了：',end-begin,'秒')


#通过将while循环全部用for循环替换进行进一步优化
# from time import *
# begin=time()
# print('本程序可求出n以内的所有质数')
# n=int(input('请输入n->'))
# for i in range(1,n):
#     b=0
#     a=2
#     for a in range(2,int(i**(1/2)+1)):#优化点2
#         if i%a==0:
#             b=1
#             break#（优化点1）
#         a+=1
#     if b==0:
#         print(i,'是质数')
# end=time()
# print('程序执行花费了：',end-begin,'秒')