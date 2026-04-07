import customtkinter as ctk
import subprocess
import os
import threading

class ProcessApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Менеджер процесів - Завдання 3")
        self.geometry("450x350")

     
        self.label = ctk.CTkLabel(self, text="Паралельний запуск процесів", font=("Arial", 20))
        self.label.pack(pady=20)

   
        self.entry = ctk.CTkEntry(self, placeholder_text="Кількість процесів (N)")
        self.entry.pack(pady=10)

      
        self.btn = ctk.CTkButton(self, text="Запустити", command=self.start_threading)
        self.btn.pack(pady=10)

      
        self.log = ctk.CTkTextbox(self, width=400, height=120)
        self.log.pack(pady=20)

    def start_threading(self):
        thread = threading.Thread(target=self.run_logic, daemon=True)
        thread.start()

    def run_logic(self):
        try:
            n = int(self.entry.get())
            child_path = os.path.join(os.path.dirname(__file__), "listing_2_1_child.py")
            
            self.btn.configure(state="disabled")
            self.log.insert("end", f"> Запуск {n} процесів...\n")
            
            procs = []
            for i in range(n):
                p = subprocess.Popen(["python", child_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
                procs.append(p)
            
            for p in procs:
                p.wait()
                
            self.log.insert("end", "> Усі процеси завершені.\n")
            self.btn.configure(state="normal")
            
        except ValueError:
            self.log.insert("end", "! Помилка: Введіть число.\n")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    app = ProcessApp()
    app.mainloop()