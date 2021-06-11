# This is a basic Calculator with the help of loops and functions
import os
import time


def expression_input():
    e = input("Please Enter a polynomial expression to be calculated: ")
    return e


def expression_calculator(exp):
    product_operator_index = exp.find('*')
    division_operator_index = exp.find('/')
    addition_operator_index = exp.find('+')
    subtraction_operator_index = exp.find('-')
    modulus_operator_index = exp.find('%')

    if product_operator_index > 0:
        i = float(exp[0:product_operator_index])
        j = float(exp[product_operator_index+1:])
        return i * j
    elif division_operator_index > 0:
        i = float(exp[0:division_operator_index])
        j = float(exp[division_operator_index+1:])
        if j >0:
            return i / j
        else:
            raise "Zero Division Error"
    elif addition_operator_index > 0:
        i = float(exp[0:addition_operator_index])
        j = float(exp[addition_operator_index+1:])
        return i + j
    elif subtraction_operator_index> 0:
        i = float(exp[0:subtraction_operator_index])
        j = float(exp[subtraction_operator_index+1:])
        return i - j
    elif modulus_operator_index > 0:
        i = float(exp[0:modulus_operator_index])
        j = float(exp[modulus_operator_index+1:])
        if j >0:
            return i % j
        else:
            raise "Zero Division Error"
    else:
        return "Invalid Polynomial Expression"




def runner():
    print(expression_calculator(expression_input()))
    q = input("do you want to quit? (y / n): ")
    q
    if q == 'y' or q == 'Y':
        exit()
    elif q == 'n' or q == 'N':
        os.system("clear")
        runner()
    else:
        print("Invalid Entry")
        time.sleep(2)
        print("Restarting the script")
        time.sleep(2)
        os.system("clear")
        runner() 
    
if __name__ == '__main__':
    runner()

# q = 'n'
# while q != 'y':
#     print(expression_calculator(expression_input()))
#     q = input("do you want to quit? (y / n): ")
#     q