import sys

argvArray = sys.argv

if len(argvArray) == 2 and argvArray[1].isnumeric():
    argv = int(argvArray[1])
    if argv == 0:
        print("I'm Zero.")
    elif argv % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

elif len(argvArray) > 2 or argvArray[1].isnumeric() == "False":
    print("ERROR")
