from ctypes import BigEndianStructure
import random
import turtle  
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
# while True:
#     try:
#         m = int(input('輸入數字:'))
#     except:
#         print("error try again")
#         continue
#     if m > n:
#         print("little")
#         if l > m:
#             l = m
#         print("{}~{}".format(b,l))
#     if m < n:
#         print("big")
#         if b < m: 
#             b = m
#         print("{}~{}".format(b,l))
#     if m == n:
#         print("success")
#         break
l = []
while True:    
    print("1加入物品")
    print("2顯示所有物品")
    print("3離開")
    s = input("請輸入代號:")
    if s == "1":
        l.append(input('物品:'))
        print("..................")
    elif s == "2":
        for a in range(len(l)):
            print(l[a])
        print('..................')   
    elif s == "3":
        print('next time to see')
        print('-----------------')
        break 
    else :
        print('!!!lishilapasa!!!')
        print('-----------------')
        continue