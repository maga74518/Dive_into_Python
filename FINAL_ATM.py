from time import sleep

def wait_3_second():
    for i in range(3):
        print('.', end='')
        sleep(1)
    print()

class ATM:
    def __init__(self, balance):
        self.balance = balance

    def find_out_balance(self):
        return f'Ваш баланс: {self.balance}р.'

    def withdraw(self, money):
        if money > self.balance:
            wait_3_second()
            print('Недостаточно средств на счете!')
            return False
        if 0 < money < self.balance:
            self.balance -= money
            return print(f'Успешно! Вы сняли со счета {money} р.')

    def add_money(self, money):
        if money > 0:
            print('Пожалуйста подождите! Деньги пересчитываются')
            wait_3_second()
            self.balance += money
            print('\nУспешно! Деньги зачислены на ваш счет!\n')
            return sleep(2)
class BankCard:
    attempts = 2

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
                print(f'\nВы ввели не верный код. Осталось {self.attempts+1} попыток.')
                return self.check_pin(input('Введите код повторно: '))
        elif self.attempts == 0:
            wait_3_second()
            print('Ваша карта заблокирована! Введен не правильный пароль более 3х раз.')
            return False

def operations():

    match int(input('1: Снять\n2: Внести\n3: Баланс\n4: Выход\nВыберите номер операцию: ')):
        case 1:
            b.withdraw(int(input('Введите сумму которую хотите снять: ')))
            if int(input('\n1: Продолжить операции с картой\n2: Выход\nВыберите действие : ')+'\n') == 2:
                return
            else:
                operations()
        case 2:
            b.add_money(int(input('Внесите сумму в банкомат: ') + '\n'))
            if int(input('\n1: Продолжить операции с картой\n2: Выход\nВыберите действие : ')+'\n') == 2:
                return
            else:
                operations()
        case 3:
            print('\n'+ b.find_out_balance())
            sleep(2)
            if int(input('\n1: Продолжить операции с картой\n2: Выход\nВыберите действие : ')+'\n') == 2:
                return
            else:
                operations()
        case 4:
            return print('Досвидания!')
        case _:
            print('\nВведена неподдерживаемая команда! Выберите операцию из списка\n')
            sleep(2)
            operations()

bank_card = BankCard()
entered_pin = input("Введите PIN-код: ")
b = ATM(bank_card.check_pin(entered_pin))
operations()



