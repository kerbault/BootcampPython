import sys

argvArray = sys.argv
del argvArray[0]

strArg = " ".join(argvArray).swapcase()

print(strArg[::-1])
