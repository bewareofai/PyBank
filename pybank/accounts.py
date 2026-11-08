from .exceptions import InvalidAmount, InsufficientFunds, AccountBlocked
class Account:
    _counter = 0
    def __init__(self, owner, balance=0 ):
        Account._counter += 1
        self._owner = owner
        self._balance = balance
        self._number = f"ACC-{Account._counter:03d}"
        self.is_blocked = False
    def to_dict(self):
        return {"type": type(self).__name__, "owner": self._owner, "balance": self._balance, "number": self._number, "is_blocked": self.is_blocked}
    @classmethod
    def from_dict(cls, data):
        acc = cls(data["owner"], data["balance"])
        acc._number = data["number"]
        acc.is_blocked = data["is_blocked"]
        return acc
    @classmethod
    def reset_counter(cls):
        cls._counter = 0
    @property
    def balance(self):
        balance = round(self._balance, 2)
        return balance
    @property
    def available(self):
        return self.balance
    @property
    def kind(self):
        return "Базовий"
    @staticmethod
    def validate_amount(amount):
        if not isinstance(amount, (int, float)):
            raise InvalidAmount(amount)
        if amount < 0:
            raise InvalidAmount(amount)
    def deposit(self, amount):
        Account.validate_amount(amount)
        if self.is_blocked:
            raise AccountBlocked(self._number)
        self._balance += amount
        return self.balance
    def withdraw(self, amount):
        Account.validate_amount(amount)
        if self.is_blocked:
            raise AccountBlocked(self._number)
        if amount > self.available:
            raise InsufficientFunds(self._number, self.available, amount)
        self._balance -= amount
        return self.balance

    def __str__(self):
        return f"{self._number} | {self._owner} | {self.kind} | {self.balance:.2f} грн"

    def __repr__(self):
        return f"Account('{self._number}', {self.balance:.2f})"

    def __eq__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self._number == other._number

    def __lt__(self, other):
        if not isinstance(other, Account):
            return NotImplemented
        return self.balance < other.balance
class SavingsAccount(Account):
    def __init__(self, owner, balance=0, rate=5.0):
        super().__init__(owner, balance)
        self._rate = rate
    def to_dict(self):
        data = super().to_dict()
        data["rate"] = self._rate
        return data
    @classmethod
    def from_dict(cls, data):
        acc = super().from_dict(data)
        acc._rate = data["rate"]
        return acc
    @property
    def kind(self):
        return "Ощадний"
    def add_interest(self):
        interest = self.balance/100 * self._rate
        self.deposit(interest)
        return interest
class CreditAccount(Account):
    def __init__(self, owner, balance=0, limit = 10000):
        super().__init__(owner, balance)
        self._limit = limit
    def to_dict(self):
        data = super().to_dict()
        data["limit"] = self._limit
        return data
    @classmethod
    def from_dict(cls, data):
        acc = super().from_dict(data)
        acc._limit = data["limit"]
        return acc
    @property
    def kind(self):
        return "Кредитний"
    @property
    def available(self):
        return self.balance +  self._limit







