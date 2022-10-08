import re

def calculate(exp):
    validExpression = re.findall("\d+|[\+\-\*]", exp)
    # validOperator = re.findall("[\+\-\*]", number)
    # print(f"The numbers: {validExpression}\nThe operators: {validOperator}\nThird integer is: {int(validExpression[2])+int(validExpression[4])}")
    
    while (validExpression.count("*") > 0):
        opIndex = validExpression.index("*")
        computedValue = int(validExpression[opIndex-1])*int(validExpression[opIndex+1])
        validExpression[opIndex-1] = computedValue
        validExpression.pop(opIndex+1)
        validExpression.pop(opIndex)
    
    while (validExpression.count("+") > 0):
        opIndex = validExpression.index("+")
        computedValue = int(validExpression[opIndex-1])+int(validExpression[opIndex+1])
        validExpression[opIndex-1] = computedValue
        validExpression.pop(opIndex+1)
        validExpression.pop(opIndex)
        
    while (validExpression.count("-") > 0):
        opIndex = validExpression.index("-")
        computedValue = int(validExpression[opIndex-1])-int(validExpression[opIndex+1])
        validExpression[opIndex-1] = computedValue
        validExpression.pop(opIndex+1)
        validExpression.pop(opIndex)
    return str(validExpression[0])

    
