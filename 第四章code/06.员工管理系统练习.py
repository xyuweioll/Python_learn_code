employees=['\t孙虎空\t18\t男\t花果山']
while True:
	print('=======================欢迎使用员工管理系统======================')

	print('请选择要做的操作:')
	print('           1.查询员工')
	print('           2.添加员工')
	print('           3.删除员工')
	print('           4.退出系统')
	ID=input('请选择(1-4)->')
	print('===============================================================')
	if ID==str(1):
		print('\t序号\t姓名\t年龄\t性别\t住址')
		n=1
		for employee in employees:

			print(f'\t{n}\t{employee}')
			n+=1
	elif ID==str(2):
		name=(input('请输入姓名->'))
		age=(input('请输入年龄->'))
		sex=(input('请输入性别->'))
		adress=(input('请输入住址->'))
		a='\t'+name+'\t'+age+'\t'+sex+'\t'+adress
		employees.append(a)
	elif ID==str(3):
		b=int(input('请输入你想删除的员工序号：->'))
		b-=1
		c=len(employees)-1
		if 0 < b <= c:
			del employees[b]
		else:
			print('您输入的序号超出范围')
	elif ID==str(4):
		input('欢迎使用，再会！')
		break
	else:
		print('您输入的有误，请重新输入！')
	print('===============================================================')


