from ctypes import BigEndianStructure
import random  
# n = input('請輸入一個數字')
# m = random.randint(1,int(n))
# s = 1
# print(m)
# while s <= m:
    
#     if s < m:
#         s += 1
#     if s == m:
#         print(s)
#         break
n = random.randint(1,100)
l = 100
b = 1
while True:
    try:
        m = int(input('輸入數字:'))
    except:
        print("error try again")
        continue
    if m > n:
        print("little")
        if l > m:
            l = m
        print("{}~{}".format(b,l))
    if m < n:
        print("big")
        if b < m: 
            b = m
        print("{}~{}".format(b,l))
    if m == n:
        print("success")
        break