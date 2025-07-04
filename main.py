todo_list = []

import json

def save_to_json():
    with open("todo.json", "w", encoding="utf-8") as f:
        json.dump(todo_list, f, ensure_ascii=False, indent=2)

def load_from_json():
    global todo_list
    try:
        with open("todo.json", "r", encoding="utf-8") as f:
            todo_list = json.load(f)
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
        return 0
    else:
        for idx, item in enumerate(todo_list, 1):
            print(f"{idx}. {item}")

def add_todo():
    task = input("請輸入代辦事項：")
    todo_list.append(task)
    print("新增完成")

def delete_todo():
    if show_todos() == 0:
        return
    try:
        index = int(input("請輸入要刪除的編號：")) - 1
        if 0 <= index < len(todo_list):
            removed = todo_list.pop(index)
            print(f"已刪除：{removed}")
        else:
            print("無效編號")
    except ValueError:
        print("請輸入正確數字")

load_from_json()

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
        save_to_json()
        print("Bye~")
        break
    else:
        print("請輸入正確選項！")