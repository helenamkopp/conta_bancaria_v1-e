class Client:

    def __init__(self, first, last, cpf):
        self.first = first
        self.last = last
        self.cpf = str(cpf)


class Account:

    def __init__(self, number, client, balance=0, limit=1000.0):
        if not isinstance(client, Client):
            raise TypeError(f"client must be of type Client not {type(client)}")
        self._holder = client
        self._number = str(number)
        self._balance = float(balance)
        self._limit = float(limit)

    def deposit(self, amount):
        self._balance += amount

    def withdraw_money(self, amount):
        if amount > self._balance:
            return False
        else:
            self._balance -= amount

    def bank_statement(self):
        print(f"Acocunt number: {self._number}\n Account balance: {self._balance}")
        return self._balance

    def transfer_to(self, destiny, amount):
        withdrew = self.withdraw_money(amount)
        if withdrew == False:
            return False
        else:
            destiny.deposity(amount)
            return True

    def update(self, tax):
        self._balance += self._balance * tax

    @property
    def balance(self):
        return self._balance


class CheckingAccount(Account):

    def __init__(self, number, client, balance=0, limit=1000.0):
        super().__init__(number, client, balance, limit)

    def deposit(self, amount):
        self._balance += amount - 0.10

    def update(self, tax):
        self._balance += self._balance * tax * 2
