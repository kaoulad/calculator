# calculator-cli

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
- [ ] [Calculator history](#history)
- [ ] [Clear Input](#clear)

---

## Operations
<div id ="addition">

**Addition**
```
> 5+7+4
16
```
</div>

---

<div id ="substraction">

**Substraction**
```
> 10-20-40
-50
```
</div>

---

<div id="multiplication">

**Multiplication**
```
> 5*2*3
30
```
</div>

---

<div id ="division">

**Division**
```
> 100/10
10.0
```
</div>

---

<div id="power">

**Squared**
```
> 5^2
25
```

**Cubed**
```
> 10^3
1000
```

**Root square**
```
> 25^0.5
5.0
```

</div>

---

<div id="mixed">

**Mixed**
```
> (5+5*2/4-2)^2
30.25
```
</div>

--- 

## Additional commands

<div id="exit">

To exit the program.
```
> quit
```

</div>

---

<div id="history">

Go back to an old calculus with up arrow key.
```
> (10+3)*2
26

> 6*2+3
15

> 6*2+3 (up arrow key)
```

Or go back to a recent calculus with bottom arrow key.
```
> (10+3)*2
26

> 6*2+3
15

> 6*2+3     (up arrow key)

> (10+3)*2  (up arrow key)

> 6*2+3     (bottom arrow key)
```

</div>

---

<div id="clear">
You can clear input with CTRL+L key.

```
> (10+3)*2
26

> 6*2+3
15
```

(With CTRL+L)
```
>
```


