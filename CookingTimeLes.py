import random

print("You're cooking a Lasagna")
layers = int(input("How many layers will be in the lasagna? Assuming it take 2 minutes to make each layer.\n>"))
expectedMinutesInOven = int(input("How many minutes should the Lasagna cook? \n> "))

prepTimeInMinutes = layers * 2
totalCookingTime = expectedMinutesInOven + prepTimeInMinutes

print(f"Total time {totalCookingTime} minutes")
print(f"due to the estimated preparation time being {prepTimeInMinutes} minutes.\nAnd the total cooking time being "
      f"{expectedMinutesInOven} minutes.")

randomMinutes = random.randint(5, expectedMinutesInOven - 3)
remainingMinuteInOven = expectedMinutesInOven - randomMinutes
print(f"You coming back in {randomMinutes} minutes to find it has {remainingMinuteInOven} minutes left.")
