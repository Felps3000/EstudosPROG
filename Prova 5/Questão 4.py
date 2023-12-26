"""
4) Faça um programa para receber do usuário um valor inteiro e positivo. Desenvolva um programa que realiza a
soma de todos os números da Série de Fibonacci que são menores do que o valor apresentado na entrada,
conforme os exemplos abaixo. Os dois primeiros valores da Série de Fibonacci são 0 e 1 e, a partir destes, cada
número seguinte é o resultado da soma dos seus dois antecessores.

Entrada: um valor inteiro positivo N (N >0).
Saída: um valor inteiros e positivo, que representa a soma entre todos os números da Série de Fibonacci menores
que o valor N lido na entrada.
Exemplos de entrada e saída:

Entrada		Entrada		Entrada
1			10			6

Saída		Saída		Saída
0			20			12
"""

entrada = int(input())

c = 0

n1 = 1
n2 = 0
fib = 0
soma = 0

if entrada == 1:
    print("0")

else:

    while c < entrada:

        fib = n2 + n1
        n2 = n1  # está um pouco "enrolado" - poderia ser bem mais direto
        n1 = fib

        if fib < entrada:
            soma += fib

        c += 1

    print(soma + 1)