"""
第一种方法：
向后顺序移动三位
"""
# plaincode = input("请输入明文： ")
# for p in plaincode:
#     if ord("a") <= ord(p) <= ord("z"):
#         print(chr(ord("a") + (ord(p) - ord("a") +3 ) % 26), end="")
#     else:
#         print(p,end="")


# 第二种方法：循环
# 向后顺序移动13位
s = "Gur Mra bs Clguba"
d = {}
for c in (65,97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)
print("".join([d.get(c, c) for c in s]))
