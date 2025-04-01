#código para rceber 2 times e o número de gols marcado e escrever o nome do vencedor
Time1 = str(input("Insira o nome do primeiro time"))
Time2 = str(input("Insira o nome do segundo time"))
GT1 = int(input("número de gol do time1"))
GT2 = int(input("número de gol do time2"))

if GT1 > GT2:
    print(f"o time do {Time1} ganhou do {Time2} de {GT1} a {GT2}")
else:
    if GT2 > GT1:
        print(f"o time do {Time2} ganhou do {Time1} de {GT2} a {GT1}")
    else:
     print(f"Empate")
