from abc import ABC, abstractmethod
from typing import List

class Expense(ABC):
    def __init__(self, amount: float, description: str):
        if amount < 0:
            raise ValueError("Expense amount cannot be negative")
        self._amount = amount
        self._description = description

    @property
    def amount(self):
        return self._amount

    @abstractmethod
    def get_category(self) -> str:
        pass

class FixedExpense(Expense):
    def get_category(self) -> str:
        return "Fixed Cost"

class ProductExpense(Expense):
    def get_category(self) -> str:
        return "Product"

class ServiceExpense(Expense):
    def get_category(self) -> str:
        return "Service"

class Earning:
    def __init__(self, amount: float, source: str):
        if amount < 0:
            raise ValueError("Earning cannot be negative")
        self.amount = amount
        self.source = source

class FinancialRecord:
    def __init__(self, salon_name: str):
        self.salon_name = salon_name
        self.expenses: List[Expense] = []
        self.earnings: List[Earning] = []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)  # composition

    def add_earning(self, earning: Earning):
        self.earnings.append(earning)  # aggregation

    def total_expenses(self) -> float:
        return sum(e.amount for e in self.expenses)

    def total_earnings(self) -> float:
        return sum(e.amount for e in self.earnings)

    def profit_loss(self) -> float:
        return self.total_earnings() - self.total_expenses()
