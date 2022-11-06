'''
文件上传
保存log

系统函数：
open(file,mode,buffering,encoding)  #buffering缓存
如果读取的内容是图片则不能使用默认的读取方式,应设置参数 mode = 'rb'
'''
stream = open()  # 按住ctrl见单击函数名即可查看源码.open返回值是流
stream.read()
result = stream.readable()  # 返回值为布尔值，判断文件是否可读
line = stream.readline()  # 一行一行读，但如果上面已经用过read函数读取内容则后面就无法再读到内容
lines = stream.readlines()  # 读多行，将结果读到列表中
while True:  # 通过readline读取所有行
    line1 = stream.readline()
    print(line1)
    if not line1:
        break
'''
mode:r/w/rb/wb
r:read 读
w:write 写
b:binary 二进制
rb:二进制读
wb:二进制写
'''
s = '''
你好！
    欢迎
    123
'''             # 3个'是保留原格式文本
result = stream.write(s)  # 当mode = 'w'写内容时原来的内容都会被清空,想要原有内容不被清空使用追加,mode = 'w'
print(result)

stream.close()  # 释放资源


# ======================================================================================================
# 文件的复制
'''
源文件：c:\p1\girl.jbg
目标文件：c:\p2\girl.jpg
with 结合open使用，可以帮助我们自动释放资源
'''
with open(r'c:\p1\girl.jbg', 'rb') as stream:
    container = stream.read()  # 读取文件内容

    with open(r'c:\p2\girl.jpg', 'wb') as wstream:
        wstream.write(container)
    print('复制完成！')














