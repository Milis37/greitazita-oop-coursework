    def process_message(self, salon_id: int, message: str) -> str:
        if salon_id not in self.salons:
            self.salons[salon_id] = Salon(salon_id, f"Salon-{salon_id}")
        
        salon = self.salons[salon_id]

        # <<< NAUJA DALIS: Įkeliam visus senus duomenis iš CSV >>>
        self._load_records_from_csv(salon, salon_id)

        # Ištraukiame naujus duomenis iš žinutės
        expenses = self._extract_expenses(message)
        earnings = self._extract_earnings(message)

        for exp in expenses:
            salon.add_expense(exp)
        for earn in earnings:
            salon.add_earning(earn)

        # Generuojame ataskaitą
        builder = FinancialReportBuilder(f"Salon-{salon_id}")
        for exp in salon.expenses:
            builder.add_expense(exp)
        for earn in salon.earnings:
            builder.add_earning(earn)

        report = builder.add_summary().build()

        file_name = f"salon_{salon_id}_report.txt"
        self.file_manager.save_report_txt(report, file_name)

        return report

    def _load_records_from_csv(self, salon, salon_id: int):
        """Įkelia visus įrašus iš CSV atgal į salon objektą"""
        filename = f"salon_{salon_id}_finance.csv"
        try:
            records = self.file_manager.import_from_csv(filename)  # turi būti tavo file_exportas.py
            for rec in records:
                if rec['type'] == 'earning':
                    # Sukurti Earning objektą ir pridėti
                    pass  # čia reikia logikos pagal tavo modelius
                elif rec['type'] == 'expense':
                    # Sukurti Expense objektą
                    pass
        except:
            pass  # jei failo nėra – nieko nedaryti
