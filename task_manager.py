import json

class Task:
    
    def __init__(self, id, description, completed=False):
        self.id = id
        self.description = description
        self.completed = completed
        
    def __str__(self):
        """This function is being overidden in order to print specific changes"""
        status = "✓" if self.completed else " "  # Operador ternario check if completed, whitespace if not.
        return f"[{status}] #{self.id}: {self.description}"
    
class TaskManager:
    
    # Constantes en python se suelen escribir en mayusculas, aunque no es obligatorio. Es una convención.
    FILENAME = "tasks.json"
    
    def __init__(self):
        self._tasks = []
        self._next_id = 1
        self.load_tasks()
        
    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Task added: {description}")
        self.save_tasks()
    
    def list_tasks(self):
        if not self._tasks:
            print("No tasks available at this moment.")
        else:
            for task in self._tasks:
                print(task)
    
    def complete_task(self, id):
        """ We have to first find the task in our list """
        for task in self._tasks:
            if id == task.id:
                task.completed = True
                print(f"Task #{id} marked as completed.[✓]")
                self.save_tasks()
                return
        print(f"Task with id #{id} not found.")
    
    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Task #{id} deleted.")
                self.save_tasks()
                return
        print(f"Task with id #{id} not found.")
        
    def load_tasks(self):
        try:
            # With open es una forma de manejar archivos que asegura que el archivo se cierre correctamente después de su uso, incluso si ocurre un error durante la operación. Es una buena práctica para evitar fugas de recursos.
            # El modo "r" indica que el archivo se abrirá en modo de lectura. Si el archivo no existe, se lanzará una excepción FileNotFoundError, que es manejada por el bloque except.
            with open(self.FILENAME, "r") as file:
                data = json.load(file)
                self._tasks = [Task(item["id"], item["description"], item["completed"]) for item in data]
                if self._tasks:
                    self._next_id = self._tasks[-1].id + 1
                else:
                    self._next_id = 1
                    
        except FileNotFoundError:
            self._tasks = []
    
    def save_tasks(self):
        with open(self.FILENAME, "w") as file:
            # La función json.dump() se utiliza para escribir datos en un archivo en formato JSON. En este caso, se está escribiendo una lista de diccionarios, donde cada diccionario representa una tarea con sus atributos (id, description, completed). La comprensión de listas se utiliza para crear esta lista de diccionarios a partir de la lista de objetos Task.
            json.dump([{"id": task.id, "description": task.description, "completed": task.completed} for task in self._tasks], file, indent=4)