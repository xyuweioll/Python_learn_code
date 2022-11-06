# 列表推导式   字典推导式  集合推导式
# 旧的列表--》新的列表

# 1. 列表推导式：格式：[表达式 for 变量 in 旧列表] 或者 [表达式 for 变量 in 旧列表 if条件]

# 过滤掉长度小于等于3的人名,并首字母大写
names = ['tom', 'lily', 'abc', 'jack', 'steven', 'bob']
result = [name.title() for name in names if len(name) > 3]
print(result)
result = [name.capitalize() for name in names if len(name) > 3]
print(result)

# 将1-100之间能被3整除的数放列表里
num = [i for i in range(1, 101) if i % 3 == 0]
print(num)

# 双重循环
num_1 = [(i, j) for i in range(5) if i % 2 == 0 for j in range(10) if j % 2 != 0]
print(num_1)

# 带else的推导式
dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'lucy', 'salary': 8000}
dict3 = {'name': 'jack', 'salary': 4500}
dict4 = {'name': 'lily', 'salary': 3000}
list1 = [dict1, dict2, dict3, dict4]
# if薪资大于5000加200，低于等于5000加500
newlist = [employee['salary'] + 200 if employee['salary'] > 5000 else employee['salary'] + 500 for employee in list1]
newlist2 = [{'name':employee['name'],'salary':employee['salary']+200} if employee['salary'] > 5000 else {'name':employee['name'],'salary':employee['salary']+500} for employee in list1]
print(newlist2)

# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}  # 将字典的键与值进行交换
newdic = {value: key for key,value in dict1.items()}
print(newdic)
