"""
2) Utilizando estruturas de repetição, desenvolva um programa que recebe um valor inteiro e positivo e mostra uma
sequência de números, a partir do padrão apresentado e separados por espaços, conforme os exemplos abaixo:
Entrada: um valor inteiro positivo.
Saída: sequência de valores, relacionados ao valor de entrada, conforme os exemplos.
Exemplos de entrada e saida:

Entrada		Entrada		Entrada			Entrada
1			5			12				15

Saída		Saída		Saída			Saída
0			0 2 4		0 2 4 6 8 10	0 2 4 6 8 10 12 14
"""

entrada = int(input())

c = 0

while c <= entrada:
        print(c, end=" ")
        c += 2