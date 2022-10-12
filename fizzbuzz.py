# fizzbuzz

number = 1
while number<101:
    three = number % 3
    five = number % 5
    if three == five == 0:
        print("FizzBuzz")
    elif three == 0:
        print("Fizz")
    elif five == 0:
        print("Buzz")
    else:
        print(str(number))


    number += 1
