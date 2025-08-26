frutas = ("maca", "banana", "laranja", "uva")

if "banana" in frutas:
    print("passou")

lista = list(frutas)

lista.append("abacaxi")

frutas = tuple(lista)

print(frutas)
