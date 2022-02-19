def add(j_l):
    n_j =input("加入菜單")
    if n_j in j_l:
        print("you have already add it!")
    else:
        j_l.append(n_j)
        print("you add it in suceessful!")
    return j_l

def dp(j_l):
    for dp in range(len(j_l)):
        print(j_l[dp])
    return j_l

def rm (j_l):
    d_j =input("what you want to remove?")
    if d_j in j_l:
        j_l.remove(d_j)
        print("you del it in suceessful!")
    else:
        print("I can not find what you want you del")
    return j_l

l = []
sl = [add , dp , rm]
while True:    
    print("1加入物品")
    print("2顯示所有物品")
    print("3刪除物品")
    print("4離開")
    s = int(input("請輸入代號:"))
    if s == 4:
        a = input ('you really want to exit?Y/N')
        if a == "y":
            break
        else:
            print('-----------------')
            continue           
    else :
        print('!!!lishilapasa!!!')
        print('-----------------')
        continue
    l = sl[s-1](l)