# todo.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Tarefa adicionada: {task}")

def list_tasks():
    print("\nLista de Tarefas:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def delete_task(index):
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print(f"Tarefa removida: {removed}")
    else:
        print("Índice inválido!")

# Teste
add_task("Aprender Git")
add_task("Praticar GitHub")
list_tasks()
