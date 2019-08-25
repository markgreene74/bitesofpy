def fizzbuzz(num):
    result = ""
    if num % 3 == 0:
        result += "Fizz"
    if num % 5 == 0:
        result += "Buzz"
    if not result:
        return num
    else:
        return "Fizz Buzz" if result == "FizzBuzz" else result
