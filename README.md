# Tech 201 Functions

Functions in Python are a great way for us to write and execute more complex code easier.

### Creating a Function
```Python
def print_something():    # Creates our function
    print("Something has been printed")    # what we want our function to do
```
We create our functions via the keyword `def` which means to define a function, following which we write our function name with a pair of parentheses at the end and a colon.
Similarly to for loops and if statements etc. functions require indentation, in which we write what we want our function to do.
Now that we've defined our function we call our function which is simply.
```python
print_something()   # "Something has been printed" will be printed to our console
```
We can call the function as much as we want, in this case we can have the string `"Something has been printed"` printed into our console anytime we call the function. Although currently there isn't much going on with the function at the moment, the way we've written it, the function is hard coded to simply print the same string over and over for every time its called. Fortunately Python allows us to create functions with arguments!
```python
def print_string(my_string):     # We have defined a function with an argument my_string
    print(my_string)              # To be executed when we call the function 

print_string("This is my string!")   # Will print the string we used as an argument here
print_string("This is my second string!")    # Will print the string we used as an argument here
```