"""Write a Python program to find the parent's process id, real user ID of the current process and change real user ID.""" 
import os
print("Parent’s process id:",os.getppid())
uid = os.getuid()
print("User ID of the current process:", uid)
uid = 1400
os.setuid(uid)
print("User ID changed")
print("User ID of the current process:", os.getuid())