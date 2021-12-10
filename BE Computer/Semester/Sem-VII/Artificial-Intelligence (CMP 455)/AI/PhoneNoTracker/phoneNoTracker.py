# @khom
# in this session, we will learn how we can get country of any phone numbers using python.

# We need one external module "phonenumbers" 
# to install phonenumbers type "pip install phonenumbers" in your terminal.

# let's get started
import phonenumbers
from phonenumbers import geocoder

phone_number1 = phonenumbers.parse("+12136574429")
phone_number2 = phonenumbers.parse("+917294536271")
phone_number3 = phonenumbers.parse("+862234567890")
phone_number4 = phonenumbers.parse("+201234567890")
phone_number5 = phonenumbers.parse("+9779806601049")

print(geocoder.description_for_number(phone_number1, 'en'))
print(geocoder.description_for_number(phone_number2, 'en'))
print(geocoder.description_for_number(phone_number3, 'en'))
print(geocoder.description_for_number(phone_number4, 'en'))
print(geocoder.description_for_number(phone_number5, 'en'))

# sample output:
# Los Angeles, CA
# Dharampuri, Madhya Pradesh
# Tianjin
# Egypt
# Nepal