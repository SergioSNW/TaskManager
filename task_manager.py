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
    
    def __init__(self):
        self._tasks = []
        self._next_id = 1
        
    def add_task(self, description):
        task = Task(self._next_id, description)
        self._tasks.append(task)
        self._next_id += 1
        print(f"Task added: {description}")
    
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
                print(f"Task #{id} marked as completed.")
                return
        print(f"Task with id #{id} not found.")
    
    def delete_task(self, id):
        for task in self._tasks:
            if task.id == id:
                self._tasks.remove(task)
                print(f"Task #{id} deleted.")
                return
        print(f"Task with id #{id} not found.")