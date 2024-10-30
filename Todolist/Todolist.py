import json

def load_Tasks():
    try:
        with open('TodoData.txt', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Tasks list is empty.")
        return []

def saveTasks(Tasks):
    with open('TodoData.txt', 'w') as f:
        return json.dump(Tasks,f)
    
def displayTask(Tasks):
    for index,Task in enumerate(Tasks,start=1):
        print(f"{index}. {Task}")
 
def addTask(Tasks):
    Task = input("Enter the Task: ")
    Tasks.append({'Task':Task})
    saveTasks(Tasks)

def updateTask(Tasks):
    displayTask(Tasks)
    index = int(input("Enter Task number which you want to update: "))
    if 1 <= index <= len(Tasks):
        Task = input("Enter the Task: ")
        Tasks[index-1] = {'Task':Task}
        saveTasks(Tasks)
    else:
        print("Invalid Index selected.")

def deleteTask(Tasks):
    displayTask(Tasks)
    index = int(input("Enter Task number which you want to delete: "))
    if 1 <= index <= len(Tasks):
        del Tasks[index-1]
        saveTasks(Tasks)
    else:
        print("Invalid Index selected.")

def main():

    while True:
        Tasks = load_Tasks()
        print(f"{"*"*25} To-Do-List {"*"*25}")
        print("1. Display All Tasks: ")
        print("2. Add Task: ")
        print("3. Update Task: ")
        print("4. Delete Task: ")
        print("5. Exit from the program: ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                displayTask(Tasks)
            case '2':
                addTask(Tasks)
            case '3':
                 updateTask(Tasks)
            case '4':
                 deleteTask(Tasks)
            case '5':
                break
            case _:
                print("Invalid choice.")

    print("Program Terminated.")

if __name__ == "__main__":
    main()