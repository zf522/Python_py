#递归求和

def sum_num(num):
    if num == 1:
        return 1
    else:
        temp = sum_num(num - 1)
        return temp + num


print(sum_num(100))
