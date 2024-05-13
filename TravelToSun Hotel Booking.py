def menu():
        output = False
        while output == False:
                print("Welcome to TravelToSun!\n")
                print("1. Spain")
                print("2. Portugal")
                print("3. Italy")
                print("4. Turkey")
                print("5. Exit")
                option = input("Please select your country^^^\n")
                if option in (1, 2, 3, 4, 5):
                        country = option
                        output=True
                        print("1. Full Board")
                        print("2. Half Board")
                        print("3. Beds Only")
                        option = input("Please select your catering option^^^\n")
                        if option in (1, 2, 3):
                                catering = option
                                output=True
                                option = input("Please enter number of people aged +12^^^\n")
                                if option in (1,2,3,4,5,6,7,8,9,10):
                                        adult = option
                                        output=True
                                else:
                                        print("Invalid input")
                                        output=False
                        else:
                                print("Invalid input")
                                output=False
                else:
                        print("Invalid input")
                        output= False

               
                        
menu()