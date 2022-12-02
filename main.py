print("**VENTA DE PANTALONES**")
nom=str(input("ingrese su nombre:"))
print(nom,":bienbenido")
#tot=160.50
print("#cantidad#")
#sub=cant*160.50
cant=int(input("ahora ingrese la cantidad de pantalones a llevar"))
sub=cant*160.50

if(cant>=10):
    print("el descuento es de un 25%")
elif(cant>=7):
    print("el descuento es de un 10%")
elif(sub>=700):
    print("descuento de un 5%")
else:
    print(sub)