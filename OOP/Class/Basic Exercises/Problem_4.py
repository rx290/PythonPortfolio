"""
'builtins' module provides direct access to all 'built-in' identifiers of Python.
Write a python program which import the abs() function using the builtins module, 
display the documentation of abs() function and find the absolute value of -155. 
"""

# Builtin Documentation
helpDoc_Abs = abs.__doc__
print(helpDoc_Abs)
print(abs(-155))

# As help document are not that helpful lets use IO and contextlib module to actually print out the help doc for any function needed

import contextlib
import io

class HelpDocPrinter:
  def PrintHelp(self,MethodName):
      # String IO is an in memory file-like object, it is called Memory files or String Buffers
      helpDoc = io.StringIO()
      # Redirecting sys.stout or system standard output to any Memory Files
      with contextlib.redirect_stdout(helpDoc):
          help(MethodName)
      helpDoc.seek(0)
      helpDocVar = helpDoc.read()
      return helpDocVar
  
docHelper = HelpDocPrinter()
absHelpDoc=docHelper.PrintHelp(abs)
print(absHelpDoc)