"""
3) Um número primo é aquele que possui exatamente dois divisores: 1 e o próprio número. Construa um programa
que leia um valor inteiro positivo e, a partir de estratégias de repetições, mostra todos os números primos menores
que esse valor (não existe número primo negativo!), conforme os exemplos abaixo:

Entrada: um valor inteiro positivo.
Saída: uma sequencia com todos os números primos menores que o valor informado na entrada.
Exemplos de entrada e saída:

Entrada Saída | Entrada Saída | Entrada Saída | Entrada Saída | Entrada Saída
35      2     | 20      2     | 2             | 7       2     | 15      2
        3     |         3     |               |         3     |         3
        5     |         5     |               |         5     |         5
        7     |         7     |               |               |         7
        11    |         11    |               |               |         11
        13    |         13    |               |               |         13
        17    |         17    |               |               |
        19    |         19    |               |               |
        23    |               |               |               |
        29    |               |               |               |
        31    |               |               |               |


"""

n = int(input('VALOR: '))

pri = 2

if (n > 2):
    while (pri < n):
        ini = 1
        div = 0
        while (ini <= pri):
            if (pri % ini == 0):
                div+=1
            ini+=1
        if (div == 2):
            print (pri)
        pri+=1