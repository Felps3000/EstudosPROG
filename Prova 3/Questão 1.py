"""
1) Faça um programa para receber do usuário um valor inteiro e positivo, que indica quantos números da Série de
Fibonacci, a partir do primeiro da série, devem ser gerados e mostrados na tela, conforme os exemplos abaixo. Os
dois primeiros valores da Série de Fibonacci são 0 e 1 e, a partir destes, cada número seguinte é o resultado da
soma dos seus dois antecessores.

Entrada: um valor inteiro positivo N (N >0).
Saída: N valores inteiros positivos, que representam os N primeiros números, sempre seguidos por um hífen
como separador, que compõem a Série de Fibonacci.
Exemplos de entrada e saída:

Entrada Saída | Entrada Saída                   | Entrada Saída
1       0-    | 10      0-1-1-2-3-5-8-13-21-34- |  5      0-1-1-2-3-
"""

fib1 = 0
fib2 = c = 1
n = int(input("Digite um número: "))
print(f"{fib1}-",end='')
while c < n:
    s = fib1 + fib2
    fib1 = fib2
    fib2 = s
    print(f"{fib1}-",end='')
    c += 1