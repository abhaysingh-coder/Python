import phonenumbers
from phonenumbers import geocoder,carrier,timezone
no=str(input("Enter the phone no"))
number=phonenumbers.parse(no)
region=geocoder.description_for_number(number,'en')
service_provider=carrier.name_for_number(number,'en')
valid=phonenumbers.is_possible_number(number)
possible=phonenumbers.is_possible_number(number)
print(number)
print(region)
print(service_provider)
print(valid)
print(possible)