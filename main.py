def convert_miles_to_km(miles):
    value_in_km = miles / 0.621371
    print(f"{miles} miles = {value_in_km} km")


def convert_km_to_miles(km):
    value_in_miles = km * 0.621371
    print(f"{km} km = {value_in_miles} miles")


def convert_pounds_to_kg(pounds):
    value_in_kg = pounds / 2.0462
    print(f"{pounds} pounds = {value_in_kg} kg")


def convert_kg_to_pounds(kg):
    value_in_pounds = kg * 2.0462
    print(f"{kg} kg = {value_in_pounds} pounds")

def menu():
    while True:
        print("Welcome to the Converter")
        print("1. Convert miles to kilometers")
        print("2. Convert kilometers to miles")
        print("3. Convert pounds to kilograms")
        print("4. Convert kilograms to pounds")
        print("5. Exit")

        option = input("What do you want to do ?")

        if option == '1':
            miles = input("Enter your value in miles :")
            convert_miles_to_km(int(miles))
        elif option == '2':
            km = input("Enter your value in km :")
            convert_km_to_miles(int(km))
        elif option == '3':
            pounds = input('Enter your value in pounds :')
            convert_pounds_to_kg(int(pounds))
        elif option == '4':
            kg = input('Enter your value in kilograms :')
            convert_kg_to_pounds(int(kg))
        elif option == '5':
            print("Goodbye :)")
            break


menu()

