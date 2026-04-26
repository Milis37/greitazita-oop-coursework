import re
from datetime import datetime

# Pataisyti importai – naudojame tikrus egzistuojančius failus tavo projekte
from .modelis import Salon, RentExpense, SupplyExpense, Earning
from .builderis import FinancialReportBuilder
from .file_exportas import FinanceFileManager
from .database import DatabaseManager


class GreitaZitaAI:
    def __init__(self):
        self.salons = {}
        self.file_manager = FinanceFileManager()
        self.db_manager = DatabaseManager()  # Singleton DB valdytojas

    def process_message(self, salon_id: int, message: str) -> str:
        """
        Pagrindinis metodas, kuris apdoroja žinutę, išsaugo duomenis 
        ir sugeneruoja ataskaitą naudojant Builder šabloną.
        """
        # 1. Gauname arba sukuriame salono objektą (Agregacija)
        if salon_id not in self.salons:
            self.salons[salon_id] = Salon(salon_id, f"Salon-{salon_id}")
        
        salon = self.salons[salon_id]

        # 2. Ištraukiame duomenis iš teksto (Regex) – veikia ir su frontend siunčiamais pranešimais
        expenses = self._extract_expenses(message)
        earnings = self._extract_earnings(message)

        # 3. Pridedame prie salono objekto
        for exp in expenses:
            salon.add_expense(exp)
        
        for earn in earnings:
            salon.add_earning(earn)

        # 4. Generuojame ataskaitą naudojant Builder šabloną
        builder = FinancialReportBuilder()
        for exp in salon.expenses:
            builder.add_expense(exp)
        for earn in salon.earnings:
            builder.add_earning(earn)

        report = builder.add_summary().build()

        # 5. Išsaugome ataskaitą į .txt failą (File I/O reikalavimas)
        file_name = f"salon_{salon_id}_report.txt"
        self.file_manager.save_report_txt(report, file_name)

        return report

    def _extract_expenses(self, message: str):
        """Ieško išlaidų (nuoma, prekės ir kt.)"""
        expenses = []
        msg_lower = message.lower()
        
        # Nuomos paieška
        rent_match = re.search(r'(nuoma|rent)\s+(\d+)', msg_lower)
        if rent_match:
            amount = float(rent_match.group(2))
            expenses.append(RentExpense(amount, datetime.now(), "Pagrindinis Salonas"))
        
        # Prekių paieška
        supply_match = re.search(r'(prekės|supplies)\s+(\d+)', msg_lower)
        if supply_match:
            amount = float(supply_match.group(2))
            expenses.append(SupplyExpense(amount, datetime.now(), "Grožio Prekės"))
        
        return expenses

    def _extract_earnings(self, message: str):
        """Ieško pajamų (kirpimas, paslaugos ir kt.)"""
        earnings = []
        msg_lower = message.lower()
        
        earn_pattern = r'(kirpimas|paslaugos|earning|income)\s+(\d+)'
        matches = re.findall(earn_pattern, msg_lower)
        
        for service, amount in matches:
            earnings.append(Earning(float(amount), service.capitalize(), datetime.now()))
            
        return earnings
