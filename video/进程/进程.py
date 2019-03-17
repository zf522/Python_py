# 进程：每次创建一个进程，操作系统会给这个进程分配对应的运行资源，一个进程里默认有一个线程
# 真正干活的是线程，进程只提供资源

# 使用多进程也可以完成多任务
# 进程会按照顺序执行
import multiprocessing
import time


def show():
    for i in range(10):
        print("show")
        time.sleep(0.2)


def show_msg():
    for i in range(10):
        print("show_msg")
        time.sleep(0.2)


if __name__ == '__main__':
    multiprocessing1 = multiprocessing.Process(target=show)
    multiprocessing2 = multiprocessing.Process(target=show_msg)

    multiprocessing1.start()
    multiprocessing2.start()
