# TEN
# mpg means miles per gallon
# The formula: mpg = m / g

# Prompts the user to enter miles driven and turns it into an integer
miles = int(input("How many miles have you driven? "))

# Prompts the user to enter gallons used and turns it into an integer
gallons = int(input("How many gallons have you used? "))

# Calculates the mpg, turns it into an integer and turns it into a string
mpg = str(int(miles / gallons))

# Tells the user what the mpg is
print("The miles per gallon is " + mpg + ".")
