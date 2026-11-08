import json
from .accounts import Account, SavingsAccount, CreditAccount
from .exceptions import StorageError
classes = {"Account": Account,
 "SavingsAccount": SavingsAccount,
 "CreditAccount": CreditAccount,}
def save_bank(bank, path):
    accounts = [acc.to_dict() for acc in bank]
    dictionary = {"name": bank.name,
                  "accounts": accounts}
    with open(path, "w", encoding="utf-8") as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=2)
    return len(bank)
def load_accounts(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError as error:
        raise StorageError(f"Файл {path} не знайдено") from error
    except json.decoder.JSONDecodeError as error:
        raise StorageError(f"Файл {path} пошкоджено") from error
    result = []
    for d in data["accounts"]:
        acc = classes[d["type"]].from_dict(d)
        result.append(acc)
    return result




