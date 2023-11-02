#!/usr/bin/python3
import hidden_4

def main():
    for name in sorted(dir(hidden_4)):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    main()

