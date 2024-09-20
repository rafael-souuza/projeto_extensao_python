import unittest
from database.db import conectar, salvar_dados_no_banco

class TestDatabaseFunctions(unittest.TestCase):

    def test_connectar(self):
        conn = conectar()
        self.assertTrue(conn.is_connected())
        conn.close()

    def test_salvar_dados_no_banco(self):
        try:
            salvar_dados_no_banco("Teste", "Equipamento", "BMP", "Problema")
            # Você pode adicionar mais validações conforme necessário
        except Exception as e:
            self.fail(f"salvar_dados_no_banco levantou uma exceção: {e}")

if __name__ == '__main__':
    unittest.main()
