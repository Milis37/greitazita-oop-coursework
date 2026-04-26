import re
from datetime import datetime

# Teisingi importai pagal tavo GitHub struktūrą
from .modelis import Salon, RentExpense, SupplyExpense, Earning
from .builderis import FinancialReportBuilder
from .file_exportas import FinanceFileManager
from .database import DatabaseManager


class GreitaZitaAI:
    def __init__(self):
        self.salons = {}
        self.file_manager = FinanceFileManager()
        self.db_manager = DatabaseManager()

    def process_message(self, salon_id: int, message: str) -> str:
        """
        Pagrindinis AI metodas. Apdoroja žinutę iš frontend, išsaugo duomenis
        ir grąžina ataskaitą (naudojant Builder).
        """
        # Sukuriame salono objektą jei dar nėra
        if salon_id not in self.salons:
            self.salons[salon_id] = Salon(salon_id, f"Salon-{salon_id}")
        
        salon = self.salons[salon_id]

        # Ištraukiame pajamas ir išlaidas iš žinutės
        expenses = self._extract_expenses(message)
        earnings = self._extract_earnings(message)

        # Pridedame prie salono
        for exp in expenses:
            salon.add_expense(exp)
        for earn in earnings:
            salon.add_earning(earn)

        # Generuojame ataskaitą per Builder
        builder = FinancialReportBuilder()
        for exp in salon.expenses:
            builder.add_expense(exp)
        for earn in salon.earnings:
            builder.add_earning(earn)

        report = builder.add_summary().build()

        # Išsaugome ataskaitą į txt failą
        file_name = f"salon_{salon_id}_report.txt"
        self.file_manager.save_report_txt(report, file_name)

        return report

    def _extract_expenses(self, message: str):
        """Regex pagalba ištraukia išlaidas (veikia su frontend duomenimis)"""
        expenses = []
        msg = message.lower()

        # Nuoma
        rent_match = re.search(r'(nuoma|rent)\s*(\d+)', msg)
        if rent_match:
            amount = float(rent_match.group(2))
            expenses.append(RentExpense(amount, datetime.now(), "Pagrindinis Salonas"))

        # Prekės
        supply_match = re.search(r'(prekės|supplies)\s*(\d+)', msg)
        if supply_match:
            amount = float(supply_match.group(2))
            expenses.append(SupplyExpense(amount, datetime.now(), "Grožio Prekės"))

        return expenses

    def _extract_earnings(self, message: str):
        """Regex pagalba ištraukia pajamas"""
        earnings = []
        msg = message.lower()

        earn_pattern = r'(kirpimas|paslaugos|earning|income)\s*(\d+)'
        matches = re.findall(earn_pattern, msg)

        for service, amount_str in matches:
            earnings.append(Earning(float(amount_str), service.capitalize(), datetime.now()))

        return earnings
