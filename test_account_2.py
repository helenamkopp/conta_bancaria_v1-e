from account import CheckingAccount, Client

client_1 = Client("Helena", "Maria", "555.555.444-85")

def method1():
    print("starting method 1")
    method2()
    print("end method 1")


def method2():
    print("starting method 2")
    ca = CheckingAccount("1543-6", client_1)

    for i in range(1, 15):
        try:
            ca.deposit(i + 1000)
            print(ca.balance)
            if i == 5:
                ca = None
        except:
            print("error")

    print("end method 2")

if __name__ == "__main__":
    print("starting main")
    method1()
    print("end main")