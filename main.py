from src.tracker import TaskTracker
from src.api import obter_frase_motivacional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()


def exibir_menu():
    painel = Panel.fit(
        "🧠 [bold cyan]MicroPassos[/bold cyan] - Foco no Agora",
        border_style="cyan"
    )
    console.print(painel)
    console.print("1. [green]Adicionar[/green] tarefa com micro-passos")
    console.print("2. [blue]Listar[/blue] tarefas e progresso")
    console.print("3. [magenta]Concluir[/magenta] um micro-passo")
    console.print("0. [red]Sair[/red]")
    return console.input("\n[bold]Escolha uma opção:[/bold] ")


def main():
    tracker = TaskTracker()

    while True:
        opcao = exibir_menu()

        if opcao == '1':
            nome = console.input("[yellow]Qual a grande tarefa?[/yellow] ")
            txt_p = "[yellow]Passos (separar por vírgula):[/yellow] "
            passos_str = console.input(txt_p)
            passos = [p.strip() for p in passos_str.split(",") if p.strip()]

            try:
                tracker.add_task(nome, passos)
                msg = "[bold green]✅ Tarefa adicionada![/bold green]\n"
                console.print(msg)
            except ValueError as e:
                console.print(f"[bold red]❌ Erro: {e}[/bold red]\n")

        elif opcao == '2':
            tarefas = tracker.get_tasks()
            if not tarefas:
                console.print("[bold red]📭 Nenhuma tarefa.[/bold red]\n")
                continue

            for t in tarefas:
                progresso = tracker.get_progress(t['id'])
                titulo = f"[{t['id']}] {t['name']} ({progresso:.1f}%)"

                tabela = Table(title=titulo, title_style="bold cyan")
                tabela.add_column("Nº", justify="center", style="cyan")
                tabela.add_column("Status", justify="center")
                tabela.add_column("Descrição", style="white")

                for i, passo in enumerate(t['steps']):
                    if passo['completed']:
                        status = "[green]✅[/green]"
                    else:
                        status = "[red]❌[/red]"
                    tabela.add_row(str(i), status, passo['description'])

                console.print(tabela)
                console.print()

        elif opcao == '3':
            try:
                txt_id = "Digite o [cyan]ID da tarefa[/cyan]: "
                t_id = int(console.input(txt_id))

                txt_passo = "Digite o [cyan]Nº do passo[/cyan]: "
                p_idx = int(console.input(txt_passo))

                tracker.complete_step(t_id, p_idx)
                msg_ok = "[bold green]🎉 Passo concluído![/bold green]"
                console.print(msg_ok)

                # Chamada da API motivacional
                frase = obter_frase_motivacional()
                console.print(f"[italic yellow]{frase}[/italic yellow]\n")

            except (ValueError, KeyError, IndexError) as e:
                console.print(f"[bold red]❌ Erro: {e}[/bold red]\n")

        elif opcao == '0':
            console.print("[bold cyan]Até logo! Mantenha o foco.[/bold cyan]")
            break
        else:
            console.print("[bold red]❌ Opção inválida.[/bold red]\n")


if __name__ == "__main__":
    main()
