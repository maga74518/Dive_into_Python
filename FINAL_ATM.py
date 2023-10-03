from time import sleep
from datetime import datetime as dt


def wait_3_second():
    for i in range(3):
        print('.', end='')
        sleep(1)
    print()


class BankCard:
    attempts = 2
    operations_history = []

    def __init__(self):
        self.__pin = '123'
        self.__balance = 10000

    def check_pin(self, entered_pin):
        if self.attempts > 0:
            if self.__pin == entered_pin:
                self.attempts = 2
                wait_3_second()
                print('\nДоступ разрешен!')
                sleep(2)
                return self.__balance
            else:
                self.attempts -= 1
                wait_3_second()
                print(f'\nВы ввели не верный код. Осталось {self.attempts + 1} попыток.')
                return self.check_pin(input('Введите код повторно: '))
        elif self.attempts == 0:
            wait_3_second()
            print('Ваша карта заблокирована! Введен не правильный пароль более 3х раз.')
            return False


class ATM(BankCard):

    def __init__(self, balance):
        self.__balance = balance

    def find_out_balance(self):
        self.operations_history.append(f'{dt.now()}: Проверка баланса')
        return f'Ваш баланс: {self.__balance}р.'

    def withdraw(self, money):
        if money > self.__balance:
            wait_3_second()
            print('Недостаточно средств на счете!')
            self.operations_history.append(f'{dt.now()}: Отказ в выдаче наличных на сумму {money}р.')
            return False
        if 0 < money < self.__balance:
            self.__balance -= money
            self.operations_history.append(f'{dt.now()}: Выдача наличных на сумму {money}р.')
            print('\nВыдача наличных. Подождите.')
            wait_3_second()
            return print(f'Успешно! Вы сняли со счета {money} р.')

    def add_money(self, money):
        if money > 0:
            self.operations_history.append(f'{dt.now()}: Внесено {money}р.')
            print('Пожалуйста подождите! Деньги пересчитываются')
            wait_3_second()
            self.__balance += money
            print('\nУспешно! Деньги зачислены на ваш счет!\n')
            return sleep(2)

    def operations_history_chek(self):
        if len(self.operations_history) == 0:
            wait_3_second()
            return print('История операций чиста')
        wait_3_second()
        return print(self.operations_history)


def operations():
    match int(input('1: Снять\n2: Внести\n3: Баланс\n4: История операций\n5: Выход\nВыберите номер операцию: ')):
        case 1:
            b.withdraw(int(input('Введите сумму которую хотите снять: ')))

            if int(input('\n1: Продолжить операции с картой\n2: Выход\nВыберите действие : ') + '\n') == 2:
                return
            else:
                operations()
        case 2:
            b.add_money(int(input('Внесите сумму в банкомат: ') + '\n'))
            if int(input('\n1: Продолжить операции с картой\n2: Выход\nВыберите действие : ') + '\n') == 2:
                return
            else:
                operations()
        case 3:
            print('\n' + b.find_out_balance())
            sleep(2)
            if int(input('\n1: Продолжить операции с картой\n2: Выход\nВыберите действие : ') + '\n') == 2:
                return
            else:
                operations()
        case 4:
            b.operations_history_chek()
            if int(input('\n1: Продолжить операции с картой\n2: Выход\nВыберите действие : ') + '\n') == 2:
                return
            else:
                operations()
        case 5:
            return print('Досвидания!')
        case _:
            print('\nВведена неподдерживаемая команда! Выберите операцию из списка\n')
            sleep(2)
            operations()


bank_card = BankCard()
b = ATM(bank_card.check_pin(input("Введите PIN-код: ")))
operations()

#pin - 123



