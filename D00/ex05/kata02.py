t = (3, 30, 2019, 9, 25)

print(str(t[3]).rjust(2, '0') + '/' + str(t[4]).rjust(2, '0') + '/' + str(t[2]),
      str(t[0]).rjust(2, '0') + ':' + str(t[1]).rjust(2, '0'))
