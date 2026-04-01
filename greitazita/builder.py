from .entities import FinancialRecord, FixedExpense, ProductExpense, ServiceExpense, Earning
from datetime import datetime

class FinancialReportBuilder:
    def __init__(self, salon_name: str):
        self.record = FinancialRecord(salon_name)
        self.period_start = datetime(2026, 1, 1)
        self.period_end = datetime(2026, 3, 31)

    def add_expense(self, amount: float, description: str, category: str = "Fixed Cost"):
        if category == "Product":
            self.record.add_expense(ProductExpense(amount, description))
        elif category == "Service":
            self.record.add_expense(ServiceExpense(amount, description))
        else:
            self.record.add_expense(FixedExpense(amount, description))
        return self

    def add_earning(self, amount: float, source: str):
        self.record.add_earning(Earning(amount, source))
        return self

    def set_period(self, start, end):
        self.period_start = start
        self.period_end = end
        return self

    def build(self):
        return self.record
