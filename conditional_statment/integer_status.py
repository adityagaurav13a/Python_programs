def status_check(number1, number2):
    """ Based on the values of number1 and number2, this function will return:

    - If both are positive, return "True".
    - If both are negative, return "True".
    - If one is positive and the other is negative, return "False".
    """
    if (number1 >= 0 and number2 >= 0)  or (number1 < 0 and number2 < 0):
        return "True"
    else:
        return "False"    

if __name__ == "__main__":
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    result = status_check(num1, num2)
    print(f"The status of the integers {num1} and {num2} is: {result}.")
    print("")
    
    #another way of calling the function
    print("another way of calling the function (Ex. status_check(0, 15)): "+ status_check(0, 15))