class BankError(Exception):
    """Проблеми з банком"""
class AccountError(BankError):
    """Проблеми з акаунтом"""
class AccountNotFound(AccountError):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Рахунок {number} не знайдено")
class AccountBlocked(AccountError):
    def __init__(self, number):
        self.number = number
        super().__init__(f"Рахунок {number} заблоковано")
class OperationError(BankError):
    """Проблеми з операціями"""
class InvalidAmount(OperationError):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Некоректна сума: {amount!r}")
class InsufficientFunds(OperationError):
    def __init__(self, number, available, required):
        self.number = number
        self.available = available
        self.required = required
        self.shortage = required - available
        super().__init__(f"На вашому рахунку {number} бракує {self.shortage:.2f} грн (баланс - {available}, потрібно - {required})")
class LimitExceeded(OperationError):
    def __init__(self, amount, limit):
        self.amount = amount
        self.limit = limit
        super().__init__(f"Зняття суми {amount:.2f} неможливе, ви вичерпали свій ліміт: {limit:.2f} грн")
class StorageError(BankError):
    """Проблеми зі сховищем"""
