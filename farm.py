#In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. The farmer breeds three species:

#chickens = 2 legs
#cows = 4 legs
#pigs = 4 legs
#The farmer has counted his animals and he gives you a subtotal for each species. You have to implement a function that returns the total number of legs of all the animals.

def total_legs(chickens_count, cows_count, pigs_count):
    # Calculate the total number of legs for each species
    total_chicken_legs = chickens_count * 2
    total_cow_legs = cows_count * 4
    total_pig_legs = pigs_count * 4
    
    # Calculate the overall total number of legs
    total_legs = total_chicken_legs + total_cow_legs + total_pig_legs
    
    return total_legs

# Test the function with example subtotals
chickens_count = 5
cows_count = 3
pigs_count = 2

total_animal_legs = total_legs(chickens_count, cows_count, pigs_count)
print(f"The total number of legs among all the animals is: {total_animal_legs}")
