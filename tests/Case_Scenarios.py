# Patikrinu, kaip programa reaguoja į nelogiškus įvedimus
import unittest
from io import StringIO
import sys
from greitazita.ai import GreitaZitaAI
from greitazita.entities import FinancialRecord

class TestBusinessScenarios(unittest.TestCase):
    """
    Scenarijų testai, tikrinantys elgseną su neteisingais duomenimis.
    """

    def setUp(self):
        self.ai = GreitaZitaAI()
        self.record = FinancialRecord("Scenarijų Testas")

    def test_scenario_invalid_amount_input(self):
        """
        SCENARIJUS: Vartotojas vietoj skaičiaus įveda tekstą.
        Tikimasi: Sistema ne lūžta, o informuoja apie klaidą.
        """
        # Imituojame sistemos išvestį (stdout)
        captured_output = StringIO()
        sys.stdout = captured_output
        
        # Bandoma pridėti pajamų kiekį kaip tekstą 'daug'
        self.ai.process_message(1, "Mano pajamos buvo daug")
        
        sys.stdout = sys.__stdout__  # Grąžiname standartinę išvestį
        
        # Tikriname, ar vartotojas gavo pranešimą apie klaidą
        self.assertIn("Something went wrong", captured_output.getvalue())
        print("\n[OK] Nelogiško įvedimo testas praėjo: Sistema informavo apie klaidą.")

    def test_scenario_negative_expense(self):
        """
        SCENARIJUS: Vartotojas įveda neigiamas išlaidas (loginė klaida).
        """
        response = self.ai.process_message(1, "Išlaidos -500")
        self.assertIn("Something went wrong", response)
        print("[OK] Neigiamų skaičių scenarijus suvaldytas.")

    def test_scenario_empty_report(self):
        """
        SCENARIJUS: Bandoma generuoti ataskaitą be jokių duomenų.
        """
        result = self.record.profit_loss()
        self.assertEqual(result, 0)
        print("[OK] Tuščios ataskaitos scenarijus: Balansas lygus 0.")

if __name__ == '__main__':
    unittest.main(verbosity=2)
