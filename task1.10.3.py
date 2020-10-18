
class Pets_house:

    def __init__(self, first_name, sekond_name, patronomik, account_balance):
        self.first_name = first_name
        self.sekond_name = sekond_name
        self.patronomik = patronomik
        self.account_balance = account_balance

    def database(self):
        database_1 =[]
        database_1.append(self.first_name), database_1.append(self.sekond_name), database_1.append(
            self.patronomik), database_1.append(self.account_balance)
        return database_1

    def information_client(self):

        return str(Pets_house.database() + ' ' + Pets_house.database(self.sekond_name))

    def information_client_balans(self):
        return str(Pets_house.database(self.account_balance)[3])

while True:
    chosee_a_number = int(
        input("Нажмите 1, если хотите добавить клиента в базу, нажмите 2, если хотите вывести информацию о клиенте : "))

    if chosee_a_number == 1:
        first_name = input('first_name : ')
        sekond_name = input('sekond_name : ')
        patronomik = input('patronomik : ')
        account_balance = int(input('account_balance : '))
        pet_house = Pets_house(first_name, sekond_name, patronomik, account_balance)
        print(pet_house.database())
        continue
    elif chosee_a_number == 2:

        print('клиент : ', Pets_house.information_client() + ' ' + 'баланс : ', Pets_house.information_client_balans())
    else:
        print('веденое число не верное')
        continue

    break