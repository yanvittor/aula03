#código para receber 3 notas de um aluno e verificar se ele esta reprovado ou aprovado
N1 = float(input("digite a primeira nota"))
N2 = float(input("digite a segunda nota"))
N3 = float(input("digite a terceira nota"))
Media = (N1+N2+N3)/3

if Media >= 7:
    print(f"Aprovada maezinha")
else:
     if Media <4:
         print(f"Reprovada, maezinha, tente novamente")
     else:
        print(f"Recupera maezinhaa")
