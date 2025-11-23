"""Write a Python program to get the size, permissions, owner, device, created, last modified and last accessed date time of a specified path.""" 
import os
import sys
import time

_path = input("Please enter a path: ")

stats =os.stat(_path)

print("""
      Size:                    {}
      Permission:              {}
      Owner:                   {}
      Device:                  {}
      Created:                 {}
      Last Modified:           {}
      Last Accessed Date Time: {}
      """.format(stats[6],stats[0],stats[5],stats[2],time.ctime(stats[-1]),time.ctime(stats[-2]),time.ctime(stats[-3])))