import os
from subprocess import call, CalledProcessError

def build(src: str, out: str) -> int:
    call(["gcc", "-static", "-shared", "-o", out, src])