#遍历字典
# keys() 该方法会返回字典的所有key
d={'name':'孙悟空','age':'25','gender':'男'}
# print(d.keys())
# dict_keys(['name', 'age', 'gender'])
# [Finished in 0.3s]
#通过遍历keys()来获取所有的键
#for k in d.keys():
	# print(k)
# name
# age
# gender
# [Finished in 0.4s]
	##通过键值遍历获取值
#该方法会返回一个序列,序列中保存有字典的所有的键
#通过遍历keys()来获取所有的键


# values()
#该方法会返回一个序列,序列中保存有字典所有的值
# for v in d.values():
# 		print(v)
# 孙悟空
# 25
# 男
# [Finished in 0.3s]


# items()
# 该方法会返回字典中所有的项(键值对)
#它会返回一个序列,序列中包含双值子序列
#双值分别是字典中的key和value
# print(d.items())
# dict_items([('name', '孙悟空'), ('age', '25'), ('gender', '男')])
# [Finished in 0.3s]

# for k,v in d.items():
# 	print(k,'=',v)
# name = 孙悟空
# age = 25
# gender = 男
# [Finished in 0.3s]

