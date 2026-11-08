from pybank import Bank, Account, SavingsAccount, CreditAccount, VERSION, save_bank, load_accounts, AccountNotFound, AccountError, InvalidAmount, InsufficientFunds, OperationError, LimitExceeded, StorageError, BankError, AccountBlocked
Account.reset_counter()
print(f"PyBank v{VERSION}")
bank = Bank("PyBank")
bank.open_account(Account("Оксана", 5000))
bank.open_account((SavingsAccount("Ігор", 20000, 5)))
bank.open_account(CreditAccount("Тарас", 0, 10000))
print(len(bank))
print(f"{bank.total:.2f}")
for account in bank:
    print(account)
bank.deposit("ACC-001", 1500)
bank.transfer("ACC-001", "ACC-002", 2000)
bank.withdraw("ACC-003", 3500)
print(f"{bank.total:.2f}")
a = ("ACC-001", "ACC-002", 60000)
b = ("ACC-001", "ACC-077", 100)
c = ("ACC-001", "ACC-002", 10000)
roster = [a,b,c]
for source, target, amount in roster:
    try:
        bank.transfer(source, target, amount)
    except LimitExceeded as e:
        print("Перевищено ліміт:", e.limit)
    except AccountNotFound as e:
        print("Рахунок не знайдено:", e.number)
    except InsufficientFunds as e:
        print("Не вистачає:", f"{e.shortage:.2f}")
    except BankError as e:
        print("Інша помилка банку:", e)
print(f"{bank["ACC-002"].add_interest():.2f}")
ranked = sorted(bank, reverse=True)
for acc in ranked:
    print(acc)
print(f"{bank.total:.2f}")
for t in bank._log:
    print(t)
print([t.id for t in bank._log.by_kind("TRANSFER")])
save_bank(bank, "bank.json")
loaded = load_accounts("bank.json")
print(loaded[0] == bank["ACC-001"])
print([type(a).__name__ for a in loaded])
try:
    load_accounts("no_such.json")
except StorageError as e:
    print(e, type(e.__cause__).__name__)
