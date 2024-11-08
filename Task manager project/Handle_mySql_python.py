import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Om@89281"
    )

    if conn.is_connected():
        print("Connection established.")
except mysql.connector.Error as err:
    print(f"Error: {err}")

mycursor = conn.cursor()

mycursor.execute("USE tsm")

mycursor.execute('''
    CREATE TABLE IF NOT EXISTS Tasks(
                TaskId INT PRIMARY KEY AUTO_INCREMENT,
                TaskName VARCHAR(50) NOT NULL,
                TaskDescription VARCHAR(100)             
    );''')
print("Table is created")

def showAllTasks():
    mycursor.execute("SELECT * FROM Tasks")
    myresult = mycursor.fetchall()
    if myresult:
        for task in myresult:
            print(task)
    else:
        print("Task List is empty.\n")


def AddTask(TaskName,TaskDescription):
    mycursor.execute('''INSERT INTO Tasks
                     (TaskName,TaskDescription)
                     VALUES
                     (%s,%s)''',(TaskName,TaskDescription))
    conn.commit()
    print("Task added successfully.\n")

def UpdateTask(TaskId,newTaskName,newTaskDescription):
    sql = "UPDATE Tasks SET TaskName = %s, TaskDescription = %s WHERE TaskId = %s" 
    val = (newTaskName,newTaskDescription,TaskId)

    mycursor.execute(sql,val)

    conn.commit()
    print("Task Updated successfully.\n")

def DeleteTask(TaskId):
    sql = "DELETE FROM Tasks WHERE TaskId = %s"
    val = (TaskId,)

    mycursor.execute(sql,val)

    conn.commit()
    print("Task Deleted.\n")

def main():
    while True:
        print("1.Show All Tasks")
        print("2.Add Task")
        print("3.Update Task")
        print("4.Delete Task")
        print("5.Exit")

        choice = input("Enter Your Choice: ")

        match(choice):
            case "1":
                showAllTasks()
            case "2":
                TaskName = input("Enter The Task: ")
                TaskDescription = input("Enter The Task Description: ")
                AddTask(TaskName, TaskDescription)
            case "3":
                TaskId = input("Enter The TaskID You Want Update: ")
                newTaskName = input("Enter The New Task: ")
                newTaskDescription = input("Enter New Task Description: ")
                UpdateTask(TaskId,newTaskName, newTaskDescription)
            case "4":
                TaskId = input("Enter The TaskID You Want Delete: ")
                DeleteTask(TaskId)
            case "5":
                break
        
    else:
        print("Invalid Input")


if __name__ == "__main__":
    main()
    conn.close()
