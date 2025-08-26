from listaDeCompras import adicionar, exibir, remover
from rich.console import Console
from rich.prompt import Prompt

console = Console()


def main():
    while True:
        console.print(
            "\n[blue]================ LISTA DE COMPRAS ================[/blue]"
        )
        console.print("[blue]1[/blue] - Adicionar item")
        console.print("[blue]2[/blue] - Exibir itens")
        console.print("[blue]3[/blue] - Remover")
        console.print("[blue]4[/blue] - Sair")
        console.print("[blue]==================================================[/blue]")

        opcao = Prompt.ask("Digite a opção desejada")

        if opcao == "1":
            adicionar()
        elif opcao == "2":
            exibir()
        elif opcao == "3":
            remover()
        elif opcao == "4":
            break
        else:
            console.print("[red]Opção inválida. Tente novamente.[/red]")


if __name__ == "__main__":
    main()
