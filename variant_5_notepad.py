import customtkinter as ctk
import subprocess
import threading
import os
import time

class NotepadManagerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Варіант 5 - Notepad Manager")
        self.geometry("500x450")

        self.label = ctk.CTkLabel(self, text="Запуск N блокнотів", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        self.entry_n = ctk.CTkEntry(self, placeholder_text="Введіть кількість N")
        self.entry_n.pack(pady=10)

        self.btn_run = ctk.CTkButton(self, text="Запустити Блокноти", command=self.start_launching)
        self.btn_run.pack(pady=10)

        self.log_box = ctk.CTkTextbox(self, width=420, height=200)
        self.log_box.pack(pady=20)


    def start_launching(self):
        try:
            val = self.entry_n.get()
            if not val:
                self.log_box.insert("end", "! Помилка: поле порожнє.\n")
                return
            
            n = int(val)
            
            if n <= 0:
                self.log_box.insert("end", "! Помилка: число повинно бути більшим за 0.\n")
                return
            
            self.log_box.insert("end", f"> Запит на запуск {n} процесів...\n")
            
            for i in range(1, n + 1):
                t = threading.Thread(target=self.launch_notepad, args=(i,), daemon=True)
                t.start()
                time.sleep(0.3)  
                
        except ValueError:
            self.log_box.insert("end", "! Помилка: введіть ціле число.\n")

    def launch_notepad(self, index):
        try:
            proc = subprocess.Popen("notepad.exe")
            
            self.after(0, lambda: self.log_box.insert("end", f"[Відкрито] Блокнот №{index}\n"))
            self.log_box.see("end")
            proc.wait()
            self.after(0, lambda: self.log_box.insert("end", f"--- {index}-й Блокнот закритий! ---\n"))
            self.log_box.see("end")
            
        except Exception as e:
            self.after(0, lambda: self.log_box.insert("end", f" Помилка при запуску блокнота №{index}: {e}\n"))
        
if __name__ == "__main__":
    app = NotepadManagerApp()
    app.mainloop()