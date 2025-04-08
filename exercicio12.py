#pedir um numero ao usuario e fazer uma tabuada
numero1 = int(input("digite um número"))
for x in range (1, 11, 1):
    mult = numero1 * x
    print( f"{x} X {numero1} = {mult}")