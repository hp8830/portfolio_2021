from app import Target, Actual
from random import randint 

actualx = Actual(
    Target(randint(0,100))
)

print("Actual Score: ", 
actualx.score.target)

user_target = Target(float(input("Guess Target: ")))

user_actuals = float(input("Guess actual score: "))


print("Your actuals achieved target: ", user_target.target_achieved(actualx))

print("Your score was off by: ", actualx.difference() - user_actuals)