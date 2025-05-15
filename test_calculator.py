#!/usr/bin/env python
# test_calculator.py
import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_multiplicar_enteros(self):
        self.assertEqual(Calculadora.multiplicar(3, 4), 12)

    def test_multiplicar_flotantes(self):
        self.assertAlmostEqual(Calculadora.multiplicar(2.5, 4), 10.0)

    def test_multiplicar_negativos(self):
        self.assertEqual(Calculadora.multiplicar(-2, 3), -6)
        self.assertEqual(Calculadora.multiplicar(-2, -3), 6)

    def test_multiplicar_por_cero(self):
        self.assertEqual(Calculadora.multiplicar(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
