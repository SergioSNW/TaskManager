from task_manager import TaskManager

def print_menu():
    print("\n--- Inteligent Task Manager ---\n")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

def main():
    
    manager = TaskManager()
    
    while True:
    
        print_menu()
        
        try:
    
            choice = int(input("Choose an option: "))
        
            match choice:
                case 1:
                    description = input("Enter task description: ")
                    manager.add_task(description)
                
                case 2:
                    manager.list_tasks()
                    
                case 3:
                    id = input("Enter task ID to complete: ")
                    if id.isdigit():
                        manager.complete_task(int(id))
                    else:
                        print("Invalid ID. Please enter a numeric value.")
                        
                case 4:
                    id = input("Enter task ID to delete: ")
                    if id.isdigit():
                        manager.delete_task(int(id))
                    else:                    
                        print("Invalid ID. Please enter a numeric value.")
                    
                case 5:
                    print("Exiting the Task Manager. Goodbye!")
                    break
                case _: # Default case for Default in other languages
                    print("Invalid option. Please choose a valid option.")
                
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__": # If the file is named main.py, this code will run. Being the same name as the function is just a convention, it can be named differently.
    main()