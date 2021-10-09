import random
l=["heads","tails"]
a=input("enter heads or tails :")
if a==random.choice(l):
    print("...winner...")
else:
    print("...loser...")