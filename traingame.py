def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def operandToString(operand):
    if operand == 0:
        return '+'
    if operand == 1:
        return '-'
    if operand == 2:
        return 'x'
    if operand == 3:
        return '/'

number = input('Please enter the 4 digit number: ')
print('The solutions are as follows:')
numberList = list(number)
count = 0
while count < len(numberList):
    numberList[count] = int(numberList[count])
    count = count + 1

operands = [0,0,0]

while operands[0] < 4:

    if operands[0] == 0:
        res1 = add(numberList[0],numberList[1])
    if operands[0] == 1:
        res1 = subtract(numberList[0],numberList[1])
    if operands[0] == 2:
        res1 = multiply(numberList[0],numberList[1])
    if operands[0] == 3 and numberList[1] != 0:
        res1 = divide(numberList[0],numberList[1])

    operands[1] = 0
    while operands[1] < 4:

        if operands[1] == 0:
            res2 = add(res1,numberList[2])
        if operands[1] == 1:
            res2 = subtract(res1,numberList[2])
        if operands[1] == 2:
            res2 = multiply(res1,numberList[2])
        if operands[1] == 3 and numberList[2] != 0:
            res2 = divide(res1,numberList[2])

        operands[2] = 0  
        while operands[2] < 4:
            if operands[2] == 0:
                res3 = add(res2,numberList[3])
            if operands[2] == 1:
                res3 = subtract(res2,numberList[3])
            if operands[2] == 2:
                res3 = multiply(res2,numberList[3])
            if operands[2] == 3 and numberList[3] != 0:
                res3 = divide(res2,numberList[3])
            if res3 == 10:
                print( '(' , '(' , numberList[0] , operandToString(operands[0]) , numberList[1] , ')' , operandToString(operands[1]) , numberList[2] , ')' , operandToString(operands[2]) , numberList[3])
            operands[2] = operands[2] + 1

        operands[1] = operands[1] + 1

    operands[0] = operands[0] + 1

# This section is for grouping the first 2 numbers and last two numbers eg. 5554 = (5+5) X (5-4) = 10
operands = [0,0,0]

while operands[0] < 4:

    if operands[0] == 0:
        res1 = add(numberList[0],numberList[1])
    if operands[0] == 1:
        res1 = subtract(numberList[0],numberList[1])
    if operands[0] == 2:
        res1 = multiply(numberList[0],numberList[1])
    if operands[0] == 3 and numberList[1] != 0:
        res1 = divide(numberList[0],numberList[1])

    operands[2] = 0  
    while operands[2] < 4:
        if operands[2] == 0:
            res3 = add(numberList[2],numberList[3])
        if operands[2] == 1:
            res3 = subtract(numberList[2],numberList[3])
        if operands[2] == 2:
            res3 = multiply(numberList[2],numberList[3])
        if operands[2] == 3 and numberList[3] != 0:
            res3 = divide(numberList[2],numberList[3])

        operands[1] = 0
        while operands[1] < 4:

            if operands[1] == 0:
                res2 = add(res1,res3)
            if operands[1] == 1:
                res2 = subtract(res1,res3)
            if operands[1] == 2:
                res2 = multiply(res1,res3)
            if operands[1] == 3 and res3 != 0:
                res2 = divide(res1,res3)
            if res2 == 10:
                print('(', numberList[0] , operandToString(operands[0]) , numberList[1] , ')' , operandToString(operands[1]) , '(' , numberList[2] , operandToString(operands[2]) , numberList[3] , ')')

            operands[1] = operands[1] + 1
        operands[2] = operands[2] + 1
    operands[0] = operands[0] + 1

# This section is for grouping the middle two numbers eg. 5 + ( 3 X 2 ) - 1
operands = [0,0,0]

