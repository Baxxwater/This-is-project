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
        damage = random.randint(5, 20)
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


sta = [1, 50, 100]
eve_list = [updata_HP, updata_gold, battle]

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
        break
    else:
        continue