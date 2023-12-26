"""
5) Utilizando estruturas de repetição, desenvolva um programa que recebe um valor inteiro e positivo e mostra uma
sequência de números, a partir do padrão apresentado e separados por espaços, conforme os exemplos abaixo:

Entrada: um valor inteiro positivo.
Saída: sequência de valores, relacionados ao valor de entrada, conforme os exemplos.
Exemplos de entrada e saída:

Entrada Saída | Entrada Saída | Entrada Saída        | Entrada Saída
1       1     | 5       1 3 5 | 12      1 3 5 7 9 11 | 15      1 3 5 7 9 11 13 15

"""

entrada = int(input())

c = 1

while c <= entrada:
        print(c, end=" ")
        c += 2