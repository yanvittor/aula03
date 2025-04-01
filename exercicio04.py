#código para receber dois múmeros e mostrar eles em ordem crescente
X  = int(input("digite um numero"))
Y = int(input("digite um numero"))

if X > Y:
    print(f"{Y},{X}")
else:
    print(f"{X},{Y}")