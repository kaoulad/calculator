from shlex import shlex
from prompt_toolkit import PromptSession
import calculator

def run():
    print("calculator - An elegant calculator written in Python")
    print("Type quit to exit.\n")
    session = PromptSession()
        
    n = session.prompt("> ")

    while n != "quit":
        calc = shlex(calculator.parenthesis(n), punctuation_chars=True)
        calc.wordchars = calc.wordchars.replace("-", "").replace("/", "").replace("*", "")
        # -------------------------------
        try: 
            print(f"{calculator.eval_(calculator.parse(calc))}\n")
        except:
            print("Cannot evaluate this expression.\n")
        
        n = session.prompt("> ")


# ------------------
run()
