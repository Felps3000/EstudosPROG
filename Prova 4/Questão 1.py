"""
1) Faça um programa onde um usuário informa três valores inteiros e positivos. Considere que esses números devem
compor uma data (dia, mês e ano). O programa dever verificar se esta é uma data válida, observando o número de
dias de cada mês, bem como se o ano é bissexto. Anos bissextos acontecem sempre que o ano é divisível por 4
sem ser divisível por 100, a menos que, neste caso seja também divisível por 400. Por fim, o programa apresenta
- uma mensagem com o resultado da análise, conforme os exemplos abaixo

Entrada: três valores inteiros positivos D, M e A (D> 0; M > 0; A > 0), que representam, respectivamente, um
dia, um mês e um ano para compor uma data.
Saída: uma mensagem de texto, com a palavra sim ou a palavra não, indicando o resultado da verificação.
Exemplos de entrada e saída:

Entrada Saída |  Entrada Saída | Entrada Saída
29      não   |  31      sim   | 35      não
2             |  7             | 15
2019          |  2023          | 2000
"""

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

bissexto = 0

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 100 == 0 and ano % 400 == 0):
    bissexto = 1

if dia <= 31 and mes <= 12:
    if mes == 2 and bissexto == 1 and dia <= 29:
        print("sim")

    elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia <= 30):
        print("sim")

    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        print("sim")

    else:
        print("não")
else:
    print("não")