def sum_numbers(numbers=None):
    sum = 0
    if numbers == None:
        for i in range(1,101):
            sum += i
    else:
        for i in numbers:
            sum += int(i)
    return sum
