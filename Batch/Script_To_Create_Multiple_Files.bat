@echo off
set /p num="Number of files: "
for /l %%x in (1, 1,%num%) do (
   echo """ """ > Problem_%%x.py
)