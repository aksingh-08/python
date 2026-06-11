def main():
    print("Calculator CLI. Type 'help' for commands. Type 'exit' to quit.")
    while True:
        raw = input("calc> ").strip()
        if not raw:
            continue
        if raw in ("exit", "quit"):
            print("Bye.")
            break

main()