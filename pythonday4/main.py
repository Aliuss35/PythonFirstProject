import random
#lists
from types import CoroutineType


boroughs = ["Manhattan", "Queens", "Brooklyn", "Bronx"]
activities = ["Empire States Building", "Statue of Liberty", "Brighton Beach", "Times Square"]
restaurants =["Masal Plus", "ABA Restaurant", "Nusr-Et Steakhouse", "Burger King"]
commutes = ["Train", "Bus", "Uber", "Bike"]
#functions
def starter_function(answer):
  
  if answer == "y":
    print("Lets get started!")
    
  else:
    print("goodbye!")
   


def borough_picker(answer):
  
  while answer == "y":
    random_number = random.randint(0,len(boroughs)-1)
    random_borough = boroughs[random_number]
    print("How about " + random_borough)
    boroughs.remove(random_borough)
    answer = input("do you want to try again?")

  
#actual code

print("Hello Welcome to Random Trip Generator!")
answer = input("Do you want to start y/n?")
starter_function(answer)

answer = input("lets start with the cities okay? y/n")
borough_picker(answer)

print("Let's continue with ")
  