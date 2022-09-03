from enum import Enum


class ClientType(Enum):
    REGULAR = 1
    PREMIUM = 2
    VIP = 3


class ClientActions(Enum):
    DEPOSIT = 1
    WITHDRAW = 2
    GET_BALANCE = 3


class BankActions(Enum):
    ADD_ClIENT = 1
    PRINT_ALL = 2
    ACTION_CLIENT = 3
    EXIT = 4
