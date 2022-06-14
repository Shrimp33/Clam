from . import preprocessing as process
import os
from .resources.locator import locate_devconsole

def build(src: str, out: str) -> int:
    path = locate_devconsole()
    process.generate_header(src)
    source = src.split('.')[-2] + "_.c"
    print(f"cd \"{out}\" \"{path}\" && cl -LD + \"{source}\"")
    os.system(f"cd \"{out}\" && \"{path}\" && cl -LD \"{source}\"")
    return 0

if __name__ == "__main__":
    build("./tests/add.c", './tests/build')
