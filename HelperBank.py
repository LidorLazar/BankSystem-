from CustomerClass import Customer, Vip, Premium
def read_file():
    with open('Customer.txt', 'r') as cf:  # cf = customer file
        file = cf.readlines()
    return file


def write_regular_client():
    name = input('name :')
    age = int(input('age :'))
    id = input('id :')
    salary = int(input('salary in dollar:'))
    level = input('select level for customer R , V ,P :')
    regular = (Customer(name, age, id, level, salary))
    with open('Customer.txt', 'a') as af:  # af = add file
        af.write(str(regular))


def write_vip_client():
    name = input('name :')
    age = int(input('age :'))
    id = input('id :')
    salary = int(input('salary in dollar:'))
    level = input('select level for customer R , V ,P :')
    vip = (Vip(name, age, id, level, salary))
    with open('Customer.txt', 'a') as af:  # af = add file
        af.write(str(vip))


def write_premium_client():
    name = input('name :')
    age = int(input('age :'))
    id = input('id :')
    salary = int(input('salary in dollar:'))
    level = input('select level for customer R , V ,P :')
    premium = (Premium(name, age, id, level, salary))
    with open('Customer.txt', 'a') as af:  # af = add file
        af.write(str(premium))


def search_client():
    check_id = input('Please write the id client : ')
    for id in read_file():
        if check_id == id.split()[2]:
            return 'The id exits in bank '


def deposit_money():
    des_money = int(input('How much you want deposit ? '))
    check_id = input('Please write the id client : ')
    with open('Customer.txt', 'r') as f:
        file = f.readlines()
        for i in file:
            if check_id == i.split()[2]:
                new_balance = (int(i.split()[3]) + des_money)
                with open('Customer.txt', 'r+') as f:
                    balance_to_file = i.replace(i.split()[3], str(new_balance))
                    f.write(balance_to_file)


def withdraw_money():
    check_id = input('Please write the id client : ')
    with open('Customer.txt', 'r') as f:
        file = f.readlines()
        for i in file:
            if check_id == i.split()[2]:
                get_money = int(input('How much you want withdraw ? '))
                new_balance = (int(i.split()[3])) - get_money
                if i.split()[4] == 'p'.upper():
                    if new_balance >= 0:
                        with open('Customer.txt', 'r+') as f:
                            balance_to_file = i.replace(i.split()[3], str(new_balance))
                            f.write(balance_to_file)
                    else:
                        return "Can't get into the minus"
                    if i.split()[4] == 'v'.upper():
                        if new_balance >= -500:
                            with open('Customer.txt', 'r+') as f:
                                balance_to_file = i.replace(i.split()[3], str(new_balance))
                                f.write(balance_to_file)
                        else:
                            return "Can't get into the minus"
                        if i.split()[4] == 'p'.upper():
                            if new_balance >= -1000:
                                with open('Customer.txt', 'r+') as f:
                                    balance_to_file = i.replace(i.split()[3], str(new_balance))
                                    f.write(balance_to_file)
                            else:
                                return "Can't get into the minus"


def show_balance():
    user_id = input('Please write the id client : ')
    with open('Customer.txt', 'r') as f:
        file = f.readlines()
        for i in file:
            if i.split()[2] == user_id:
                return i.split()[3]

