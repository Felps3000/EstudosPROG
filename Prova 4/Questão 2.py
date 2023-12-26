"""
2) Serão realizadas eleições na turma e para isso será necessário desenvolver um programa que registra os votos,
calcula e apresenta os resultados com percentuais. Segundo as regras da instituição, em todos os processos
eletivos, podem concorrer no máximo 5 candidatos, identificados pelos números de 1 a 5. Outra regra é que todos
os alunos são obrigados a votar. Dessa forma, já se sabe antecipadamente qual o total de votos que deverão ser
registrados. Desenvolva o programa para essa eleição com as seguintes características: inicialmente o usuário
deve informar o número total de votantes (t ), para depois digitar os votos individuais de cada um desses
votantes, onde cada voto é um número entre 1 e 5 ( 1 <= voto <= 5 ). O programa deve calcular e mostrar a
quantidade de votos recebida por cada um dos candidatos, seguido do percentual, conforme os exemplos abaixo:

Entrada: um número inteiro e positivo total, onde 0 < total, que representa a quantidade total de alunos votantes
no processo. Esse número é então seguido por total outros números inteiros ( voto ) que estão contidos no
intervalo ( 1 <= voto <= 5 ), onde cada voto representa um voto no respectivo candidato.
Saída: seis linhas, onde as cinco'primeiras são compostas por 3 números, separados por um espaço entre eles: o
número do candidato ( 1 a 5 ), o total de votos recebido por este candidato e, por fim, o percentual que representa
essa quantidade de votos no pleito. O valor de percentual é um número com duas casas decimais, seguido pelo
respectivo símbolo "%". A sexta e última linha da saída indica o resultado oficial da eleição. Caso haja um
vencedor, apresenta o número do candidato vencedor seguido pela palavra " venceu!". No entanto, se houver
empate, apresenta a mensagem "Empate!"
Exemplos de entrada e saída:

Entrada     Saída       |   Entrada     Saída       |   Entrada     Saída       |   Entrada     Saída
20          1 6 30.00%  |    10         1 3 30.00%  |   7           1 2 28.57%  |   16          1 4 25.00%
1           2 4 20.00%  |    5          2 2 20.00%  |   4           2 3 42.86%  |   1           2 2 12.50%
2           3 4 20.00%  |    1          3 3 30.00%  |   1           3 0 00.00%  |   2           3 4 25.00%
1           4 2 10.00%  |    2          4 0 00.00%  |   2           4 2 28.57%  |   5           4 2 12.50%
5           5 4 20.00%  |    3          5 2 20.00%  |   1           5 0 20.00%  |   3           5 4 25.00%
3           1 venceu!   |    5          Empate!     |   4           2 venceu!   |   4           Empate!
4                       |    2                      |   2                       |   2
2                       |    3                      |   2                       |   4
4                       |    1                      |                           |   3
3                       |    1                      |                           |   5
5                       |    3                      |                           |   5
5                       |                           |                           |   1
2                       |                           |                           |   3
1                       |                           |                           |   1
3                       |                           |                           |   3
1                       |                           |                           |   5
3                       |                           |                           |   1
5                       |                           |                           |
2                       |                           |                           |
1                       |                           |                           |
1                       |                           |                           |
"""
