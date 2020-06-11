import shlex
import sys
from decimal import Decimal,getcontext

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
            if x == "^":
                result = eval(repr(Decimal(remainder[0])) + "**" + repr(Decimal(remainder[1])))
            else:
                result = eval(repr(Decimal(remainder[0])) + str(x) + repr(Decimal(remainder[1])))
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

# ------------------------------------------------------------------------------
#                     '>' , '<' , '=' (Symbols)
# ------------------------------------------------------------------------------

def verify_equality(expr):
    calculus1 = shlex.shlex(expr[0], punctuation_chars=True)
    calculus1.wordchars = calculus1.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")

    calculus2 = shlex.shlex(expr[1], punctuation_chars=True)
    calculus2.wordchars = calculus2.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")

    return True if str(eval_(parse(calculus1))) == str(eval_(parse(calculus2))) else False

# ------------------------------

def verify_greater_than(expr):
    calculus1 = shlex.shlex(expr[0], punctuation_chars=True)
    calculus1.wordchars = calculus1.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")

    calculus2 = shlex.shlex(expr[1], punctuation_chars=True)
    calculus2.wordchars = calculus2.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")

    return True if float(eval_(parse(calculus1))) > float(eval_(parse(calculus2))) else False

# ------------------------------

def verify_less_than(expr):
    calculus1 = shlex.shlex(expr[0], punctuation_chars=True)
    calculus1.wordchars = calculus1.wordchars.replace("-", "").replace("/", "").replace("*", "")

    calculus2 = shlex.shlex(expr[1], punctuation_chars=True)
    calculus2.wordchars = calculus2.wordchars.replace("-", "").replace("/", "").replace("*", "")

    return True if float(eval_(parse(calculus1))) < float(eval_(parse(calculus2))) else False
