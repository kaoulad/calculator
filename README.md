# calculator

Basic calculator written in Python using Shunting-yard algorithm.

### Pre-requiste
- python (> 3)
- prompt_toolkit (library)

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
parse(l_calc)
```

And thanks to reverse polish notation, the program can easily evaluate mathematical expression.

```py
eval_(parse(l_calc))
```

# Features
### Operations
- [ ] [Addition](#addition)
- [ ] [Substraction](#substraction)
- [ ] [Multiplication](#multiplication)
- [ ] [Division](#division)
- [ ] [Power](#power)
- [ ] [Mixed](#mixed)

### Commands
- [ ] [Exit program](#exit)
- [ ] [calculator history](#history)
- [ ] [Clear Input](#clear)

---

## Operations
<div id ="addition">

**Addition**
```
sy) 5+7+4
16
```
</div>

---

<div id ="substraction">

**Substraction**
```
sy) 10-20-40
-50
```
</div>

---

<div id="multiplication">

**Multiplication**
```
sy) 5*2*3
30
```
</div>

---

<div id ="division">

**Division**
```
sy) 100/10
10.0
```
</div>

---

<div id="power">

**Squared**
```
sy) 5^2
25
```

**Cubed**
```
sy) 10^3
1000
```

**Root square**
```
sy) 25^0.5
5.0
```

</div>

---

<div id="mixed">

**Mixed**
```
sy) (5+5*2/4-2)^2
30.25
```
</div>

--- 

## Additional commands

<div id="exit">

To exit the program.
```
sy) quit
```

</div>

---

<div id="history">

Go back to an old calculus with up arrow key.
```
sy) (10+3)*2
26
sy) 6*2+3
15
sy) 6*2+3 (up arrow key)
```

Or go back to a recent calculus with bottom arrow key.
```
sy) (10+3)*2
26
sy) 6*2+3
15
sy) 6*2+3     (up arrow key)
sy) (10+3)*2  (up arrow key)
sy) 6*2+3     (bottom arrow key)
```

</div>

---

<div id="clear">
You can clear input with CTRL+L key.

```
sy) (10+3)*2
26
sy) 6*2+3
15
```

(With CTRL+L)
```
sy)
```


