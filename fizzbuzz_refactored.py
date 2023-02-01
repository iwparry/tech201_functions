# FizzBuzz - Refactored

# FizzBuzz - Write program that prints numbers from 1-100
# But for multiples of 3 print "Fizz" and for multiples of 5 print "Buzz"
# For multiples of both 3 and 5 print "FizzBuzz":

def fizzbuzz(): # list of numbers from 1 to 100
    hundred = list(range(1, 101))
    for i in hundred:
        if i % 3 == 0 and i % 5 != 0:  # i is only a multiple of 3
            print("Fizz")
        elif i % 3 != 0 and i % 5 == 0:  # i is only a multiple of 5
            print("Buzz")
        elif i % 3 == 0 and i % 5 == 0:  # i is a multiple of both 3 and 5
            print("FizzBuzz")
        else:  # i is a multiple of neither 3 nor 5
            print(i)

print(fizzbuzz())






