import prettytable as pt
def show_tickets(row_num):
	tb=pt.PrettyTable()  #定义类，将该表格定义为该类
	tb.field_name=['行号','座位1','座位2','座位3','座位4','座位5']   #调用类里的field_name方法对表头进行赋值
	for i in range(row_num):
		lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
		tb.add_row(lst)
	print(tb)

# def order_ticket(row_num,row,column):
# 	tb=pt.PrettyTable()
# 	tb.field_name=['行号','座位1','座位2','座位3','座位4','座位5']
# 	for r in row_num:
# 		lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
# 		if r==(int(row_num)-1):
# 			lst[int(column)]='无票'
# 		tb.add_row(lst)
# 	print(tb)



		
if __name__=='__name__':
	row_num=13
	show_tickets(row_num)
# 	chose_num=input('请输入选择的座位->(如13排5座即13,5)')
# 	try:
# 		row,column=chose_num.split(',')
# 	except:
# 		print('输入格式有误')

# 	order_ticket(row_num,row,column)





# import prettytable as pt
# def show_tickets(row_num):
# 	tb=pt.PrettyTable()  #定义类，将该表格定义为该类
# 	tb.field_name=['行号','座位1','座位2','座位3','座位4','座位5']   #调用类里的field_name方法对表头进行赋值
# 	for i in range(row_num):
# 		lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
# 		tb.add_row(lst)
# 	print(tb)

# def order_ticket(row_num,row,column):
# 	tb=pt.PrettyTable()
# 	tb.field_name=['行号','座位1','座位2','座位3','座位4','座位5']
# 	for i in range (row_num):
# 		if int(row)==i+1:
# 			lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
# 			lst[int(column)]='无票'
# 			tb.add_row(lst)
# 		else:
# 			lst=[f'第{i+1}行','有票','有票','有票','有票','有票']
# 			tb.add_row(lst)
# 	print(tb)



		
# if __name__=='__name__':
# 	row_num=13
# 	show_tickets(row_num)
# 	choose_num=input('请输入选择的座位->(如13排5座即13,5)')
# 	try:
# 		row,column=choose_num.split(',')
# 	except:
# 		print('输入格式有误')

	# order_ticket(13,3,5)
	# show_tickets(13)