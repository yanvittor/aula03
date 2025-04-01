#ler o programa que inmfrome os dados de uma pessoa:nome, idade e salario
nome = str(input("digite seu nome"))
idade = int(input("digite sua idade"))
salario = float(input("digite seu salario"))
percentual = float(input("seu salario com base no percentual de"))
aumento = ((salario)*(percentual)/100)
salario_aumentado = (salario)+(aumento)
print(f"Ola,{nome},sua idade é{idade} e seu salario {salario_aumentado:.2f}")
