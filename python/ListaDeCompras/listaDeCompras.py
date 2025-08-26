import json
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

console = Console()

# Carregar lista do arquivo JSON
try:
    with open("lista.json", "r") as f:
        lista = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    lista = []


# Salvar lista no JSON
def salvar_lista():
    with open("lista.json", "w") as f:
        json.dump(lista, f)


# Validar quantidade
def validar():
    while True:
        try:
            quantidade = IntPrompt.ask("Digite a quantidade")
            if quantidade <= 0:
                console.print("[red]Digite um número maior que zero[/red]")
            else:
                return quantidade
        except ValueError:
            console.print("[red]Por favor, digite um número válido[/red]")


# Validar número do item
def validar_numero(prompt, minimo, maximo):
    while True:
        try:
            valor = IntPrompt.ask(prompt)
            if minimo <= valor <= maximo:
                return valor
            console.print(f"[red]Digite um número entre {minimo} e {maximo}[/red]")
        except ValueError:
            console.print("[red]Por favor, digite um número válido[/red]")


# Adicionar item
def adicionar():
    item = Prompt.ask("\nDigite o item que deseja adicionar").strip()
    quantidade = validar()

    for i, (nome) in enumerate(lista):
        if nome.lower() == item.lower():
            lista[i][1] += quantidade
            console.print(
                f"[green]{quantidade} {item} adicionados. Total agora: {lista[i][1]}[/green]"
            )
            salvar_lista()
            return

    lista.append([item, quantidade])
    console.print(f"[green]{item} adicionado à lista de compras[/green]")
    salvar_lista()


# Exibir lista
def exibir():
    if not lista:
        console.print("\n[yellow]A lista de compras está vazia[/yellow]")
        return

    table = Table(title="Lista de Compras")
    table.add_column("Nº", justify="right")
    table.add_column("Item", justify="left")
    table.add_column("Quantidade", justify="right")

    for i, (nome, qtd) in enumerate(lista, start=1):
        table.add_row(str(i), nome, str(qtd))

    console.print(table)


# Remover item
def remover():
    if not lista:
        console.print("\n[yellow]A lista de compras está vazia[/yellow]")
        return

    exibir()
    numero = validar_numero(
        "\nDigite o número do item que deseja remover", 1, len(lista)
    )
    item, qtd_atual = lista[numero - 1]

    quantidade = validar()

    if quantidade < qtd_atual:
        lista[numero - 1] = [item, qtd_atual - quantidade]
        console.print(f"[green]{quantidade} {item} removido(s) da lista[/green]")
    else:
        lista.pop(numero - 1)
        console.print(f"[green]Todos os {item} foram removidos da lista[/green]")

    salvar_lista()
