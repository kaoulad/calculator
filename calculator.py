# ------------------------------------------------------------------------------
#                         Util Function
# ------------------------------------------------------------------------------

def isnumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

# --------------------------

def parenthesis(expr):
    return expr.replace('(', '( ').replace(')', ' )')


# ------------------------------------------------------------------------------
#                         Eval Function
# ------------------------------------------------------------------------------

def eval_(parsed):
    stack = []
    
    for x in parsed:
        if isnumber(x):
            stack.append(x)
        else:
            remainder = stack[-2:]
            del stack[-2:]
            if x == "^":
                result = eval(str(remainder[0]) + "**" + str(remainder[1]))
            else:
                result = eval(str(remainder[0]) + str(x) + str(remainder[1]))

            stack.append(result)

    return stack[0]

# ------------------------------------------------------------------------------
#                         Parse Function
# ------------------------------------------------------------------------------

def priority(op):
    PRIORITY_ = {
        "+":1,
        "-":1,
        "*":2,
        "/":2,
        "^":3,
        '(':4,
        ')':4
    }
    return PRIORITY_[op]

# --------------------------

def last_element(l):
    try:
        return l[-1:][0]
    except IndexError:
        return []

# --------------------------

def parse(expr):
    _OPERATORS = ['+', '-', '*', '/', '^']
    stack      = []
    res        = []

    for x in expr:
        if x in _OPERATORS:
            while stack and priority(last_element(stack)) >= priority(x) and last_element(stack) != "(":
                res.append(stack.pop())
            stack.append(x)
        elif x == '(':
            stack.append(x)
        elif x == ')':
            while last_element(stack) != "(":
                res.append(stack.pop())

            if last_element(stack) == '(':
                stack.pop()
        else:
            res.append(x)

    return res+stack[::-1]
