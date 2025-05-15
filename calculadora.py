#!/usr/bin/env python
# calculadora.py
import sys

class Calculadora:
    @staticmethod
    def multiplicar(a, b):
        return a * b
    def dividir(a, b):
        return a / b

def main():
    if len(sys.argv) != 3:
        print("Uso: python calculadora.py <num1> <num2>")
        sys.exit(1)
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Ambos parámetros deben ser números.")
        sys.exit(1)
    resultado = Calculadora.multiplicar(num1, num2)
    print(resultado)

if __name__ == "__main__":
    main()
