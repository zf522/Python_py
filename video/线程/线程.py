import time
import threading


def A(count):
    for i in range(count):
        print("aa")
        time.sleep(0.2)


def B():
    for i in range(10):
        print("bb")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程执行对应的代码
    # target表示目标函数
    sub_thread = threading.Thread(target=A, args=(1,))
    sub_thread.start()

    B()

    #线程执行是无序的，由cpu调度
