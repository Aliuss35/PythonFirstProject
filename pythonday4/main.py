import random
from types import CoroutineType
#lists

boroughs = ["Manhattan", "Queens", "Brooklyn", "Bronx"]

activities = ["Empire States Building", "Statue of Liberty", "Brighton Beach", "Times Square"]

restaurants =["Masal Plus", "ABA Restaurant", "Nusr-Et Steakhouse", "Burger King"]

commutes = ["Train", "Bus", "Uber", "Bike"]

#ALL FUNCTIONS

def starter_function(answer):
  
  if answer == "y":
    print("Lets get started!")
    
  else:
    print("goodbye!")

def commute_picker(answer):
  while answer == 'y'or answer == 'yes' or answer == 'Yes':
    random_number = random.randint(0,len(commutes)-1)
    random_commute = commutes[random_number]
    print("How about " + random_commute)
    commutes.remove(random_commute)
    answer = input("do you want to change this? y/n: \n")

  return random_commute

def restaurant_picker(answer):
  while answer == 'y':
    random_number = random.randint(0,len(restaurants)-1)
    random_restaurant = restaurants[random_number]
    print("How about " + random_restaurant)
    restaurants.remove(random_restaurant)
    answer = input("do you want to change this? y/n: \n")

  return random_restaurant

def activity_picker(answer):

  while answer == 'y':
    random_number = random.randint(0,len(activities)-1)
    random_activity = activities[random_number]
    print("How about " + random_activity)
    activities.remove(random_activity)
    answer = input("do you want to change this? y/n: \n")

  return random_activity

def borough_picker(answer):
  
  while answer == "y":
    random_number = random.randint(0,len(boroughs)-1)
    random_borough = boroughs[random_number]
    print("How about " + random_borough)
    boroughs.remove(random_borough)
    answer = input("do you want to change this? y/n: \n")

  return random_borough

#Actual Code

print("Hello Welcome to Random Trip Generator!")
answer = input("Do you want to start y/n? ")
starter_function(answer)

while answer == "y":
  answer = input("Lets start with the cities okay? y/n")
  decided_borough = borough_picker(answer)

  answer = input("Let's continue with Activities, Shall we? y/n")
  decided_activity = activity_picker(answer)

  answer = input("Let's decide on where to eat, shall we? y/n")
  decided_restaurant = restaurant_picker(answer)

  answer = input("Let's see some transportation options, shall we? y/n")
  decided_commute = commute_picker(answer)

  print("lets have a look at your trip plan: ")
  
  print(decided_borough)
  print(decided_activity)
  print(decided_restaurant)
  print(decided_commute)

  satisfied_answer = input("Are you satisfied with the selections? y/n?")
  if satisfied_answer == "y":
    print("Enjoy your trip!")
    break
  else:
    answer = "y"
    print("Let's start over!!")
    continue

