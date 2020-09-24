# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

def factorial_calc(x):   #you may choose the name of the parameter
    y = x
    if x == 0:
        return(1)
    for count in range(x, 1, -1):
        y = y*(count-1)
    #
    return y    # be sure to return the factorial


if __name__ == '__main__':
    # Test your code with this first
    # Change the argument to try different values
    x = int(input("Pick a number and we'll give you the factorial!"))
    print(factorial_calc(x))

    # After you are satisfied with your results, use input() to prompt the user for a value:
    #num = input("Enter value to factorialize: ")
    #print(factorial_calc(int(num)))
    ###########################################################################################
