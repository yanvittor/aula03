#Código para ler o números de litros vendidos e o tipo de combustivel
tipo = input("Digite o tipo do combustivel\n"
             "G para Gasolina\n"
             "E para Etanol")
quantidade = float(input("Quantos litros:  "))
vGas = 5.8
vEtal = 4.9
if tipo == "G":
    valor = vGas * quantidade
else:
    valor = vEtal * quantidade

    print(f"Voce gastou R${valor:.2f}")