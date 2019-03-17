import multiprocessing
import time


def show(name):
    print('show:', multiprocessing.current_process())
    print(name)
    while True:
        for i in range(3):
            print("哈哈")
            time.sleep(0.2)


# def show_msg(name):
#     for i in range(10):
#         print(name)
#         time.sleep(0.2)


if __name__ == '__main__':
    print('main:', multiprocessing.current_process())
    first = multiprocessing.Process(target=show, args=("李四",))
    # second = multiprocessing.Process(target=show_msg("张三"))
    # 创建守护进程
    first.daemon = True
    # 让子进程终止，销毁子进程
    # first.terminate()

    first.start()
    # second.start()
    time.sleep(1)
    print("over")
