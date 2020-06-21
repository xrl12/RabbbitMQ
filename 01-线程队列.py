from multiprocessing import Queue  # 进程间的队列
from queue import Queue  # 线程之间的队列

q = Queue(maxsize=20)  # 表示这个对列对大可以放20条消息  默认是先进先出
q.put('你好')
q.put('我不好')
q.put('我非常不好')

q1 = q.get()
q2 = q.get()
q3 = q.get()
q4 = q.get(block=False)  # 如果block为True队列里面没有消息不会报错，如果为False就会报错，默认是True

print(q1, q2, q3)