while operands[1] < 4:

    if operands[1] == 0:
        res1 = add(numberList[1],numberList[2])
    if operands[1] == 1:
        res1 = subtract(numberList[1],numberList[2])
    if operands[1] == 2:
        res1 = multiply(numberList[1],numberList[2])
    if operands[1] == 3 and numberList[2] != 0:
        res1 = divide(numberList[1],numberList[2])

    operands[0] = 0  
    while operands[0] < 4:
        if operands[0] == 0:
            res3 = add(numberList[0],res1)
        if operands[0] == 1:
            res3 = subtract(numberList[0],res1)
        if operands[0] == 2:
            res3 = multiply(numberList[0],res1)
        if operands[0] == 3 and res2 != 0:
            res3 = divide(numberList[0],res1)

        operands[2] = 0
        while operands[2] < 4:

            if operands[2] == 0:
                res2 = add(res3, numberList[3])
            if operands[2] == 1:
                res2 = subtract(res3, numberList[3])
            if operands[2] == 2:
                res2 = multiply(res3, numberList[3])
            if operands[2] == 3 and res3 != 0:
                res2 = divide(res3, numberList[3])
            if res2 == 10:
                print(numberList[0] , operandToString(operands[0]) , '(' , numberList[1] , operandToString(operands[1]) , numberList[2] , ')' , operandToString(operands[2]) , numberList[3])

            operands[2] = operands[2] + 1
        operands[0] = operands[0] + 1
    operands[1] = operands[1] + 1

# This section is for grouping the last three numbers eg. a + ( b + c + d )
operands = [0,0,0]

while operands[1] < 4:

    if operands[1] == 0:
        res1 = add(numberList[1],numberList[2])
    if operands[1] == 1:
        res1 = subtract(numberList[1],numberList[2])
    if operands[1] == 2:
        res1 = multiply(numberList[1],numberList[2])
    if operands[1] == 3 and numberList[2] != 0:
        res1 = divide(numberList[1],numberList[2])

    operands[2] = 0  
    while operands[2] < 4:
        if operands[2] == 0:
            res3 = add(res1,numberList[3])
        if operands[2] == 1:
            res3 = subtract(res1,numberList[3])
        if operands[2] == 2:
            res3 = multiply(res1,numberList[3])
        if operands[2] == 3 and numberList[3] != 0:
            res3 = divide(res1,numberList[3])

        operands[0] = 0
        while operands[0] < 4:
            if operands[0] == 0:
                res2 = add(numberList[0], res3)
            if operands[0] == 1:
                res2 = subtract(numberList[0], res3)
            if operands[0] == 2:
                res2 = multiply(numberList[0], res3)
            if operands[0] == 3 and res3 != 0:
                res2 = divide(numberList[0], res3)
            if res2 == 10:
                print(numberList[0] , operandToString(operands[0]) , '(' , numberList[1] , operandToString(operands[1]) , numberList[2] , operandToString(operands[2]) , numberList[3] , ')')

            operands[0] = operands[0] + 1
        operands[2] = operands[2] + 1
    operands[1] = operands[1] + 1

# This section is for grouping the last three numbers eg. a + ( b + (c + d) )
operands = [0,0,0]

while operands[2] < 4:

    if operands[2] == 0:
        res1 = add(numberList[2],numberList[3])
    if operands[2] == 1:
        res1 = subtract(numberList[2],numberList[3])
    if operands[2] == 2:
        res1 = multiply(numberList[2],numberList[3])
    if operands[2] == 3 and numberList[3] != 0:
        res1 = divide(numberList[2],numberList[3])

    operands[1] = 0  
    while operands[1] < 4:
        if operands[1] == 0:
            res2 = add(numberList[1],res1)
        if operands[1] == 1:
            res2 = subtract(numberList[1],res1)
        if operands[1] == 2:
            res2 = multiply(numberList[1],res1)
        if operands[1] == 3 and res1 != 0:
            res2 = divide(numberList[1],res1)

        operands[0] = 0
        while operands[0] < 4:
            if operands[0] == 0:
                res3 = add(numberList[0], res2)
            if operands[0] == 1:
                res3 = subtract(numberList[0], res2)
            if operands[0] == 2:
                res3 = multiply(numberList[0], res2)
            if operands[0] == 3 and res3 != 0:
                res3 = divide(numberList[0], res2)
            if res3 == 10:
                print(numberList[0] , operandToString(operands[0]) , '(' , numberList[1] , operandToString(operands[1]) , '(' , numberList[2] , operandToString(operands[2]) , numberList[3], ')' , ')')

            operands[0] = operands[0] + 1
        operands[1] = operands[1] + 1
    operands[2] = operands[2] + 1