from .accounts import Account

class Transaction:
    _counter = 0
    def __init__(self, kind, amount, sender, recipient = "-"):
        self._amount = amount
        self._kind = kind
        self._sender = sender
        self._recipient = recipient
        Transaction._counter += 1
        self._id = f"T{Transaction._counter:03d}"
    @classmethod
    def reset_counter(cls):
        cls._counter = 0
    def __str__(self):
        return f"  {self._id}  {self._kind}: {self._amount:.2f} грн ({self._sender} -> {self._recipient})"
    def __repr__(self):
        return f"Transaction('{self._id}', {self._amount:.2f})"
    @property
    def kind(self):
        return self._kind
    @property
    def id(self):
        return self._id
class LogIterator:
    def __init__(self, records):
        self._records = records
        self._pos = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._pos == len(self._records):
            raise StopIteration
        item = self._records[self._pos]
        self._pos += 1
        return item
class TransactionLog:
    def __init__(self):
        self._transactions = []
    def add(self, transaction):
        self._transactions.append(transaction)
        return transaction
    def __iter__(self):
        return LogIterator(self._transactions)
    def __len__(self):
        return len(self._transactions)
    def __getitem__(self, index):
        return self._transactions[index]
    @property
    def total_amount(self):
        sum_money = sum(t._amount for t in self._transactions)
        return sum_money
    def by_kind(self, kind):
        for transaction in self._transactions:
            if transaction.kind == kind:
                yield transaction












