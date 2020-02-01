# https://codechalleng.es/bites/159/
def simple_calculator(calculation):
    """Receives 'calculation' and returns the calculated result,

       Examples - input -> output:
       '2 * 3' -> 6
       '2 + 6' -> 8

       Support +, -, * and /, use "true" division (so 2/3 is .66
       rather than 0)

       Make sure you convert both numbers to ints.
       If bad data is passed in, raise a ValueError.
    """
    _num1, operator, _num2 = calculation.split()

    try:
        num1 = int(_num1)
        num2 = int(_num2)
    except ValueError:
        raise ValueError("Invalid operand(s)")

    if operator == "+":
        return int(num1) + int(num2)
    elif operator == "-":
        return int(num1) - int(num2)
    elif operator == "*":
        return int(num1) * int(num2)
    elif operator == "/":
        try:
            return int(num1) / int(num2)
        except:
            raise ValueError
    else:
        raise ValueError("Invalid operator")
