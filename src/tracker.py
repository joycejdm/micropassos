import sqlite3


class TaskTracker:
    def __init__(self, filepath="data.db"):
        self.filepath = filepath
        self._create_tables()

    def _get_connection(self):
        """Abre uma conexão com o banco de dados SQLite."""
        return sqlite3.connect(self.filepath)

    def _create_tables(self):
        """Cria as tabelas relacionais se não existirem."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            ''')
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS steps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_id INTEGER NOT NULL,
                    description TEXT NOT NULL,
                    completed BOOLEAN NOT NULL CHECK (completed IN (0, 1)),
                    FOREIGN KEY (task_id) REFERENCES tasks (id)
                )
            ''')
            conn.commit()

    def add_task(self, name, steps):
        """Insere uma tarefa e seus passos no banco de dados."""
        if not name.strip() or not steps:
            msg = "A tarefa precisa de um nome e pelo menos um passo."
            raise ValueError(msg)

        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tasks (name) VALUES (?)", (name,))
            task_id = cursor.lastrowid

            for step in steps:
                sql = "INSERT INTO steps (task_id, description, completed) "
                sql += "VALUES (?, ?, 0)"
                cursor.execute(sql, (task_id, step))
            conn.commit()

        return {
            "id": task_id,
            "name": name,
            "steps": [{"description": s, "completed": False} for s in steps]
        }

    def get_tasks(self):
        """Busca todas as tarefas e seus respectivos passos."""
        tasks = []
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM tasks")
            for row in cursor.fetchall():
                task_id, name = row
                cursor.execute(
                    "SELECT description, completed FROM steps "
                    "WHERE task_id = ? ORDER BY id", (task_id,)
                )
                steps = [
                    {"description": r[0], "completed": bool(r[1])}
                    for r in cursor.fetchall()
                ]
                tasks.append({"id": task_id, "name": name, "steps": steps})
        return tasks

    def complete_step(self, task_id, step_index):
        """Marca um passo como concluído atualizando o banco."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
            if not cursor.fetchone():
                raise KeyError("Tarefa não encontrada.")

            cursor.execute(
                "SELECT id FROM steps WHERE task_id = ? ORDER BY id",
                (task_id,)
            )
            steps = cursor.fetchall()

            if not (0 <= step_index < len(steps)):
                raise IndexError("Passo não encontrado.")

            step_db_id = steps[step_index][0]
            cursor.execute(
                "UPDATE steps SET completed = 1 WHERE id = ?", (step_db_id,)
            )
            conn.commit()
            return True

    def get_progress(self, task_id):
        """Calcula a porcentagem lendo os passos do banco."""
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM tasks WHERE id = ?", (task_id,))
            if not cursor.fetchone():
                raise KeyError("Tarefa não encontrada.")

            cursor.execute(
                "SELECT completed FROM steps WHERE task_id = ?", (task_id,)
            )
            steps = cursor.fetchall()
            total = len(steps)
            if total == 0:
                return 0.0

            completed = sum(1 for step in steps if step[0])
            return (completed / total) * 100
