from typing import List
from datetime import datetime
from .modelis import Expense, Earning   # jei klaida - pakeisk į .entities

class FinancialReportBuilder:
    """Builder dizaino šablonas ataskaitoms (OOP reikalavimas)"""

    def __init__(self, salon_name: str = "Grožio Salonas"):
        self._report_lines = []
        self._total_expenses = 0.0
        self._total_earnings = 0.0
        self.salon_name = salon_name

    def add_expense(self, expense: Expense) -> 'FinancialReportBuilder':
        self._report_lines.append(f"  ❌ {expense.get_description()}")
        self._total_expenses += expense.get_amount()
        return self

    def add_earning(self, earning: Earning) -> 'FinancialReportBuilder':
        self._report_lines.append(f"  ✅ {earning.get_description()}")
        self._total_earnings += earning.get_amount()
        return self

    def add_summary(self) -> 'FinancialReportBuilder':
        profit = self._total_earnings - self._total_expenses
        current_month = datetime.now().strftime("%Y %B")

        self._report_lines.append("\n" + "=" * 60)
        self._report_lines.append(f"📊 MĖNESIO ATASKAITA – {self.salon_name}")
        self._report_lines.append(f"   Laikotarpis: {current_month}")
        self._report_lines.append("=" * 60)

        self._report_lines.append(f"\n💰 PAJAMOS:          {self._total_earnings:.2f} €")
        self._report_lines.append(f"💸 IŠLAIDOS:         {self._total_expenses:.2f} €")
        self._report_lines.append(f"\n📈 **GRYNASIS PELNAS: {profit:+.2f} €**")

        if profit > 1000:
            self._report_lines.append("   🎉 Puikus rezultatas! Sveikiname!")
        elif profit > 0:
            self._report_lines.append("   📈 Teigiamas pelnas, bet gali būti geriau.")
        else:
            self._report_lines.append("   ❌ Nuostolis. Rekomenduojame peržiūrėti išlaidas.")

        return self

    def build(self) -> str:
        return "\n".join(self._report_lines)
