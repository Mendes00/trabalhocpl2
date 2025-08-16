# Calculadora em C + Python

Projeto de uma calculadora que soma dois números usando:
- Código em C para calcular a soma.
- Interface gráfica em Python com Tkinter.

## Estrutura do projeto

- `src/soma.c` → Código em C que recebe dois números via terminal e retorna a soma.
- `src/calculadora.py` → Interface gráfica em Python que chama o programa C compilado.


## Como usar

 1. Compile o código C:
 gcc src/soma.c -o src/soma.exe

   2.Execute a interface em Python:
   python src/calculadora.py
