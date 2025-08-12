numero = int(input("Coloque um número:"))

if numero:
    
    par = "impar"
    
if numero % 2 == 0:
 par = "par"

print(f"O número {numero} é {par}")