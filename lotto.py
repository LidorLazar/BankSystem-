import random


def loto():
    number_list = []
    while 6 >= len(number_list):
        ball = random.randint(1, 15)
        if ball not in number_list:
            number_list.append(ball)
    print(number_list)
    return random.sample(range(1, 15), 7)


print(loto())
