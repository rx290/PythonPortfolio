"""Write a Python program to write a string to a buffer and retrieve the value written, at the end discard buffer memory.""" 
import io
# Write a string to a buffer
output = io.StringIO()
output.write('This will be saved in buffer')
# Retrieve the value written
print(output.getvalue())
# Discard buffer memory
output.close()