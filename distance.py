#A vehicle needs 10 times the amount of fuel than the distance it travels. However, it must always carry a minimum of 100 fuel before setting off.

#Create a function which calculates the amount of fuel it needs, given the distance.

def calculate_fuel(distance):
    # Minimum fuel required before setting off is 100 units
    minimum_fuel = 100
    
    # Calculate the amount of fuel needed (10 times the distance or the minimum_fuel, whichever is greater)
    fuel_needed = max(distance * 10, minimum_fuel)
    
    return fuel_needed

# Test the function with an example distance
distance_traveled = 50
fuel_required = calculate_fuel(distance_traveled)
print(f"The amount of fuel needed for a distance of {distance_traveled} units is: {fuel_required} units")
