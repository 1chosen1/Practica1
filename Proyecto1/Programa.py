# Mi primer programa
print("Hola soy el Doctor Python")
nom = input("Deme su Nombre: ")
h = input("Tiene dolor de cabeza? (s/n)")
s = input("Tiene dolor de estomago? (s/n)")
pr = input("Tiene problemas respiratorios? (s/n)")
if h == "s" and s == "s" and pr == "s":
    print(nom + " debemos Internarlo")
elif h == "s"  and s == "s":
    print(nom + " debes tomar Paracetamol")
elif h == "s":
    print (nom + " debes tomar Tylenol")
elif s == "s":
    print(nom + " debes tomar Pepto Bismol")
elif pr == "s":
    print(nom + " debes tomar Norcetin")
else:
    print(nom + " por favor retirese a su casa")

