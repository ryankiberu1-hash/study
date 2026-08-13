x = 20
for i in range(1, 20):
    if x % 3 == 0:
        print("Fizz")
    if x % 5 == 0:
        print("Buzz")
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    else:
        print(x)    