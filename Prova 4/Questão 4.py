"""
4) Um dispositivo de monitoramento de temperatura faz leituras de um sensor a cada segundo. Dessa forma, para
cada leitura, ele associa a temperatura ao horário em segundos. A cada 24 horas, o contador de segundos é zerado,
então a marcação de tempo é válida para cada leitura dentro do mesmo dia. Desenvolva um programa que recebe
dois valores. O primeiro é um valor inteiro não negativo, que indica o horário, em segundos, que foi realizada a
leitura da temperatura. O segundo valor é a temperatura, que possui uma casa decimal. Após, converte o horário
em segundos para o formato HH:MM:SS e apresenta uma mensagem, conforme os exemplos abaixo:

Entrada: um valor inteiro não negativo, que representa o horário, em segundos, da leitura do sensor; e mais um
valor com uma casa decimal.
Saída: Duas linhas impressas na tela, sendo que a primeira linha apresenta o texto "Horário:" seguido do horário
no formato HH:MM:SS, e a segunda apresenta o texto "Temperatura:" seguido da temperatura, com precisão de
uma casa decimal.
Exemplos de entrada e saída:

Entrada  Saída                     | Entrada  Saída
51792    Horário: 14:23:12         | 1        Horário: 00:00:01
13.1     Temperatura: 13.1 graus   | 5.9      Temperatura: 5.9 graus
"""

hora = int(input("Hora: "))
temp = float(input("Temperatura: "))

if hora > 86400:
    hora -= 86400

horaC = hora // 3600

minuto = hora - (horaC * 3600)

minC = minuto // 60

segundo = ((minC * 60) - minuto) * -1

print(f"Horário: {horaC:02}:{minC:02}:{segundo:02}")

print(f"Temperatura: {temp:.1f} graus")