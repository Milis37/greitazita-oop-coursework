import unittest
from greitazita.entities import FixedExpense, ProductExpense, FinancialRecord, Earning
from greitazita.builder import FinancialReportBuilder
from greitazita.database import DatabaseManager
from greitazita.ai import GreitaZitaAI

class TestGreitaZitaOOP(unittest.TestCase):
    def test_4_oop_pillars(self):
        # Inheritance + Polymorphism
        fixed = FixedExpense(1000, "Rent")
        product = ProductExpense(300, "Shampoo")
        self.assertEqual(fixed.get_category(), "Fixed Cost")
        self.assertEqual(product.get_category(), "Product")

        # Encapsulation
        self.assertTrue(hasattr(fixed, '_amount'))  # private

        # Composition / Aggregation
        record = FinancialRecord("Test Salon")
        record.add_expense(fixed)
        record.add_earning(Earning(5200, "Sales"))
        self.assertGreater(record.profit_loss(), 0)

    def test_singleton(self):
        db1 = DatabaseManager()
        db2 = DatabaseManager()
        self.assertIs(db1, db2, "Singleton violated")

    def test_builder(self):
        builder = FinancialReportBuilder("Beauty Salon")
        builder.add_expense(5000, "Nuoma").add_earning(5200, "Apyvarta")
        report = builder.build()
        self.assertEqual(report.profit_loss(), 200)

    def test_ai_and_db(self):
        ai = GreitaZitaAI()
        resp = ai.process_message(1, "Nuoma 5000 Maitinimas 100 Apyvarta 5200")
        self.assertIn("profit", resp.lower())

if __name__ == '__main__':
    unittest.main(verbosity=2)
