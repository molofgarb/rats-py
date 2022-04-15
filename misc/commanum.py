def commanum(numstr):
    ctr = len(numstr) - 1
    while ctr - 3 >= 0:
        ctr = ctr - 3
        numstr = numstr[:ctr + 1] + "," + numstr[ctr + 1:]
    return numstr

print(commanum("1234567890"))

