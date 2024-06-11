# # Create an empty list to store the dictionaries
# people = []

# # Input the number of people to add
# num_people = int(input("Enter the number of people to add: "))

# # Input details for each person and append to the list
# for i in range(num_people):
#     print(f"\nEnter details for person {i+1}:")
#     name = input("Name: ")
#     age = int(input("Age: "))
#     city = input("City: ")
    
#     person = {"name": name, "age": age, "city": city}
#     people.append(person)

# # Print the list of dictionaries
# print("\nList of people:")
# for person in people:
#     print(person)

# one 

people = []

num_people = int(input("Enter number of people you want to add:"))

for i in range(num_people):
    print(f"Enter details of {i+1}st person ")
    name = input("name :")
    city = input("city :")
    company = input("company name:")
    salary = int(input("company salary:"))

    person = {"name": name , "city": city , "company":company, "salary":salary}

    people.append(person)

for person in people:
    print(person)
