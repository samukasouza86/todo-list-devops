# todo.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Tarefa adicionada: {task}")

def list_tasks():
    print("\nLista de Tarefas:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Teste
add_task("Aprender Git")
add_task("Praticar GitHub")
list_tasks()
