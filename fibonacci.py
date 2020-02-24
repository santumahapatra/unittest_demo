def calculate(input):
    if not isinstance(input, int) or isinstance(input, bool) or input < 0 :
        return "WRONG INPUT"
    if input is 0 or input is 1:
        return input
    return calculate(input - 1) + calculate(input - 2)