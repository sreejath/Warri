__author__ = 'sreejath'
# Collatz

def number_entry():
    seed = 0
    not_entered = True
    while not_entered:
        try:
            seed = input("Please enter a whole number greater than 1")
            seed = int(seed) # This conversion is not done above
            # so that the ArithmeticError can get the actual value the user entered if the above line
            # (input = )errors out.
            if seed < 2:
                raise ArithmeticError("You entered %s, which is not a whole number greater than 1" % seed)
            not_entered = False
        except ValueError:
            print("You entered %s. This is not a whole number." % seed)
            continue
        except ArithmeticError as a:
            print(a.args[0])
            continue
    return seed


def collatz(seed):
    steps = 0
    while seed > 1:
        if seed % 2 == 0:
            seed /= 2
        else:
            seed = (seed * 3) + 1
        steps += 1
        print(seed)
    print(steps)

collatz(number_entry())