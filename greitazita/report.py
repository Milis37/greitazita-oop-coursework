from .entities import FinancialRecord
from .utils import export_to_csv

class ReportGenerator:
    """Generates professional financial summaries and exports."""

    def generate_summary(self, record: FinancialRecord) -> str:
        summary = f"🏬 Salon: {record.salon_name}\n"
        summary += f"Total Expenses (3 months): {record.total_expenses():.2f} €\n"
        summary += f"Total Earnings (3 months): {record.total_earnings():.2f} €\n"
        profit = record.profit_loss()
        summary += f"**Real Profit / Loss: {profit:+.2f} €**\n"
        if profit < 0:
            summary += "⚠️ CRITICAL: Salon is operating at a loss. Immediate cost review recommended.\n"
        return summary

    def export_report(self, record: FinancialRecord, filename: str = "financial_report.csv"):
        export_to_csv(record, filename)
        return f"Report exported → {filename}"
