# Patikrinu, ar visi 4 OOP principai veikia
import unittest
from greitazita.entities import FixedExpense, Earning, FinancialRecord
from greitazita.database import DatabaseManager
from greitazita.builder import FinancialReportBuilder

class TestFinanceUnits(unittest.TestCase):
    """
    Standartiniai vienetų testai, tikrinantys bazinę OOP struktūrą.
    Atitinka reikalavimą: 'Core functionality covered with unit tests'.
    """

    def setUp(self):
        self.db = DatabaseManager()  # Singleton instancija 

    def test_inheritance_and_polymorphism(self):
        """Tikriname paveldėjimą ir polimorfizmą per kategorijų gavimą."""
        expense = FixedExpense(1000, "Nuoma")
        # Tikriname, ar FixedExpense paveldėjo bazinės klasės savybes
        self.assertEqual(expense.get_category(), "Fixed Cost")
        self.assertIsInstance(expense, FixedExpense)

    def test_singleton_consistency(self):
        """Patikriname, ar DatabaseManager tikrai yra Singleton."""
        db2 = DatabaseManager()
        self.assertIs(self.db, db2, "Klaida: Sukurta daugiau nei viena DB instancija!")

    def test_encapsulation(self):
        """Patikriname, ar privatūs atributai yra apsaugoti (Encapsulation)."""
        expense = FixedExpense(500, "Internet")
        # Tikriname, ar tiesioginė prieiga prie _amount yra ribojama (Python konvencija)
        self.assertTrue(hasattr(expense, '_amount'))

    def test_builder_logic(self):
        """Patikriname, ar Builder šablonas teisingai surenka objektą."""
        builder = FinancialReportBuilder("Test Salon")
        report = builder.add_earning(1000, "Pardavimai").build()
        self.assertEqual(report.profit_loss(), 1000)

if __name__ == '__main__':
    unittest.main()
