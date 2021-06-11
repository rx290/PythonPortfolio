# Introduction

## Common mistakes which every python developer must avoid

    1. Always use if __name__ == '__main__': constructor
    2. When handling exceptions always use except Exceptions so that keyboard interrupts and other system interrupts can break the code if needed and always raise exception in try block
    3. use traceback module and traceback.print_exc() or traceback.format_exc() to get the useful traceback rather than parsing it as a variable
    4. instead of using list for in clauses use sets or hash tables
    5. never set defaults to mutable objects in methods
    6. Always use ternary conditions when using simple logics example:
        if condition:
            x = 0
        else:
            x =1 
        to this x = 1 if condition else 0
    7. use '_' to separate values for int and float and when print use string format for better readability f'{total:,}'
    8. always use context managers to manage your resources
    9. 