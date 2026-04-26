from typing import List
from .modelis import Expense, Earning

class FinancialReportBuilder:
    """Builder pattern for constructing financial reports"""
    
    def __init__(self):
        self._report_lines = []
        self._total_expenses = 0.0
        self._total_earnings = 0.0
    
    def add_expense(self, expense: Expense) -> 'FinancialReportBuilder':
        self._report_lines.append(f"  ❌ {expense.get_description()}")
        self._total_expenses += expense.get_amount()
        return self  # fluent interface
    
    def add_earning(self, earning: Earning) -> 'FinancialReportBuilder':
        self._report_lines.append(f"  ✅ {earning.get_description()}")
        self._total_earnings += earning.get_amount()
        return self
    
    def add_summary(self) -> 'FinancialReportBuilder':
        profit = self._total_earnings - self._total_expenses
        self._report_lines.append("\n" + "="*40)
        self._report_lines.append(f"📊 SUMMARY:")
        self._report_lines.append(f"   Total Earnings: {self._total_earnings}€")
        self._report_lines.append(f"   Total Expenses: {self._total_expenses}€")
        self._report_lines.append(f"   Net Profit: {profit}€")
        
        # AI advice
        if profit < 0:
            self._report_lines.append("   ⚠️ CRITICAL: You're losing money! Reduce expenses.")
        elif profit < 500:
            self._report_lines.append("   📉 Low profit margin. Consider raising prices.")
        else:
            self._report_lines.append("   ✅ Healthy profit! Great job!")
        return self
    
    def build(self) -> str:
        return "\n".join(self._report_lines)
