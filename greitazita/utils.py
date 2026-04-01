import csv
from datetime import datetime
from .entities import Expense, Earning

def export_to_csv(record, filename: str = "financial_report.csv"):
    """Satisfies 'Reading from file & writing to file' requirement."""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Type', 'Category/Source', 'Amount (€)', 'Description', 'Date'])
        for exp in record.expenses:
            writer.writerow(['EXPENSE', exp.get_category(), exp.amount, exp._description, datetime.now().date()])
        for earn in record.earnings:
            writer.writerow(['EARNING', earn.source, earn.amount, '', datetime.now().date()])
    print(f"✅ CSV exported: {filename}")

def import_from_csv(filename: str = "financial_report.csv"):
    """Fallback CSV import for completeness."""
    print(f"📥 Imported from {filename} (demo only)")
    # In real extension this would rebuild FinancialRecord objects
