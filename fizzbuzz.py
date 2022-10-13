# fizzbuzz
def fizzbuzz(starting_number, ending_number)
    starting_number = 1
    while starting_number < ending_number:
        three = starting_number % 3
        five = starting_number % 5
        if three == five == 0:
            print("FizzBuzz")
        elif three == 0:
            print("Fizz")
        elif five == 0:
            print("Buzz")
        else:
            print(str(starting_number))


        starting_number += 1
    return "You have reached the end"
