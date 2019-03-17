import threading

num = 0
# 定义一个互斥锁:保证只有一个线程去执行，每个线程按顺序执行
lock = threading.Lock()


def A():
    # 上锁
    lock.acquire()
    global num
    for i in range(1000000):
        num += 1
    print(num)
    # 释放锁
    lock.release()


def B():
    # 上锁
    lock.acquire()
    global num
    for i in range(1000000):
        num += 1
    print(num)
    # 释放锁
    lock.release()


if __name__ == '__main__':
    first_thread = threading.Thread(target=A)
    second_thread = threading.Thread(target=B)

    first_thread.start()
    second_thread.start()
