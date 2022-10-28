#列表的方法	
stus=['孙悟空','猪八戒','沙和尚']
print('原列表',stus)
#append() 向序列的末尾添加一元素
# stus.append('唐僧')
# print(stus)
# #insert() 向列表的指定位置插入一个元素
# #其有两个参数，第一个是要插入的位置，第二个是要插入的元素		
# stus.insert(2,'白骨精')
# print(stus)

#extend()
#使用新的序列来拓展当前序列
# stus.extend('唐僧','白骨精')，相当于在stus列表后加入'唐僧','白骨精'
# 即加一个可以用append(),加多个用extend()

#clear()
#清空序列
# stus.clear(),此时stus中的元素全部被清空
#pop()
#根据索引删除并返回指定元素
#a=stus.pop(2),即删除序列为2的元素并返回被删除元素的值，不写索引则删除最后一个元素
#remove()删除指定值的元素
#stus.remove('猪八戒')若有重复值，则删除第一个
#reverse()
#用来反转列表
#sort()用来对列表中的元素进行默认升序排序
#stus.sort()
stus.sort(reverse=True)降序排列
print(stus)
#

