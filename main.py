from shlex import shlex
from prompt_toolkit import PromptSession
import sy

def run():
    print("sy - An elegant calculator written in Python")
    print("Type quit to exit.\n")
    session = PromptSession()
        
    n = session.prompt("sy) ")

    while n != "quit":
        calc = shlex(sy.parenthesis(n), punctuation_chars=True)
        calc.wordchars = calc.wordchars.replace("-", "").replace("/", "").replace("*", "")
        # -------------------------------
        try: 
            print(sy.eval_(sy.parse(calc)))
        except:
            print("sy cannot evaluate this expression.")
        
        n = session.prompt("sy) ")


# ------------------
run()
