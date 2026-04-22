import csv
import json
from typing import List, Dict
from datetime import datetime

class FinanceFileManager:
    @staticmethod
    def export_to_csv(records: List[Dict], filename: str = "finance_report.csv"):
        """Export financial records to CSV file"""
        if not records:
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['type', 'amount', 'category', 'date', 'description']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)
        print(f"✅ Exported to {filename}")
    
    @staticmethod
    def import_from_csv(filename: str) -> List[Dict]:
        """Import financial records from CSV file"""
        records = []
        try:
            with open(filename, 'r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    records.append(row)
            print(f"✅ Imported {len(records)} records from {filename}")
        except FileNotFoundError:
            print(f"❌ File {filename} not found")
        return records
    
    @staticmethod
    def save_report_txt(report_text: str, filename: str = "profit_report.txt"):
        """Save report to plain text file"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"✅ Report saved to {filename}")
