import unittest
from unittest.mock import Mock, patch
from greitazita.ai import GreitaZitaAI
from greitazita.models import Salon, Expense, Earning
from greitazita.builder import FinancialReportBuilder
from datetime import datetime

class TestGreitaZitaAI(unittest.TestCase):
    
    def setUp(self):
        self.ai = GreitaZitaAI()
        self.salon = Salon(1, "Test Salon")
    
    def test_profit_calculation(self):
        """Test profit/loss calculation"""
        expense = Expense(1000, "Rent", datetime.now())
        earning = Earning(5000, "Haircut", datetime.now())
        self.salon.add_expense(expense)
        self.salon.add_earning(earning)
        
        profit = self.salon.calculate_profit()
        self.assertEqual(profit, 4000)
    
    def test_builder_pattern(self):
        """Test report builder creates correct format"""
        builder = FinancialReportBuilder()
        expense = Expense(500, "Supplies", datetime.now())
        earning = Earning(2000, "Coloring", datetime.now())
        
        report = builder.add_expense(expense).add_earning(earning).add_summary().build()
        
        self.assertIn("Total Expenses: 500.0€", report)
        self.assertIn("Total Earnings: 2000.0€", report)
        self.assertIn("Net Profit: 1500.0€", report)
    
    @patch('greitazita.file_export.FinanceFileManager.save_report_txt')
    def test_file_export(self, mock_save):
        """Test file export is called"""
        response = self.ai.process_message(1, "Rent 1200, Haircut 5000")
        mock_save.assert_called_once()
        self.assertIn("Net Profit", response)

if __name__ == '__main__':
    unittest.main()
