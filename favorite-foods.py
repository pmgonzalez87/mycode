#!/usr/bin/env python3

#Print lists 

# Create Fave Mex Food List
faveMexFood = [ "Enchiladas", "Tacos", "Chilaquiles" ]

# Create Fave Desserts List 
faveDesserts = [ "Sundaes", "Apple Pie", "Creme Brulee" ]

# create Fave Fruits List
faveFruits = [ "Papaya", "Dragonfrut", "Jackfruit" ]

faveMexFood.extend(faveDesserts)
faveMexFood.append(faveFruits)

# Print my list of favorite foods and specifics items from the list
print( "My Favorite Foods: " + str(faveMexFood ))
print( "My top three favorite foods are: " + str(faveMexFood[1]) + str(faveMexFood[5]) + str(faveMexFood[6]) )

# create a dictionary of sealife
shark = { "Type": "fish", "Diet": "fish", "Tail-type": "vertical", "BreathesAir":False }

dolphin = { "Type": "mammal", "Diet": "fish", "Tail-type": "horizontal", "BreathesAir":True }

# print keys
print(shark.keys())
print(dolphin.keys())

# pritn values
print(shark.values())
print(dolphin.values())
