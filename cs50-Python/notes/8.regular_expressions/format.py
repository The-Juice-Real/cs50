import time
import re

t1 = time.time()

name = input("What's your name? ").strip()

#The walrus operator := 

if matches := re.search(r"^ *(.+), *(.+) *$", name):
    name = matches.group(2) + " " + matches.group(1)

print(f"hello, {name}")

t2 = time.time()

print(f"total time elapsed: {round(t2 - t1)} seconds")