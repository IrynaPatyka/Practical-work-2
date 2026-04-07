import subprocess
import os

def run_n_parallel():
    
    child_path = os.path.join(os.path.dirname(__file__), "listing_2_1_child.py")
    
    try:
        n = int(input("Введіть кількість процесів (N) для запуску: "))
    except ValueError:
        print("Помилка: введіть число!")
        return

    processes = []

    print(f"Запуск {n} процесів...")
    for i in range(n):
     
        p = subprocess.Popen(
            ["python", child_path], 
            creationflags=subprocess.CREATE_NEW_CONSOLE
        )
        processes.append(p)
        print(f"Процес №{i+1} (PID: {p.pid}) запущено.")

    print("\nОчікування завершення всіх процесів...")
    
   
    for p in processes:
        p.wait()

    print("\nУсі процеси завершили роботу.")
    input("Натисніть Enter...")

if __name__ == "__main__":
    run_n_parallel()