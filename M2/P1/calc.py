def main():
    print("Calculator CLI. Type 'help' for commands. Type 'exit' to quit.")

    OPS = {
        "add": lambda a, b: a + b,
        "sub": lambda a, b: a - b,
        "mul": lambda a, b: a * b,
        "div": lambda a, b: a / b,
    }

    history = []

    while True:
        raw = input("calc> ").strip()
        if not raw:
            continue
        if raw in ("exit", "quit"):
            print("Bye.")
            break
        if raw == "help":
            print("Available commands:")
            print("add <a> <b> - Add two numbers")
            print("sub <a> <b> - Subtract b from a")
            print("mul <a> <b> - Multiply two numbers")
            print("div <a> <b> - Divide a by b")
            print("history     - Show operation history")
            print("help        - Show this help message")
            print("exit/quit   - Exit calculator")
            continue
        if raw == "history":
            if not history:
                print("No operations yet.")
            else:
                print("History:")
                for i, (cmd, result) in enumerate(history, 1):
                    print(f"  {i}. {cmd} = {result}")
            continue
        
        try:
            tokens = raw.split()
            cmd = tokens[0].lower()
            args = tokens[1: ]
        
            def parse_number(token: str):
                try:
                    if token.isdigit() or (token.startswith("-") and token[1:].isdigit()):
                        return int(token)
                    return float(token)
                except ValueError:
                    raise ValueError(f"Invalid number: {token}")
        
            func = OPS[cmd]
            a = parse_number(args[0])
            b = parse_number(args[1])
            result = func(a, b)
            print(result)
            history.append((raw, result))
            
        except Exception as e:
            print(f"Error: {e}")
            continue        
            
main()