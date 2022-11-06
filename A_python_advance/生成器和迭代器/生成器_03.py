'''
生成器方法：
__next__():获取下一个元素
send(value):向每次生成器调用中 传值 注意：第一次调用必须传send(None)
'''

def gen():
    i = 0
    while i < 5:
        temp = yield i
        print('temp:', temp)
        i += 1
    return '没有更多的数据了！'

g = gen()

print(next(g))

# g.__next__()
print(g.send(None))
n1 = g.send('呵呵')
print('n1:', n1)
n2 = g.send('哈哈')
print('n1:', n2)
