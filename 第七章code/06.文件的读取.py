# file_name='demo.txt'

# try:
# 	#调用open()来打开一个文件，可以将文件分成两种类型
# 	#一种是纯文本文件(使用utf-8等编码编写的文件)
# 	#一种是二进制文件(图片、mp3、ppt等文件)
# 	#open()打开文件时默认是以文本文件的形式打开的，但是open()默认的编码为None
# 	# 所以处理文本文件时，必须要指定文件的编码
# 	with open(file_name,encoding='utf-8') as file_obj:
# 		#通过read()来读取文件中的内容
# 		#如果直接调用read()它会将文本文件的所以内容全部读取出来
# 		#    如果要读取的文件较大的话，会一次性将文件的内容加载到内存中，容易导致
# 		#    内存泄露
# 		#    所以对于内存较大的文件不要直接调用read()
# 		#read()可以接受一个size作为参数，该参数用来指定要读取的字符的数量
# 		#默认值为-1，它会读取文件中的所以字符
# 		#可以为size指定一个值，这样read()会读取指定数量的字符，
# 		#     每一次读取都是接着上次读取结束的位置接着读取
# 		#      如果字符数量小于size,则会读取剩余所以的字符
# 		#      如果已经读取到了文件的结尾处，则会返回''空串
# 		content=file_obj.read()
# 		print(content)

# except FileNotFoundError:
# 	print(f'{file_name} 这个文件不存在')


#读取大文件的方式

file_name = 'demo2.txt'
try:
	with open(file_name,encoding='utf-8') as file_obj:
		#定义一个变量，来指定每次读取的大写
		chunk=100
		#创建一个循环来读取文件内容
		while True:
			#读取chunk大小的内容
			content=file_obj.read(chunk)
			#检查是否读取到了内容
			if not content:
				break
				#内容已经读取完毕

			#输出内容
			print(content,end='')


except FileNotFoundError:
	print(f'{file_name} 这个文件不存在')

