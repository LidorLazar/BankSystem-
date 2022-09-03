from HelperBank import *
from EnumForBank import BankActions, ClientType, ClientActions


def menu():
    print(f'Welcome {name_clerk} have a nice day ')
    for action in BankActions:
        print(f'{action.value} -- {action.name}')
    return int(input('Select action : '))


def add_customer():
    for ct in ClientType:
        print(f'{ct.value} -- {ct.name}')
    select_type = (int(input('Select type : ')))
    print('Now we check if id in data of bank')
    search_client()
    if select_type == ClientType.REGULAR.value:write_regular_client()
    if select_type == ClientType.VIP.value:write_vip_client()
    if select_type == ClientType.PREMIUM.value:write_premium_client()


def print_all():
    select_level_client = input('Which level client you want see R / V / P ? ').upper()
    for i in read_file():
        if i.strip('\n').split()[4] == select_level_client:
            print(i.strip('\n'))


def action_in_client():
    for ca in ClientActions:
        print(f'{ca.value} -- {ca.name}')
    action_client = (int(input("Which actions would you like to make ? ")))
    if action_client == ClientActions.WITHDRAW.value:withdraw_money()
    if action_client == ClientActions.DEPOSIT.value:deposit_money()
    if action_client == ClientActions.GET_BALANCE.value:show_balance()


def main():
    opt_clerk = menu()
    while opt_clerk != BankActions.EXIT.value:
        if opt_clerk == BankActions.ADD_ClIENT.value:add_customer()
        if opt_clerk == BankActions.PRINT_ALL.value:print_all()
        if opt_clerk == BankActions.ACTION_CLIENT.value:action_in_client()
        opt_clerk = menu()

    print('Bye Bye')


if __name__ == '__main__':
    name_clerk = input('Please write your name :')
    main()
