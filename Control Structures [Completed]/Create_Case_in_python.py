"""
Switch Statement in C++
switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
    
    
"""

# Simple switch would be like using dictionary for example
def switch(case):
    switch_dict = {
            'case1': 'This is case 1',
            'case2': 'This is case 2',
            'case3': 'This is case 3'
        }
        
    return switch_dict.get(case, 'This is the default case')
