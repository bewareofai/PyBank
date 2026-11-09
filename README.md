# PyBank

A small console banking system written in Python. It is a learning project that ties together object-oriented programming, error handling, iterators, decorators and JSON storage.

## Features

- **Account types:** basic, savings (with interest) and credit (with an overdraft limit), built on inheritance and polymorphism
- **Bank operations:** deposit, withdraw and transfer between accounts
- **Atomic transfers:** if the second half of a transfer fails, the money is returned to the sender
- **Custom exception hierarchy:** `BankError` with account, operation and storage branches
- **Transaction log:** a custom iterator (`LogIterator`) and a generator (`by_kind`) for filtering records
- **Logging decorator:** `log_operation` reports the result of every bank operation
- **JSON storage:** save the bank to a file and load accounts back with `to_dict()` / `from_dict()`

## Project structure

```
PyBank/
    main.py              # demo scenario
    pybank/
        __init__.py      # public API and VERSION
        accounts.py      # Account, SavingsAccount, CreditAccount
        bank.py          # Bank class
        exceptions.py    # exception hierarchy
        transactions.py  # Transaction, TransactionLog, LogIterator
        utils.py         # log_operation decorator
        storage.py       # save_bank / load_accounts
```

## Requirements

Python 3.12 or newer. No third-party packages are needed.

## Usage

Run the demo scenario from the project root:

```
python main.py
```

Or use the package in your own code:

```python
from pybank import Bank, Account, SavingsAccount

bank = Bank("PyBank")
bank.open_account(Account("Alice", 5000))
bank.open_account(SavingsAccount("Bob", 20000, 5))

bank.deposit("ACC-001", 1500)
bank.transfer("ACC-001", "ACC-002", 2000)
print(bank.total)
```

## What I practiced

Classes and inheritance, `@property`, `@classmethod`, `@staticmethod`, magic methods, custom exceptions with `raise ... from`, iterators and generators, decorators, working with files and JSON, and packaging with `__init__.py

Author: Tima Kurenkov

GitHub:  bewareofai            
