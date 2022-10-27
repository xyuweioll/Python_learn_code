#在控制台种打印如下图形
#*****
#*****
#*****
#*****
#*****
# i=0
# while i<5:
#   print('*****')
#   i+=1
#方案1：
# row=int(input('输入你想打印的行数'))
# col=int(input('输入你想打印的列数'))
# i=1
# while i<=row:
#   print('*'*col)
#   i+=1
#方案2：
# row=int(input('输入你想打印的行数'))
# col=int(input('输入你想打印的列数'))
# i=1
# while i<=row:
#     j=1
#     while j<=col:
#         print("* ",end='')
#         j+=1
#     print('')
#     i+=1

#打印
#*
#**
#***
#****
#*****
#******
row=int(input('请输入您想打印的行数'))
i=1
while i<=row:
    j=1
    while j<=i:
        print("* ",end='')
        j+=1
    print()
    i+=1
