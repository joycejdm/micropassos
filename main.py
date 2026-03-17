from src.tracker import TaskTracker


def exibir_menu():
    print("\n" + "=" * 40)
    print("🧠 MicroPassos - Foco no Agora")
    print("=" * 40)
    print("1. Adicionar nova tarefa com micro-passos")
    print("2. Listar tarefas e progresso")
    print("3. Concluir um micro-passo")
    print("0. Sair")
    return input("Escolha uma opção: ")


def main():
    tracker = TaskTracker()

    while True:
        opcao = exibir_menu()

        if opcao == '1':
            nome = input("Qual a grande tarefa? (ex: Estudar): ")
            passos_str = input("Micro-passos (separados por vírgula): ")
            passos = [p.strip() for p in passos_str.split(",") if p.strip()]

            try:
                tracker.add_task(nome, passos)
                print("✅ Tarefa e micro-passos adicionados com sucesso!")
            except ValueError as e:
                print(f"❌ Erro: {e}")

        elif opcao == '2':
            tarefas = tracker.get_tasks()
            if not tarefas:
                print("📭 Nenhuma tarefa cadastrada no momento.")

            for t in tarefas:
                progresso = tracker.get_progress(t['id'])
                info_tarefa = f"\n[{t['id']}] {t['name']}"
                print(f"{info_tarefa} - Progresso: {progresso:.1f}%")
                for i, passo in enumerate(t['steps']):
                    status = "[X]" if passo['completed'] else "[ ]"
                    print(f"   {i}. {status} {passo['description']}")

        elif opcao == '3':
            try:
                task_id = int(input("Digite o ID da tarefa (número): "))
                step_idx = int(input("Digite o número do passo: "))
                tracker.complete_step(task_id, step_idx)
                print("🎉 Excelente! Micro-passo concluído!")
            except (ValueError, KeyError, IndexError) as e:
                print(f"❌ Erro: Verifique os números. Detalhe: {e}")

        elif opcao == '0':
            print("Até logo! Mantenha o foco.")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
