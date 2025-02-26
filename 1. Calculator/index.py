def add(x,y):
    '''Performs the addition operation on operands
    using the (+) operator.'''
    return x + y

def difference(x,y):
    '''Performs the subtraction operation operands
    and return the output recieved after substracting 
    using the (-) operator.'''
    return x - y 

def product(x,y):
    '''returns the product i.e the multiplication of two
    operands using the (x) operator.'''
    return x * y

def divide(x,y):
    '''Returns the quotient after diving the operands using
    the (/) operator also checks for Zero division errors'''
    try: 
        return x / y
    except ZeroDivisionError as e:
        return e
    

def percentage(x,y):
    '''Finds the percentage, this one takes two 
    the percentage to find and from how much to find
    ex- 4% of 100'''
    try:
        return x / y * 100
    except ZeroDivisionError as e:
        return e
    


def calculator():
    '''Runs the calculator allows the user to perform 
    addition, substraction, percentage, divisin, multiplication'''
    run = True
    while run:
        choice = input("Do you want to use the calculator? Yes or No")
        choice = choice.lower()
        if choice == 'no':
            run = False
        else:
            try:
                num1 = float(input('Enter the number'))
                operator = input('Enter th operator:- +, -, x, ÷, % ')
                num2 = float(input('Enter the number'))

                if operator == '+':
                    return add(num1,num2)
                if operator == '-':
                    return difference(num1,num2)
                if operator == 'x':
                    return product(num1,num2)
                if operator == '÷':
                    return divide(num1,num2)
                if operator == '%':
                    return percentage(num1,num2)

            except ValueError:
                print('Numeric Value Only')
                run = False
            
calculator()