import json
import os


class TaskTracker:
    def __init__(self, filepath="data.json"):
        self.filepath = filepath
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Carrega as tarefas salvas no arquivo JSON."""
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    def save_tasks(self):
        """Salva as tarefas no arquivo JSON."""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(self.tasks, f, indent=4, ensure_ascii=False)

    def add_task(self, name, steps):
        """Adiciona uma nova grande tarefa dividida em micro-passos."""
        if not name.strip() or not steps:
            raise ValueError(
                "A tarefa precisa de um nome e pelo menos um passo."
            )

        new_task = {
            "id": len(self.tasks) + 1,
            "name": name,
            "steps": [{"description": s, "completed": False} for s in steps]
        }
        self.tasks.append(new_task)
        self.save_tasks()
        return new_task

    def get_tasks(self):
        """Retorna todas as tarefas."""
        return self.tasks

    def complete_step(self, task_id, step_index):
        """Marca um micro-passo específico como concluído."""
        for task in self.tasks:
            if task["id"] == task_id:
                if 0 <= step_index < len(task["steps"]):
                    task["steps"][step_index]["completed"] = True
                    self.save_tasks()
                    return True
                else:
                    raise IndexError("Passo não encontrado.")
        raise KeyError("Tarefa não encontrada.")

    def get_progress(self, task_id):
        """Calcula a porcentagem de conclusão de uma tarefa."""
        for task in self.tasks:
            if task["id"] == task_id:
                total = len(task["steps"])
                if total == 0:
                    return 0.0
                completed = sum(
                    1 for step in task["steps"] if step["completed"]
                )
                return (completed / total) * 100
        raise KeyError("Tarefa não encontrada.")
