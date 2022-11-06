# 进程 》 线程 》 协程
#

def tesk1(n):
    for i in range(n):
        print(f"正在搬第{i}块砖！")
        yield None


def tesk2(n):
    for i in range(n):
        print(f"正在听第{i}首歌！")
        yield None


g1 = tesk1(5)
g2 = tesk2(5)

while True:
    try:
        g1.__next__()   # 二者交替进行
        g2.__next__()
    except:
        break

'''
生成器：generator

定义生成器的方式：
1、通过列表推导式方式
    g = (x for x in range(6))
2、函数+yield完成
    def func():
    ...
        yield
    
    g = func()
    
产生元素：
    1.next(generator) --> 每次调用都会产生一个新的元素，如果元素产生完毕再次调用会残生异常
    2.生成器自己的方法：
        g.__next__()
        g.send(value)
        
    应用：协程
'''
