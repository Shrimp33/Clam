import os
from windows.builder import build as wbuild
from linux.build import build as lbuild


def make(src: str, out: str) -> int:
    # If windows, use windows\build.py
    if os.name == "nt":
        wbuild(src, out)
    # If linux, use linux\build.py 
    else:
        lbuild(src, out)

def main():
    make(input("src: "), input("out: "))
    return 0

if __name__ == "__main__":
    main()