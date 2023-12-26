"""
3) Cinco jovens estão participando de uma gincana e eles estão identificados, cada um, por um número de 1 a 5. A
tarefa de hoje é empilhar tijolos. Os competidores vão até o depósito de tijolos, pegam quantos conseguem
carregar e levam até o local onde eles montam as pilhas. Desta forma, não há como prever quantas vezes cada
competidor carregará tijolos e nem quantos tijolos por vez. Portanto, quando eles chegam no local de
empilhamento, o juiz da prova verifica o número do competidor e a quantidade de tijolos que ele trouxe para
acrescentar à sua pilha. Vence aquele que ao final da prova tiver a pilha com o maior número de tijolos. No caso
de empate, será considerado vencedor o competidor com o número mais baixo. Desenvolver um programa para
que o juiz, a cada chegada de competidor no local de empilhamento, possa informar o número do competidor e,
logo em seguida, a quantidade de tijolos trazida por ele. Para encerrar a prova, o juiz informa o valor ZERO na
leitura do número do competidor.

Entrada: um valor n, onde 0 <= n <= 5, onde 0 representa a condição de término da prova e os outros valores, o
número do competidor, que é então seguido por outro valor inteiro e positivo que representa a respectiva
quantidade de tijolos trazida por ele.
Saída: dois valores inteiros separados por um hífen, que representam, respectivamente, o número do competidor
vencedor e a quantidade de tijolos que ele empilhou. No caso da competição ser encerrada sem pilha de tijolos de
qualquer competidor, o programa apresenta ZERO na saída.
Exemplos de entrada e saída:

Entrada Saída | Entrada Saída | Entrada Saída | Entrada Saída | Entrada Saída
1       1-20  | 5       2-20  | 3       2-12  | 1       1-5   | 0       0
20            | 6             | 5             | 2             |
0             | 4             | 2             | 2             |
              | 9             | 4             | 2             |
              | 3             | 1             | 3             |
              | 7             | 3             | 2             |
              | 2             | 2             | 4             |
              | 10            | 6             | 2             |
              | 1             | 1             | 1             |
              | 8             | 3             | 3             |
              | 5             | 2             | 2             |
              | 6             | 2             | 3             |
              | 4             | 5             | 3             |
              | 9             | 2             | 3             |
              | 3             | 0             | 4             |
              | 7             |               | 3             |
              | 2             |               | 0             |
              | 10            |               |               |
              | 1             |               |               |
              | 8             |               |               |
              | 0             |               |               |
"""
