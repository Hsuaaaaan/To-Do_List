import tkinter as tk
from tkinter import messagebox
import todo_core

todo_core.load_from_json()

window = tk.Tk()
window.title("To-Do List")

def add_task():
    task = entry.get()
    if task:
        todo_core.todo_list.append({"task": task, "done": False})
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        todo_core.save_to_json()
        update_listbox()
    else:
        messagebox.showwarning("錯誤", "請輸入代辦事項")

def toggle_done():
    selection = listbox.curselection()
    if not selection:
        messagebox.showinfo("提示", "請選取一個項目")
        return
    index = selection[0]
    todo_core.todo_list[index]["done"] = not todo_core.todo_list[index]["done"]
    update_listbox()
    todo_core.save_to_json()

def delete_task():
    selection = listbox.curselection()
    if not selection:
        messagebox.showinfo("提示", "請選取要刪除的項目")
        return
    index = selection[0]
    del todo_core.todo_list[index]
    update_listbox()
    todo_core.save_to_json()

def update_listbox():
    listbox.delete(0, tk.END)
    for item in todo_core.todo_list:
        status = "✔" if item["done"] else "✘"
        listbox.insert(tk.END, f"[{status}]{item['task']}")

frame = tk.Frame(window)
frame.pack(pady=10)

entry = tk.Entry(frame, width=40)
entry.pack(side=tk.LEFT)

add_btn = tk.Button(frame, text="新增", command=add_task)
add_btn.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(window, width=50, height=10)
listbox.pack(pady=10)

btn_frame = tk.Frame(window)
btn_frame.pack(pady=10)

toggle_btn = tk.Button(btn_frame, text="✔/✘ 切換狀態", command=toggle_done)
toggle_btn.pack(side=tk.LEFT, padx=5)

delete_btn = tk.Button(btn_frame, text="🗑 刪除", command=delete_task)
delete_btn.pack(side=tk.LEFT, padx=5)

update_listbox()

window.protocol("WM_DELETE_WINDOW", lambda: (todo_core.save_to_json(), window.destroy()))

window.mainloop()