# calculus

Basic calculator written in Python using Shunting-yard algorithm.

### Pre-requiste
- python (> 3)

*This program might get few calculus errors*

```
python main.py
```

## How it works ?

This calculator is based on Shunting-yard algorithm that parse mathematical expressions in reverse polish notation.

```
ex: 5+6 (infix)

RPN: 5 6 + (postfix)
```

This function parses to get reverse polish notation
```py
parsed = parse(l_calc)
```

And thanks to reverse polish notation, the program can easily evaluate mathematical expression.

```py
evaluated = eval_(parsed)
```

## Examples
**Addition**
```
calculus) 5+7+4
16
```
**Substraction**
```
calculus) 10-20-40
-50
```
**Multiplication**
```
calculus) 5*2*3
30
```
**Division**
```
calculus) 100/10
10.0
```
**Squared**
```
calculus) 5^2
25
```
**Cubed**
```
calculus) 10^3
1000
```
**Root square**
```
calculus) 25^0.5
5.0
```
**Mixed**
```
calculus) 5+5*2/4-2^2
3.5
```
To exit the program.
```
calculus) quit
```

