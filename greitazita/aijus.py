import re
from datetime import datetime
from .models import Salon, RentExpense, SupplyExpense, Earning
from .builderis.py import FinancialReportBuilder  # Įsitikinkite, kad kelias teisingas
from .file_export import FinanceFileManager      # Jūsų failų valdymo modulis
from .database import DatabaseManager              # SQL integracija

class GreitaZitaAI:
    def __init__(self):
        self.salons = {}
        self.file_manager = FinanceFileManager()
        self.db_manager = DatabaseManager()  # Singleton DB valdytojas

    def process_message(self, salon_id: int, message: str) -> str:
        """
        Pagrindinis metodas, kuris apdoroja žinutę, išsaugo duomenis į DB 
        ir sugeneruoja tekstinę ataskaitą.
        """
        # 1. Gauname arba sukuriame salono objektą (Agregacija)
        if salon_id not in self.salons:
            self.salons[salon_id] = Salon(salon_id, f"Salon-{salon_id}")
        
        salon = self.salons[salon_id]

        # 2. Ištraukiame duomenis iš teksto (Regex)
        expenses = self._extract_expenses(message)
        earnings = self._extract_earnings(message)

        # 3. Pridedame prie salono objekto ir išsaugome į SQL DB
        session = self.db_manager.get_session()
        try:
            for exp in expenses:
                salon.add_expense(exp)
                session.add(exp)  # Įrašome išlaidą į DB
            
            for earn in earnings:
                salon.add_earning(earn)
                session.add(earn) # Įrašome pajamas į DB
            
            session.commit()      # Patvirtiname SQL tranzakciją
        except Exception as e:
            session.rollback()
            print(f"Klaida įrašant į DB: {e}")
        finally:
            session.close()

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

    def _extract_expenses(self, message: str) -> list:
        """Ieško raktažodžių 'Rent' arba 'Supplies' ir sumų."""
        expenses = []
        message = message.lower()
        
        # Nuomos paieška (Inheritance: RentExpense)
        rent_match = re.search(r'nuoma\s+(\d+)', message) or re.search(r'rent\s+(\d+)', message)
        if rent_match:
            amount = float(rent_match.group(1))
            expenses.append(RentExpense(amount, datetime.now(), "Pagrindinis Salonas"))

        # Prekių paieška (Inheritance: SupplyExpense)
        supply_match = re.search(r'prekės\s+(\d+)', message) or re.search(r'supplies\s+(\d+)', message)
        if supply_match:
            amount = float(supply_match.group(1))
            expenses.append(SupplyExpense(amount, datetime.now(), "Grožio Prekės UAB"))
            
        return expenses

    def _extract_earnings(self, message: str) -> list:
        """Ieško pajamų (pvz., kirpimas, paslaugos)."""
        earnings = []
        message = message.lower()
        
        # Pajamų paieška
        earn_pattern = r'(kirpimas|paslaugos|earnings)\s+(\d+)'
        matches = re.findall(earn_pattern, message)
        for service, amount in matches:
            earnings.append(Earning(float(amount), service.capitalize(), datetime.now()))
            
        return earnings
