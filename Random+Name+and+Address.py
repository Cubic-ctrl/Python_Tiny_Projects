# faker
# importing  faker python module
from faker import Faker

#creating a function to generate a name randomly and address

fake = Faker()
name = "Name: " + fake.name()+ "\n"
address = "Address: " + fake.address()

print(name,address)
