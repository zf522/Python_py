import time
import threading


def A(count):
    print("我是一个子线程！")
    while True:
        for i in range(count):
            print("aa")
            time.sleep(0.2)


# 设置守护线程damon=True，当主线程退出，子线程直接销毁不再执行代码
a_thread = threading.Thread(target=A, args=(10,), daemon=True)
a_thread.start()

time.sleep(1)

print("主线程会等子线程执行完程序以后再退出！")
