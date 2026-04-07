import os
import ctypes


IDLE_PRIORITY_CLASS = 0x00000040     # Найнижчий (Lowest)
NORMAL_PRIORITY_CLASS = 0x00000020   # Звичайний (Normal)
HIGH_PRIORITY_CLASS = 0x00000080     # Високий (Highest)

def set_priority(priority_class):

    handle = ctypes.windll.kernel32.GetCurrentProcess()
    ctypes.windll.kernel32.SetPriorityClass(handle, priority_class)

def get_priority():
    handle = ctypes.windll.kernel32.GetCurrentProcess()
    return ctypes.windll.kernel32.GetPriorityClass(handle)

def main():

    print(f"Початковий пріоритет (код): {get_priority()}")


    set_priority(IDLE_PRIORITY_CLASS)
    print(f"Пріоритет змінено на Lowest (код): {get_priority()}")

 
    set_priority(HIGH_PRIORITY_CLASS)
    print(f"Пріоритет змінено на Highest (код): {get_priority()}")


    set_priority(NORMAL_PRIORITY_CLASS)
    print(f"Пріоритет повернуто до Normal")

    input("\nНатисніть Enter...")

if __name__ == "__main__":
    main()