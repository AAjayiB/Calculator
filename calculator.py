import re

def calculate(exp):
    if exp:
        # checks for any non operators or digits
        if not re.search("[^\d\+\-\*]",exp):
            # checks for expressions beginning only with a single minus or not
            if re.search("^\-?\d",exp):
                # checks for expressions ending with only digits 
                if re.search("\d$", exp):
                    ############# ACTUAL OPERATIONS #############
                    validExpression = re.findall("\d+|[\+\-\*]", exp)
                    ############# Here at the moment
                    if validExpression[0] =="-":
                        validExpression[0:2]=["".join(validExpression[0:2])]

                    while (validExpression.count("*") > 0):
                        opIndex = validExpression.index("*")
                        computedValue = int(validExpression[opIndex-1])*int(validExpression[opIndex+1])
                        validExpression[opIndex-1] = computedValue
                        validExpression.pop(opIndex+1)
                        validExpression.pop(opIndex)

                    while (validExpression.count("-") > 0):
                        opIndex = validExpression.index("-")
                        computedValue = int(validExpression[opIndex-1])-int(validExpression[opIndex+1])
                        validExpression[opIndex-1] = computedValue
                        validExpression.pop(opIndex+1)
                        validExpression.pop(opIndex)
                    
                    while (validExpression.count("+") > 0):
                        opIndex = validExpression.index("+")
                        computedValue = int(validExpression[opIndex-1])+int(validExpression[opIndex+1])
                        validExpression[opIndex-1] = computedValue
                        validExpression.pop(opIndex+1)
                        validExpression.pop(opIndex)

                    print(str(validExpression[0]))

                else:
                    print("Expression cannot end with an operation")
            else:
                print("Expression cannot begin with an operation")
        else:
            print("Not a valid input")
    else:
        print("No input was entered")
