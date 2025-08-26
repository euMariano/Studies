def compare():
    nomes = []
    if len(nomes) < 5:
        for i in range(5):
            nomes.append(input("Digite o nome: "))
            if len(nomes) == 5:
                nome = input("Digite o nome a ser procurado: ")
                for i in range(len(nomes)):
                    if nome == nomes[i]:
                        print(f"O nome {nome} está na posição {i + 1}")
                        break
                    elif nome not in nomes:
                        print("O nome não está na lista")
                        break


def main():
    compare()


if __name__ == "__main__":
    main()
