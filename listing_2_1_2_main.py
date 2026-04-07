import subprocess
import os


def main():
  
    child_path = os.path.join(os.path.dirname(__file__), "listing_2_1_child.py")
    new_proc = subprocess.Popen(
        ["python", child_path], 
        creationflags=subprocess.CREATE_NEW_CONSOLE
    )

    print("Новий процес створений.\n")
    
    new_proc.wait() 
    
    print("Новий процес закінчений.\n")
    input("Натисніть Enter...")

if __name__ == "__main__":
    main()