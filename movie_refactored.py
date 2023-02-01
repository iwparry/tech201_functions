# Refactored Movie Program Task

# Rewriting the code used for our movie program from our control flow tasks to include functions

def movie_rating():
    age = input("What is your age? ")
    if age.isdigit() and int(age) > 0:
        if int(age) > 117:
            return "Nope! The oldest person in the world is 117 years old."
        elif int(age) >= 18 and int(age) <= 117:
            return "You are old enough to buy tickets for any movie"
        elif int(age) < 18 and int(age) >= 15:
            return "You can buy tickets for films rated U, PG, 12 and 15"
        elif int(age) < 15 and int(age) >= 12:
            return "You can buy tickets for films rated U, PG, and 12"
        else:
            return "You can buy tickets for any U rated films, we advise adult supervision for PG rated films"
    else:
        return "The value you've entered is invalid, please enter a digit value for your age (e.g. 12) and a realistic one!"
print(movie_rating())

