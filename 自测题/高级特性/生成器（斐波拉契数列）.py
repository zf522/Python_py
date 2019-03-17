# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n += 1
#     return 'done'
#
#
# fib(6)


# 将fib函数变成generator，只需要将print改成yield,此时，fib()就是一个generator
# generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n += 1
    return 'done'

# for f in fib(6):
#     print(f)

f= fib(6)
while True:
    try:
        x = next(f)
        print("斐波拉契数列：" ,x)
    except StopIteration as e:
        print("fib_Exception is :",e.value)
        break



