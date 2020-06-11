import shlex
from prompt_toolkit import PromptSession
import calculus_utils as cu

def run():
    print("calculus - calculator written in Python by mortim")
    print("Type quit to exit.\n")
    session = PromptSession()
        
    n = session.prompt("calculus) ")

    while n != "quit":
        calc = shlex.shlex(n, punctuation_chars=True)
        calc.wordchars = calc.wordchars.replace("-", "").replace("/", "").replace("*", "").replace("=", "")
        l_calc = list(calc)

        # -------------------------------

        if l_calc[:1] == ['-']:
            l_calc.pop(0)
            l_calc[0] = "-"+l_calc[0]

        # -------------------------------

        if "=" in l_calc:
            print(cu.verify_equality("".join(l_calc).split("=")))
        elif ">" in l_calc:
            print(cu.verify_greater_than("".join(l_calc).split(">")))
        elif "<" in l_calc:
            print(cu.verify_less_than("".join(l_calc).split("<")))
        else:
            print(cu.eval_(cu.parse(l_calc)))

        # -------------------------------

        n = session.prompt("calculus) ")


# ------------------
run()