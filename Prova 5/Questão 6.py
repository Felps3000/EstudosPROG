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
n = int(input('VALOR: '))

c = 1
f1 =0
f2 =1
fibo = 1

if n == 1:

    print (c)

else:

    while (fibo < n):
        fibo = f1 + f2
        f1=f2
        f2 = fibo
        c+=1
    print (c)