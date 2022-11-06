# 模块：os.py
import os

print(os.path)

path = os.path.dirname(__file__)  # 返回当前文件所在的路径
print(path)
print(type(path))

# 保存
with open(r'c:\p1\girl.jbg', 'rb') as stream:
    container = stream.read()  # 读取文件内容
    path = os.path.dirname(__file__)
    paht1 = os.path.join(path, 'a1.jpg')  # 拼接路径
    with open(paht1, 'wb') as wstream:
        wstream.write(container)
    print('复制完成！')

r = os.path.abspath(r'c:\p1\girl.jbg')  # 判断路径是不是决定路径，返回布尔值；
r1 = os.path.isabs('../images/girls')  # ../表示当前文件的上一级 ../../上一级的上一级

# 通过相对路径得到绝对路径
path = os.path.abspath('aa.txt')
print(path)

# 获取当前文件的绝对路径
path = os.path.abspath(__file__)
print(path)

path = os.getcwd()  # 得到当前文件所在文件夹的绝对路径
print(path)

# os.path
path = r'C:\Users\xianyu\Desktop\论文初稿\3 卫宪钰 2109035 退修稿.docx'
result = os.path.split(path)  # 其返回值为一个元组，第一个值是文件路径，第二个值是文件名
result = os.path.splitext(path)  # 返回一个元组，第一个值为：C:\Users\xianyu\Desktop\论文初稿\3 卫宪钰 2109035 退修稿
# 第二个值为.docx，即可通过这种方式获得文件后缀名


# 获取文件大小，返回值单位为字节
size = os.path.getsize(path)
result = os.path.join(os.getcwd(), 'file', 'a', 'a1.jpg')  # 后面多一个就多一层
'''
# os.path 常用函数
dirname()
join()
split()
splittext()
getsize()
isabs()
isfile()
isdir()
'''

# os.path 里面的函数
'''
os.getcwd()
os.listdir() #返回指定目录里所有的文件夹和文件的名字
'''
# 创建文件夹
os.path.exists('c:\p3')  # 判断文件夹是否存在，返回布尔值
os.mkdir('c:\p3')  # 创建文件夹无返回值
os.rmdir(r'c:\p3') # 只能删除空文件夹
os.remove(r'c:\p3\p4\aa.txt')  # 删除文件

# 删除指定路径的文件夹及内部的文件
path = r'c:\p3\p4'
filelist = os.listdir(path)

for file in filelist:
    path1 = os.path.join(path, file)
    os.remove(path1)
else:
    os.rmdir(path)
print('删除成功')

# 切换目录
os.chdir(r'c:\p')

'''
os模块下的方法：
os.getcwd()  获取当前目录
os.listdir()  浏览文件夹
os.mkdir()   创建文件夹
os.rmdir()  删除空文件夹
os.remove()   删除文件
os.chdir()  切换目录
'''
