def multiply_list(list):
    '''
    Multiply all of the elements of a given list
    The function checks data structure type of element from the list
    Returns false if the data structure is invalid; string or boolean
    Else returns product of all elements in the list.
    Parameters:
            list (int, float): list of integers or float or both 
    Returns:
            result: Product of all elements of the list
    '''
    # Using isinstance to ensure that the list conatins valid elements i.e. digits
    result = 1
    for digit in list:
        if isinstance(digit, int or float):
            result = result * digit
        else:
            return False

    return result
