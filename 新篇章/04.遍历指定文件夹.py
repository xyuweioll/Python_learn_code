# import os
# lst_files=os.walk('C:\\Users\\xianyu\\Desktop\\python') #返回一个元组
# # print(lst_files)
# for dirpath,dirname,filename in lst_files:
# 	print(dirpath)  #路径
# 	print(dirname)  #文件夹名字
# 	print(filename) #文件名
# 	print('-'*60)







import os
lst_files=os.walk('C:\\Users\\xianyu\\Desktop\\python') #返回一个元组
print(lst_files)
for dirpath,dirname,filename in lst_files:
	# print(dirpath)  #路径
	# print(dirname)  #文件夹名字
	# print(filename) #文件名
	# print('-'*60)
#------------------------------------------------------------------
	# for fil in filename:
		# if fil.endswith('.py'):
		# 	print(fil)  #将其中所有以.py结尾的文件打印出来
#------------------------------------------------------------------
	# for dir in dirname:
	# 	print(os.path.join(dirpath,dir)) #将文件夹名和其路径连接起来
#-------------------------------------------------------------------
		# for fil in filename:
		# 	print(os.path.join(dirpath,fil)) #将文件名于其路径连接起来