#在对集合做运算时不会对原集合产生影响,而是将运算结果返回
#创建集合
# s1={1,3,5,7,9,0,2}
# s2={0,2,4,6,8}
# result=s1&s2
# print(resuli)
# {0, 2}
# &交集运算
# | 并集运算
# result=s1|s2
# print(result)
# {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# [Finished in 0.4s]

#-差集运算
# result=s1-s2
# print(result)
# {1, 3, 5, 7, 9}
# [Finished in 0.1s]

#^亦或集(即并集与交集的差)
# result=s1^s2
# print(result)
# {1, 3, 4, 5, 6, 7, 8, 9}
# [Finished in 0.1s]

#<= 检查一个集合是否是另一个集合的子集
# a={1,2,3}
# b={1,2,3,4,5,6}
# result=a<=b
# print(result)
# True
# [Finished in 0.1s]

#< 检查一个集合是否是另一个集合的真子集
