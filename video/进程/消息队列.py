import multiprocessing

L = [1, 2, 3]
queue = multiprocessing.Queue(3)
queue.put("lisi")
queue.put(1)
queue.put(L)

print(queue.get())
print(queue.get())
print(queue.get())
