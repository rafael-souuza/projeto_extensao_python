import unittest
import os
from src.report.report_generator import gerar_planilha

class TestReportGenerator(unittest.TestCase):

    def test_gerar_planilha(self):
        gerar_planilha()
        self.assertTrue(os.path.exists('relatorio.xlsx'))

if __name__ == '__main__':
    unittest.main()
