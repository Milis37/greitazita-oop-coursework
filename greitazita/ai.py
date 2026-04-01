from .database import DatabaseManager
from .builder import FinancialReportBuilder
from .models import ChatMessage, Salon
from datetime import datetime
import re

class GreitaZitaAI:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.db = DatabaseManager()
        return cls._instance

    def process_message(self, salon_id: int, message: str) -> str:
        # Save chat message
        session = self.db.get_session()
        chat = ChatMessage(salon_id=salon_id, role="user", content=message)
        session.add(chat)
        session.commit()

        # Simple rule-based "AI" parser (critical & realistic)
        expenses = re.findall(r'(nuoma|maitinimas|šampūnas|muilas|kosmetika)\s*[:\-]?\s*(\d+)', message.lower())
        earnings = re.findall(r'(apyvarta|pardavimai|pajamos)\s*[:\-]?\s*(\d+)', message.lower())

        builder = FinancialReportBuilder("Demo Salon")
        total_exp = 0
        total_earn = 0

        for cat, amt in expenses:
            amount = float(amt)
            total_exp += amount
            builder.add_expense(amount, cat.capitalize())

        for _, amt in earnings:
            amount = float(amt)
            total_earn += amount
            builder.add_earning(amount, "Sales")

        report = builder.build()
        profit = report.profit_loss()

        response = f"""📊 **GreitaZita 3-month analysis**
Total expenses: {total_exp:.2f} €
Total earnings: {total_earn:.2f} €
**Real profit/loss: {profit:+.2f} €**

Critical note: This does NOT include VAT (21%), taxes, or salon-specific costs. Real salons lose ~30-40% more after these."""

        # Save AI response
        ai_chat = ChatMessage(salon_id=salon_id, role="ai", content=response)
        session.add(ai_chat)
        session.commit()
        session.close()

        return response
