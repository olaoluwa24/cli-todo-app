def main():
    tasks = []
    count = 1
    while True:
        command = input("Enter a command('quit' to exit, 'done' when a task is completed): ").lower().strip()

        if command == "quit":
            break
        elif command.startswith("add "):
            new_task = command[4:]
            tasks.append(new_task)
            print(f"Added: {new_task}")
        elif command =="view":
            for task in tasks:
                print(f"{count}. {task}")
                count +=1
        elif command.startswith("done "):
            done_task = command[5:]
            if done_task in tasks:
                tasks.remove(done_task)
                print(f"Completed: {done_task}")
            else: 
                print("Task not found")
                
        else:
            print(f"You typed: {command}")

main()