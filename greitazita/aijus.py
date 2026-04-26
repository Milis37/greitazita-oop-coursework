from .models import Salon, Expense, Earning, RentExpense, SupplyExpense
from .builder import FinancialReportBuilder
from .file_export import FinanceFileManager
from datetime import datetime
import re

class GreitaZitaAI:
    def __init__(self):
        self.salons = {}  # cache for salons
        self.file_manager = FinanceFileManager()
    
    def process_message(self, salon_id: int, message: str) -> str:
        # Get or create salon (Singleton pattern for DB? optional)
        if salon_id not in self.salons:
            self.salons[salon_id] = Salon(salon_id, f"Salon-{salon_id}")
        
        salon = self.salons[salon_id]
        
        # Parse message for expenses/earnings
        # Example: "Rent 1200€, Haircut service 5000€"
        expenses = self._extract_expenses(message, salon)
        earnings = self._extract_earnings(message, salon)
        
        # Add to salon (composition)
        for exp in expenses:
            salon.add_expense(exp)
        for earn in earnings:
            salon.add_earning(earn)
        
        # Build report using Builder pattern
        builder = FinancialReportBuilder()
        for exp in salon.expenses:
            builder.add_expense(exp)
        for earn in salon.earnings:
            builder.add_earning(earn)
        
        report = builder.add_summary().build()
        
        # Export to file (file I/O requirement)
        self.file_manager.save_report_txt(report, f"salon_{salon_id}_report.txt")
        
        return report
    
    def _extract_expenses(self, message: str, salon: Salon) -> list:
        expenses = []
        # Simple regex parsing (improve as needed)
        rent_match = re.search(r'rent\s+(\d+)', message.lower())
        if rent_match:
            amount = float(rent_match.group(1))
            expenses.append(RentExpense(amount, datetime.now(), "Main Street"))
        
        supply_match = re.search(r'supplies?\s+(\d+)', message.lower())
        if supply_match:
            amount = float(supply_match.group(1))
            expenses.append(SupplyExpense(amount, datetime.now(), "Beauty Supply Co."))
        
        return expenses
    
    def _extract_earnings(self, message: str, salon: Salon) -> list:
        earnings = []
        earn_match = re.search(r'(haircut|service|earning)s?\s+(\d+)', message.lower())
        if earn_match:
            amount = float(earn_match.group(2))
            earnings.append(Earning(amount, earn_match.group(1), datetime.now()))
        return earnings
