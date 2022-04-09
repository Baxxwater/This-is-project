from distutils.ccompiler import show_compilers
import random


def updata_HP(status: list):
    get_HP = random.randint(1, 5)
    status[1] += get_HP
    print("rec_HP:{} you_HP:{}".format(get_HP, status[1]))
    return status


def updata_gold(status: list):
    get_gold = random.randint(15, 40)
    status[2] += get_gold
    print("icom_gold{} you_gold{}".format(get_gold, status[2]))
    return status


def battle(status: list):
    enemy_HP = random.randint(10, 30)
    print("enemy_HP : {}".format(enemy_HP))

    while True:
        while True:
            move = input('use spacial attack?y/n:')
            if (move == 'y' and status[3] >= 5):
                damage = random.randint(15, 35) + status[4]
                status[3] -= 5
                break
            elif move == 'n':
                damage = random.randint(5, 20) + status[4]
                break

        print("you hit {}".format(damage))
        enemy_HP -= damage
        if enemy_HP < 1:
            print("you win")
            status[2] += random.randint(10, 50)
            return status
        else:
            print("enemy bit you")
            enemy_hurt = random.randint(2, 5)
            status[1] -= enemy_hurt
            print("you got {} dmg , you still have {} ".format(
                enemy_hurt, status[1]))
            if status[1] < 1:
                print("YOU DIE")
                status[0] = 0
                return status


def shop(status: list):
    rec_HP = 25
    rec_MP = 50
    buy_weap = 1000
    while True:
        if status[2] >= buy_weap:
            recive = input(
                'what do you wnat to buy?:1.recHP 2.rec_MP 3.buy_weapen or quit(q) ?'
            )
            if recive == "1":
                status[2] -= rec_HP
                status[1] += random.randint(10, 30)
                break
            elif recive == '2':
                status[2] -= rec_MP
                status[3] += random.randint(5, 10)
                break
            elif recive == '3':
                status[2] -= buy_weap
                status[4] += random.randint(10, 100)
                break
            elif recive == 'q':
                break
        elif status[2] >= rec_MP:
            recive = input(
                'what do you wnat to buy?:1.recHP 2.rec_MP or quit(q) ?')
            if recive == "1":
                status[2] -= rec_HP
                status[1] += random.randint(10, 30)
                break
            elif recive == '2':
                status[2] -= rec_MP
                status[3] += random.randint(5, 10)
                break
            elif recive == 'q':
                break
        elif status[2] >= rec_HP:
            recive = input('what do you wnat to buy?:1.recHP or quit(q) ?')
            if recive == "1":
                status[2] -= rec_HP
                status[1] += random.randint(10, 30)
                break
            elif recive == 'q':
                break
    return status


def save(status: list):
    saving = "20220409/my laoding.txt"
    f = open(saving, 'w')
    for i in status:
        f.write(str(i) + '\n')
    f.close()


def load(status: list):
    loading = "20220409/my laoding.txt"
    f = open(loading, 'r')
    status = []
    for line in f:
        status.append(int(line))
    f.close()
    return status


sta = load([])  #1.weather live 2.HP 3.gold 4.MP 5.+damage

eve_list = [updata_HP, updata_gold, battle, shop]

print(sta)

while True:
    put = input("which c'keep'q'quit':")
    if put == 'c':
        sta = eve_list[random.randint(0, len(eve_list) - 1)](sta)
        if sta[0] == 0:
            print('YOU DIE')
            break
        print("status = {}".format(sta))
    elif put == "q":
        print('next time')
        save(sta)
        break
    else:
        continue
