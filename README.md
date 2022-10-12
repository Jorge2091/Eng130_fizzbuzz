# FizzBuzz

In this example, we will try to create a python script to Fizz any number between 1 and 100 that is a multiple of 3 and Buzz if the number is a multiple of 5. 
for this example, we will use a while loop as it will be simple and easy to understand.
we first need to introduce a variable for the while loop to follow.
```python
number = 1
```
The we can do a while loop for the number to go from 1 to 100. This means we either use the >= or just >. For this example, we will use > and therefore means the code will be as follow:
```python
while number < 101:
    three = number % 3
    five = number % 5
```
This will take the number and find the modulus of that number. In other words, find if 3 or 5 goes to each number between 1 to 100.
<br/> If the number is a multiple of any of them, we need to print something for those specific ones. For this purpose, we will be using the if statement.
```python
    if three == five == 0:
        print("FizzBuzz")
    elif three == 0:
        print("Fizz")
    elif five == 0:
        print("Buzz")
    else:
        print(str(number))
```
With this if, elif and else, the system will select each multiple of 3 and 5 and print the unique string and then go to the second line if the number is not multiple of either 3 or 5. It is important we write the first if before any other as it will not come correctly. This is because python reads the above line first before any other, if the first line satisfy the statement, the line will be executed without looking at other lines.
<br/> To make sure the while loop doesn't go forever, and the number is increased by 1, we will put a last line under the while loop and also below the if statements as shown:
```python
    number += 1
```