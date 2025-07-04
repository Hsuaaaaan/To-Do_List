todo_list = []

def save_to_file():
    with open("todo.txt", "w", encoding="utf-8") as f:
        for item in todo_list:
            f.write(item + "\n")

def load_from_file():
    try:
        with open("todo.txt", "r", encoding="utf-8") as f:
            for line in f:
                todo_list.append(line.strip())
    except FileNotFoundError:
        pass

def show_menu():
    print("\n--- To-Do List ---")
    print("1. 查看待辦事項")
    print("2. 新增待辦事項")
    print("3. 刪除待辦事項")
    print("4. 離開")

def show_todos():
    if not todo_list:
        print("目前沒有代辦事項")
    else:
        for idx, item in enumerate(todo_list, 1):
            print(f"{idx}. {item}")

def add_todo():
    task = input("請輸入代辦事項：")
    todo_list.append(task)
    print("新增完成")

def delete_todo():
    show_todos()
    try:
        index = int(input("請輸入要刪除的編號：")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"已刪除：{removed}")
        else:
            print("無效編號")
    except ValueError:
        print("請輸入正確數字")

load_from_file()

while True:
    show_menu()
    choice = input("請選擇功能：")
    if choice == "1":
        show_todos()
    elif choice == "2":
        add_todo()
    elif choice == "3":
        delete_todo()
    elif choice == "4":
        save_to_file()
        print("Bye~")
        break
    else:
        print("請輸入正確選項！")