import os
lst=os.listdir('C:\\Users\\xianyu\\Desktop\\python\\第六章code')
for filename in lst :
	if filename.endswith('.py'):
		print(filename)