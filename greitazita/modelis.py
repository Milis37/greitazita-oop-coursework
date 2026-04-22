from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

# ABSTRACTION
class FinancialRecord(ABC):
    @abstractmethod
    def get_amount(self) -> float:
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        pass

# ENCAPSULATION (private _amount, getters/setters)
class Expense(FinancialRecord):
    def __init__(self, amount: float, category: str, date: datetime):
        self._amount = amount          # private
        self._category = category
        self._date = date
    
    def get_amount(self) -> float:     # getter
        return self._amount
    
    def get_description(self) -> str:
        return f"Expense: {self._category} - {self._amount}€"
    
    def set_amount(self, amount: float):  # setter
        if amount > 0:
            self._amount = amount

# INHERITANCE
class RentExpense(Expense):
    def __init__(self, amount: float, date: datetime, location: str):
        super().__init__(amount, "Rent", date)
        self.location = location
    
    def get_description(self) -> str:    # POLYMORPHISM
        return f"🏢 Rent at {self.location}: {self._amount}€"

class SupplyExpense(Expense):
    def __init__(self, amount: float, date: datetime, supplier: str):
        super().__init__(amount, "Supplies", date)
        self.supplier = supplier

class Earning(FinancialRecord):
    def __init__(self, amount: float, service: str, date: datetime):
        self._amount = amount
        self._service = service
        self._date = date
    
    def get_amount(self) -> float:
        return self._amount
    
    def get_description(self) -> str:
        return f"💰 {self._service}: +{self._amount}€"

# COMPOSITION/AGGREGATION
class Salon:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.expenses: List[Expense] = []    # aggregation
        self.earnings: List[Earning] = []    # aggregation
    
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)
    
    def add_earning(self, earning: Earning):
        self.earnings.append(earning)
    
    def calculate_profit(self) -> float:
        total_expenses = sum(e.get_amount() for e in self.expenses)
        total_earnings = sum(e.get_amount() for e in self.earnings)
        return total_earnings - total_expenses
