import time
import sys
import os


print(f"Дочірній процес створений. PID: {os.getpid()}")
for i in range(1, 11):
    print(i, end=" ", flush=True)
    time.sleep(0.2)

print("\nРобота завершена. Натисніть будь-яку клавішу...")
sys.stdin.read(1)