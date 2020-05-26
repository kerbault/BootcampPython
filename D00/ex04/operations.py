import sys

argvArray = sys.argv

str_usage = "Usage: python operations.py <number1> <number2>\n" \
            "Example:\n" \
            "\tpython operations.py 10 3"

if len(argvArray) > 3:
    print("InputError: too many arguments\n" + str_usage)
elif len(argvArray) < 2:
    print(str_usage)
elif not argvArray[1].isnumeric() or not argvArray[2].isnumeric():
    print("InputError: only numbers\n" + str_usage)
else:
    n_sum = int(argvArray[1]) + int(argvArray[2])
    n_difference = int(argvArray[1]) - int(argvArray[2])
    n_product = int(argvArray[1]) * int(argvArray[2])
    if argvArray[2] == "0":
        n_quotient = "ERROR (div by zero)"
        n_remainder = "ERROR (modulo by zero)"
    else:
        n_quotient = int(argvArray[1]) / int(argvArray[2])
        n_remainder = int(argvArray[1]) % int(argvArray[2])

    print("Sum:".ljust(15, ' ') + str(n_sum) + "\n" +
          "Difference:".ljust(15, ' ') + str(n_difference) + "\n" +
          "Product:".ljust(15, ' ') + str(n_product) + "\n" +
          "Quotient:".ljust(15, ' ') + str(n_quotient) + "\n" +
          "Remainder:".ljust(15, ' ') + str(n_remainder))
