class User:
    def __init__(self, first_name, sekond_name, account_balance):
        self.first_name = first_name
        self.sekond_name = sekond_name
        self.account_balance = account_balance

    def get_information(self):
        return 'клиент :' + self.first_name + ' ' + self.sekond_name +' ' +'Баланс: ' + str(self.account_balance) + 'pyb'


class Database:
    def __init__(self):
        self.db = []

    def add_user(self,first_name, sekond_name, account_balance):
        user = User(first_name, sekond_name, account_balance)
        return self.db.append(user)

    def find_users(self, first_name):
        info_list = []
        for user in self.db:
            if user.first_name == first_name:
                info_list.append(user.get_information())
        return info_list


users_db = Database()


def rezult():
    baton = int(input("Нажмите 1, если хотите добавить клиента в базу, нажмите 2, если хотите вывести информацию о клиенте :"))
    if baton == 1:
        users_db.add_user(input('Введите Имя: '),input('ведите фамилию: '), int(input('Введите баланс: ')))
        rezult()
    elif baton == 2:
        print(users_db.find_users(input('Введите Имя: ')))
        rezult()
    else:
        print('Число должно быть 1 либо 2')
        rezult()


rezult()
