def porta_not(bit):
    if bit == 0:
        return 1
    else:
        return 0
    
def porta_and(bit1, bit2):
    if bit1 == 1 and bit2 == 1:
        return 1;
    else: 
        return 0
    
def porta_or(bit1, bit2):
    if bit1 == 1 or bit2 == 1:
        return 1
    else:
        return 0
    
bit1 = int(input("Digite 0 ou 1: "))
bit2 = int(input("Digite 0 ou 1: "))

resultado1 = porta_and(bit1, bit2)
resultado_negado1 = porta_not(resultado1)

print("\nAND")
print(f"Resultado AND: {resultado1}")
print(f"Resultado negado: {resultado_negado1}")

resultado2 = porta_or(bit1, bit2)
resultado_negado2 = porta_not(resultado2)

print("\nOR")
print(f"Resultado OR: {resultado2}")
print(f"Resultado negado: {resultado_negado2}")

print("\nCHAMAAA")