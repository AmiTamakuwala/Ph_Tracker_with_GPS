import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# assigning a variable to enter number in string format.
number = input("Enter your Ph. No. with +91: ")


# assign variable for phone no. which can use as a function.
# ".parse()" function will give the details of the numbers.
phone = phonenumbers.parse(number)

# assigning variable for timezone. which give correct time of the mb. location.
time = timezone.time_zones_for_number(phone)

# assigning variable to "carrier"..
# Carrier and Region of a Phone Number: ....
#     find the carrier and region of a phone number using the geocoder and carrier functions of this module.
# when we are passing carrier function will use "en" in the parenthesis, for english language.
carr = carrier.name_for_number(phone, "en")

# assigning variable for Registration...
# that means from which region registration was done by user...
reg = geocoder.description_for_number(phone, "en")

print(number)
print(phone)
print(time)
print(carr)
print(reg)

# Program to check whether a phone number is valid or not?
valid = phonenumbers.is_valid_number(phone)

# checking possibility of a number..
possibility = phonenumbers.is_possible_number(phone)

print(valid)
print(possibility)






























