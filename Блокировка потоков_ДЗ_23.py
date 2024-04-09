import random
from collections import defaultdict
import threading
from threading import Thread


class BankAccount (Thread):

    def __init__(self, account, amount, deposit, withdraw, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account = account
        self.amount = amount
        self.deposit = deposit
        self.withdraw = withdraw
        print(deposit)
        print(withdraw)



def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)
        account = BankAccount()


        global a, b
        print(f'{_}: deposit_task wait lock_A', flush=True)
        with lock_A:
            print(f'{_}: deposit_task take lock_A', flush=True)
            a += 1
            print(f'{_}: deposit_task wait lock_B', flush=True)
            with lock_B:
                print(f'{_}: deposit_task take lock_B', flush=True)
                b -= 1

def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)
        account = BankAccount()


        global a, b
        print(f'{_}: withdraw_task wait lock_B', flush=True)
        with lock_A:
            print(f'{_}: withdraw_task take lock_B', flush=True)
            b -= 1
            print(f'{_}: withdraw_task wait lock_A', flush=True)
            with lock_B:
                print(f'{_}: withdraw_task take lock_A', flush=True)
                a += 1

a = 100
b = 150
lock_A = threading.RLock()
lock_B = threading.RLock()
account = 5

deposit_thread = threading.Thread(target=deposit_task, args=(account, 100))
withdraw_thread = threading.Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

print(a, b)