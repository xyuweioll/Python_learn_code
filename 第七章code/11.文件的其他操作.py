import os
from pprint import pprint

#os.listdir()获取指定目录结构(默认获取当前目录)
#需要一个路径参数，会获取到该路径下的目录结构，默认路径为. 也就是当前目录
#该方法会返回一个列表，目录中的每一个文件(夹)的名字都是列表中的一个元素
# r=os.listdir()


#os.getcwd() 获取当前所在的目录
# r=os.getcwd()

#os.chdir()切换当前所在目录,作用相当于cd
# os.chdir('..\\..\\..')
# r=os.getcwd() 

#创建目录
#os.mkdir("aaa") #在当前目录下创建一个名字为aaa的目录

#删除目录
# os.rmdir("aaa")

# pprint(r)

# open('aa.txt','w')
#删除文件
os.remove('aa.txt')

#os.rename('旧名字','新名字')可以对一个文件重命名，也可以用来移动一个文件
