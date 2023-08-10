# Problem 3

def odd(x: int):
    if x % 2 != 0:
        print(x)
    odd(x+1)


# Problem 4

def dek(x: set):
    print(x)
    x.pop()
    if x == set():
        return
    dek(x)


# Problem 5

def spisochec_1(func):
    def inner():
        lol = func()
        return list(set(lol))
    return inner


@spisochec_1
def spisochec():
    from random import randint
    lis = []

    for i in range(100):
        lis.append(randint(10, 50))
    return lis


# Problem 6

def encrypt(func):                     # Здесь происходит шифровка данных
    def inner():
        hello = func()
        log1 = []
        pas1 = []

        for i in hello[0]:                # Сюда бросаем зашифрованные данные
            log1.append(ord(i))
        for i in hello[1]:
            pas1.append(ord(i))

        return [log1, pas1]                # Здесь выводим данные
    return inner


@encrypt
def login():                                   # Ввод логина и пароля
    log = input('Напишите ваш логин - ')
    pas = input("Напишите ваш пароль - ")
    return log, pas