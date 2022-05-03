""" PROGRAMA PARA
VERIFICAR SI DADO UN NUMERO DE TRES CIFRAS, LA SUMA DE LOS DOS PRIMEROS DA EL TERCERO """

a = int(input("Ingrese el valor del primer digito: "))
b = int(input("Ingrese el valor del segundo digito: "))
c = int(input("Ingrese el valor del tercer digito: "))

if a + b == c:
    msj = "si cumple."
else:
    msj = "no cumple."

print("El numero ingresado" , msj)
