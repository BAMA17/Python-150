"""
This assignment is worth ten points and by the end you should know the following:
How to convert Fahrenheit to Celsius in python.
How changing a variable can affect the rest of the code.
Using floating point to enforce floating point arithmetic.
"""

print "Problem 1-------------F to C and C to F ---------"
#The formula to convert F to C is :  C = F - 32 * (5/9)
#The formula to convert C to F is :  F = C * 9/5 + 32

orig_far = 98.6
orig_cel = 100

new_cel =(orig_far - 32) * (5.0/9) #edit these formulas to the formulas above.
new_far = orig_cel * 9/5.0 + 32 #edit these formulas to the formulas above.

print "New fahrenheit is ",new_far
print "New celsius is",new_cel

assert(new_far == 212), "Your fahrenheit equation is wrong"
assert(new_cel == 37), "Your celsius equation is wrong"

print "Problem 2------------Pizza Problem---------------"
#You have 5 friends, and you all order pizza together.
#The pizza costs 35.80, and you decide to tip 20% because you are good people.
#Guy 1 eats 30%, guy2 eats 25%, guy3 eats 20%, girl1 eats 10%, girl2 eats 15%
#Guy1 pays for both guy1 and girl1
#You are being fair, so everyone owes for the share they eat.
#Write formulas for the following variables
#USE FORMULAS, DO NOT HARDCODE IN THE ANSWER

pizza_cost = 35.80
pizza_with_tip = (pizza_cost * .20) + pizza_cost
guy1_pays = (pizza_with_tip * .40)
guy2_pays = (pizza_with_tip * .25)
guy3_pays = (pizza_with_tip * .20)
girl1_pays = 0
girl2_pays = (pizza_with_tip * .15)

print "Guy 1 pays",guy1_pays
print "Guy 2 pays",guy2_pays
print "Guy 3 pays",guy3_pays
print "Girl 1 pays",girl1_pays
print "Girl 2 pays",girl2_pays

assert(round(guy1_pays,2)==17.18), "Guy 1 formula is wrong"
assert(round(guy2_pays,2)==10.74), "Guy 2 formula is wrong"
assert(round(guy3_pays,2)==8.59), "Guy 3 formula is wrong"
assert(round(girl1_pays,2)==0), "Girl 1 formula is wrong"
assert(round(girl2_pays,2)==6.44), "Girl 2 formula is wrong"