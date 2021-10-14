def calculator(number1, number2, operator):
    '''
    Perform User specified operation using two numbers provided by the user.
    Checks the operator to assess what operation needs to be performed and then executes the operation
    Otherwise returns false.
    operations may be addition, subtraction, division, multiplication, integer division, and power operation
    Parameters:
            number1 (float):  First number enterd by user to be used in the specified operation
            number2 (float): Second number enterd by user to be used in the specified operation
            operator (String): The operation symbol for the operation that needs to be performed. eg: '+', '-', etc
    Returns:
            result: Value after the specified ooperation is performed.
    '''
    result = 0.0
    # Using if - elif statements to identify which operation needs to be performed.
    if operator == '+':
        result = number1 + number2
    elif operator == '-':
        result = number1 - number2
    elif operator == '*':
        result = number1 * number2
    elif operator == '/':
        # To avoid error as division by zero results in an undefined value.
        try:
            result = number1 / number2
        except:
            ZeroDivisionError: result = 0
    elif operator == '**':
        result = number1 ** number2
    elif operator == '//':
        # To avoid error as division by zero results in an undefined value.
        try:
            result = number1 // number2
        except:
            ZeroDivisionError: result = 0
    else:
        return False
    return result

def parse_input():
    '''
    Pass user input to calculator()
    Asks user to enter an equation
    parses user input to obtains two number and an operator to pass to calculator() function
    casts the two numbers to float data type and checks validity of operator
    Invalid operator stops program execution and valid operator gets passed to calculator()
    '''
    # Runnning the method in a while True loop so that i can end the program execution after one iteration
    while True:
        equation = input('Enter Equation: ')
        # Spliting the equation with whitespace as delimeter to obtain number1, number2 and operator
        equation = equation.split()
        # Parsing to float because the split statemnts creates a list of Strings
        number1 = float(equation[0])
        operator = equation[1]
        # Parsing to float because the split statemnts creates a list of Strings
        number2 = float(equation[2])

        # checking if the user entered a valid operator so that the program can terminate early if operator is invalid
        if not (operator == '+' or '-' or '*' or '**' or '/' or '//'):
            break

        calculator(number1, number2, operator)
        break
