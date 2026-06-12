# test_calculadora_ia.py
import unittest
from calculadora import potencia


class TestCalculadora(unittest.TestCase):
    """Testes para a função potencia, com cenários planejados com apoio de IA."""

    def test_potencia_com_varios_casos(self):
        casos = [
            (2, 3, 8),
            (5, 0, 1),
            (7, 1, 7),
            (0, 5, 0),
            (-2, 2, 4),
            (-2, 3, -8),
            (2, -1, 0.5),
        ]
        for a, b, esperado in casos:
            with self.subTest(a=a, b=b):
                self.assertEqual(potencia(a, b), esperado)


if __name__ == "__main__":
    unittest.main()