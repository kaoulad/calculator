import sys
import shlex
from decimal import Decimal

def isfloat(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

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

# ------------------------------------------------------------------------------

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

def verify_equality(calc1, calc2):
    res_calc1 = str(eval_(parse(calc1)))
    res_calc2 = str(eval_(parse(calc2)))

    return True if res_calc1 == res_calc2 else False

# ------------------------------------------------------------------------------

def verify_greater_than(calc1, calc2):
    res_calc1 = float(eval_(parse(calc1)))
    res_calc2 = float(eval_(parse(calc2)))

    return True if res_calc1 > res_calc2 else False

# ------------------------------------------------------------------------------

def verify_less_than(calc1, calc2):
    res_calc1 = float(eval_(parse(calc1)))
    res_calc2 = float(eval_(parse(calc2)))

    return True if res_calc1 < res_calc2 else False

# ------------------------------------------------------------------------------

def run():
    print("calculus - calculator written in Python by mortim")
    print("Type quit to exit.\n")
        
    n = input("calculus) ")

    while n != "quit":
        calc = shlex.shlex(n, punctuation_chars=True)
        calc.wordchars = calc.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")
        l_calc = list(calc)

        if l_calc[:1] == ['-']:
            l_calc.pop(0)
            l_calc[0] = "-"+l_calc[0]

        if "=" in l_calc:
            expr = "".join(l_calc).split("=")

            calculus1 = shlex.shlex(expr[0], punctuation_chars=True)
            calculus1.wordchars = calculus1.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")

            calculus2 = shlex.shlex(expr[1], punctuation_chars=True)
            calculus2.wordchars = calculus2.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")

            print(verify_equality(list(calculus1), list(calculus2)))

        elif ">" in l_calc:
            expr = "".join(l_calc).split(">")

            calculus1 = shlex.shlex(expr[0], punctuation_chars=True)
            calculus1.wordchars = calculus1.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")

            calculus2 = shlex.shlex(expr[1], punctuation_chars=True)
            calculus2.wordchars = calculus2.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")
            
            print(verify_greater_than(list(calculus1), list(calculus2)))

        elif "<" in l_calc:
            expr = "".join(l_calc).split("<")

            calculus1 = shlex.shlex(expr[0], punctuation_chars=True)
            calculus1.wordchars = calculus1.wordchars.replace("-", "").replace("/", "").replace("*", "")

            calculus2 = shlex.shlex(expr[1], punctuation_chars=True)
            calculus2.wordchars = calculus2.wordchars.replace("-", "").replace("/", "").replace("*", "")
            
            print(verify_less_than(list(calculus1), list(calculus2)))
            
        else:
            parsed = parse(l_calc)
            evaluated = eval_(parsed)
            print(evaluated)


        n = input("calculus) ")


# ------------------------------------------------------------------------------

run()
