import sys

#check for errors
if len(sys.argv) < 2:
    sys.exit("too few arguments")

for arg in sys.argv[1:-1]:
    print("hello, my name is", arg)