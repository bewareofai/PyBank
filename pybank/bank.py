from .accounts import Account
from .exceptions import AccountNotFound, LimitExceeded, BankError
from .transactions import Transaction, TransactionLog
from .utils import log_operation
TRANSFER_LIMIT = 50000.0
class Bank:
    def __init__(self, name):
        self.name = name
        self._accounts = []
        self._log = TransactionLog()
    @log_operation
    def deposit(self, number, amount):
        acc = self.find(number)
        new_balance = acc.deposit(amount)
        self._log.add(Transaction("DEPOSIT", amount, number))
        return new_balance
    @log_operation
    def withdraw(self, number, amount):
        acc = self.find(number)
        new_balance = acc.withdraw(amount)
        self._log.add(Transaction("WITHDRAW", amount, number))
        return new_balance
    @log_operation
    def transfer(self, source, target, amount):
        if amount > TRANSFER_LIMIT:
            raise LimitExceeded(amount, TRANSFER_LIMIT)
        src = self.find(source)
        dst = self.find(target)
        src.withdraw(amount)
        try:
            dst.deposit(amount)
        except BankError:
            src.deposit(amount)
            raise
        self._log.add(Transaction("TRANSFER", amount, source, target))
        return src.balance
    def open_account(self, account):
        self._accounts.append(account)
    def find(self, number):
        for acc in self._accounts:
            if acc._number == number:
                return acc
        raise AccountNotFound(number)
    @property
    def total(self):
        money = sum(acc.balance for acc in self._accounts)
        return money
    def __len__(self):
        return len(self._accounts)
    def __iter__(self):
        return iter(self._accounts)
    def __contains__(self, item):
        if isinstance(item, Account):
            return item in self._accounts
        try:
            self.find(item)
            return True
        except AccountNotFound:
            return False
    def __getitem__(self, item):
        return self.find(item)
    def __repr__(self):
        return f"Bank('{self.name}', рахунків: {len(self)})"








