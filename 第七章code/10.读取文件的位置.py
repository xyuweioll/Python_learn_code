with open('demo.txt','rb') as file_obj:
	# print(file_obj.read(100))
	# print(file_obj.read(30))
	#seek() 可以修改当前读取的位置
	#seek()需要两个参数
	#  第一个  是要切换到的位置
	#  第二个  是计算位置的方式
	#            可选值：
	#               0 从头计算，默认值
	#               1 从当前位置计算
	#               2 从最后位置开始计算
	file_obj.seek(-5,2)
	print(file_obj.read(5))
	#tell()方法用来查看当前读取的位置
	print('当前读取到了-->',file_obj.tell())


