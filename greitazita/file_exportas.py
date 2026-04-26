import csv
import os
from typing import List, Dict
from datetime import datetime

class FinanceFileManager:
    @staticmethod
    def append_to_csv(record: Dict, filename: str = "finance_report.csv"):
        """Prideda naują įrašą į CSV failą (neperrašo senų duomenų)"""
        file_exists = os.path.isfile(filename)
        
        with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['type', 'amount', 'category', 'description', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Headers rašome tik pirmą kartą
            if not file_exists or os.path.getsize(filename) == 0:
                writer.writeheader()
            
            writer.writerow(record)
        
        print(f"✅ Duomenys pridėti į {filename}")

    @staticmethod
    def export_to_csv(records: List[Dict], filename: str = "finance_report.csv"):
        """Senas metodas – perrašo failą (paliekame jei reikia)"""
        if not records:
            return
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['type', 'amount', 'category', 'description', 'date']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(records)
        print(f"✅ Eksportuota į {filename}")

    @staticmethod
    def save_report_txt(report_text: str, filename: str = "profit_report.txt"):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report_text)
        print(f"✅ Ataskaita išsaugota: {filename}")
