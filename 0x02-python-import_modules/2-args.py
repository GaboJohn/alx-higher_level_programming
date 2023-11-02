#!/usr/bin/python3
import sys

def main():
    args = sys.argv[1:]
    num_args = len(args)

    if num_args > 1:
        print(f"{num_args} arguments:")
        for i, arg in enumerate(args, start=1):
            print(f"{i}: {arg}")

    elif num_args == 0:
        print("0 arguments.")

    else:
        print("1 argument:")
        print(f"1: {args[0]}")

if __name__ == "__main__":
    main()
