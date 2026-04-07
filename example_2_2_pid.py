import os
import sys


def main():
    current_pid = os.getpid()
    
    print(f"--- Інформація про процес ---")
    print(f"PID (Ідентифікатор процесу): {current_pid}")
    print(f"Версія Python: {sys.version.split()[0]}")
    print(f"Шлях до інтерпретатора: {sys.executable}")
    
    input("\nНатисніть Enter для виходу...")

if __name__ == "__main__":
    main()