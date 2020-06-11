import shlex
import sys

# -------------------------------  Utils --------------------------------------

def isfloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

# ------------------------------------------------------------------------------
#                         Eval/Parse Functions 
# ------------------------------------------------------------------------------

def eval_(parsed):
    stack = []

    for x in parsed:
        if x.isnumeric() or isfloat(x):
            stack.append(x)
        else:
            remainder = stack[-2:]
            del stack[-2:]

            try:
                result = eval(str(remainder[0]) + ("**" if x == "^" else str(x)) + str(remainder[1]))
            except:
                sys.exit("calculus: Cannot evaluating this expression.")
                
            stack.append(result)
    
    return stack[0]

# ---------------------

def parse(calculus):
    numbers = []
    operators = []

    for x in calculus:
        if x.isnumeric() or isfloat(x):
            numbers.append(x)

        elif x == "+" or x == "-":
            
            if operators[:1] == ["*"] or operators[:1] == ["/"] or operators[:1] == ["^"]:
                i = 0
                while i < len(operators):
                    numbers.append(operators.pop(i))
                    i+1
                operators.append(x)

            elif operators[:1] == [x]:
                operators.append(x)
                numbers.append(operators.pop(0))
            else:
                operators.append(x)

        elif x == "*" or x == "/" or x == "^":

            if operators[:1] == ["^"]:
                i = 0
                while i < len(operators):
                    numbers.append(operators.pop(i))
                    i+1
                operators.append(x)
            else:
                operators.insert(0, x)            
            
        else:
            return sys.exit("calculus: Cannot parsing this expression.")

    return numbers + operators