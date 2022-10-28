	#创建字典
#使用{}
#语法:{k1:v1,k2:v2,k3:v3}
#使用dict()函数来创建字典,这种方式创建的字典，key都是字符串
# d=dict(name='孙悟空',age='18',gender='男')
# print(d,type(d))
#{'name': '孙悟空', 'age': '18', 'gender': '男'} <class 'dict'>
#[Finished in 0.2s] 
#也可以将一个包含有双值子序列的序列转换为字典
#双值序列，序列中只有两个值 如：[1.2] ('a',3)  'ab'
#如果序列中的元素也是序列，那么我们称这个元素为子序列
#[(1,2),(3,5)]
# d=dict([('name','孙五'),('age',18)])
# print(d,type(d))
#{'name': '孙五', 'age': 18} <class 'dict'>
#[Finished in 0.1s]
#len()获取字典中键值对的个数
#print(len(d))
# in 检查字典中是否包含指定的键
#not in 检查字典中是否不包含指定的键
#print('name' in d)
#True
#[Finished in 0.1s]
#获取字典中的值，根据键来获取值
#语法：d[key]
#print(d['name'])
#孙悟空
#[Finished in 0.1s]

#通过[]获取值时，如果键不存在，会抛出异常
#通过 get(key[,default]) 该方法来根据键来获取字典中的值
#通过该方法，如果获取的键在字典中不存在，会返回none,并不会报错
#print(d.get('name'))
#print(d.get('hello','默认值')),如果值不存在则返回默认值


#修改字典
#d[key]=value  即key存在则覆盖，不存在则添加
# d['name']='sunwukong' #修改字典的key-value
# d['address']='花果山' # 向字典中添加key-value
# print(d)

# setdefault(key[,default])可以用来向字典中添加key-value
#如果key已经存在于字典中，则返回 key的值，不会对字典做任何操作
#如果key不存在，则向字典中添加这个key,并设置value

#update([other])
#将其他的字典中的key-value添加到当前字典中,如果有重复的key,则后边的会替换掉当前的
d={'a':1,'b':2,'c':3	}
d2={'d':4,'e':5,'f':6}
d.update(d2)
# print(d)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# [Finished in 0.3s]


#删除可以使用del 来删除字典中的键值对 key-value,
# del d['a']  del若删除不存在的值也会报错
# print(d)
# {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
# [Finished in 0.3s]

#popitem()
#随机删除字典中的一个键值对,一般都会删除最后一个键值对
# d.popitem()  popitem是有返回值的,返回的是一个键值对
#当用popitem去删除一个空字典的时候会报错


#pop(key[,default])
#根据key删除字典中的key-value,它会将删除的值返回(注意返回的不是键值对)
#如果删除不存在的kye,会抛出异常,若写了默认值,则返回默认值并不会报错
#
#

#clear()用来清空字典
#d.clear()

#copy()
#该方法用于对字典进行浅复制,
#注意,浅复制会简单复制对象内部的值,如果值也是一个可变对象,这个可变对象不会被复制
#d2=d.copy()
#这样的化d2与d虽然相同,但指向的不是同一对象,即ID值不同,修改一个也不会影响另一个
#

