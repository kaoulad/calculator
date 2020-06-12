from shlex import shlex
from prompt_toolkit import PromptSession
import calculus as cu

def run():
    print("calculus - calculator written in Python by mortim")
    print("Type quit to exit.\n")
    session = PromptSession()
        
    n = session.prompt("calculus) ")

    while n != "quit":
        calc = shlex(cu.parenthesis(n), punctuation_chars=True)
        calc.wordchars = calc.wordchars.replace("-", "").replace("/", "").replace("*", "")
        # -------------------------------
        try: 
            print(cu.eval_(cu.parse(calc)))
        except:
            print("calculus cannot evaluate this expression.")
        
        n = session.prompt("calculus) ")


# ------------------
run()
