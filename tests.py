import unittest
from unittest.mock import patch
from core.dice import Dados

class TestDados(unittest.TestCase):

    @patch('backgammon.random.randint')
    def test_tirar_dado_iguales(self, mock_randint):
        mock_randint.side_effect = [4, 4]  
        dados = Dados(0, 0)
        resultado = dados.tirar_dado()
        self.assertEqual(resultado, [4, 4, 4, 4])
        self.assertEqual(dados.dado_1, 4)
        self.assertEqual(dados.dado_2, 4)
    
    @patch('backgammon.random.randint')
    def simple_test(self, mock_randint):

        mock_randint.side_effect = [5,2]

        dice = Dados(0,0)
        tirar = dice.tirar_dado()

        self.assertEqual(tirar, [5,2])
        self.assertEqual(dice.dado_1, 5)
        self.assertEqual(dice.dado_2, 2)
    
    def test_comenzar(self):
        dados = Dados(0,0)
        resultado = dados.comenzar()
        self.assertIn(resultado, ["Empiezan las fichas blancas", "Empiezan las fichas negras"])


if __name__ == "__main__":
    unittest.main()
