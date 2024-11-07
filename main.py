def convert_miles_to_km(miles):
    value_in_km = miles * 0.621371
    print(f"{miles} miles = {value_in_km} km")

def menu():
    print("Welcome to the Converter")
    print("1. Convert miles to kilometers")
    print("2. Exit")
    option = input("What do you want to do ?")

    while True:
        if option == '1':
            miles = input("Enter your value in miles :")
            convert_miles_to_km(int(miles))
        elif option == '2':
            print("Goodbye :)")
            break


menu()

