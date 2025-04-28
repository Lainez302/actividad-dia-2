numero1 = int(input("dame el primer numero:"))
numero2 = int(input("dame el segundo numero"))
numero3 = int(input("dame el tercer numero"))

if numero1<=numero2 and numero1<=numero3:
    print("es el numero mas pequeño", numero1)
elif numero2<=numero1 and numero2<=numero3:
    print("es el numero mas pequeño",  numero2)
else:
    print("es el numero mas pequeño", numero3)