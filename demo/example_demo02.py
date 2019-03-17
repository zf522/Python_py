# def apple():
#     def banana():
#         def orange():
#             print('orange is here')
#         print('banana is here')
#         orange()
#     print('apple is here')
#     banana()
# apple()

# print(sum(range(10)))


def num_value():
    global num
    num = 2


num = 1
num_value()
print(num)
