def main_menu():
        option = 1
        while option != 5:
                print raw_input("Enter name ")
                x = raw_input("Enter name")
                print ("Your name is "+x)
                print"Welcome "+x+to TravelToSun™\n"
                print"Select a Country: "
                print"1. Dominica"
                print"2. St. Lucia"
                print"3. Trinidad and Tobago"
                print"4. Martinique"
                print"5. Quit"
 
                print
 
                option = input("Please choose your option\n")
                if option == 1:
                        print "You have selected Dominica\n"
                        print "Please select your holiday package: "
                        num1 = input("Full Board ")
                        num2 = input("Half Board ")
                        num3 = input("Bed & Breakfast ")
                        num4 = input("Beds Only ")
                        num5 = input("Main Menu ")
 
                elif option == 2:
                        print
                        print "You have selected St. Lucia\n"
                        print "Please select your holiday package: "
                        num1 = input("Full Board ")
                        num2 = input("Half Board ")
                        num3 = input("Bed & Breakfast ")
                        num4 = input("Beds Only ")
                        num5 = input("Main Menu ")
 
 
                elif option == 3:
                        print
                        print "You have selected Trinidad and Tobago\n"
                        print "Please select your holiday package: "
                        num1 = input("Full Board ")
                        num2 = input("Half Board ")
                        num3 = input("Bed & Breakfast ")
                        num4 = input("Beds Only ")
                        num5 = input("Main Menu ")
 
 
                elif option == 4:
                        print
                        print "You have selected Martinique\n"
                        print "Please select your holiday package: "
                        num1 = input("Full Board ")
                        num2 = input("Half Board ")
                        num3 = input("Bed & Breakfast ")
                        num4 = input("Beds Only ")
                        num5 = input("Main Menu ")
 
                elif option == 5:
                        print "   PROGRAMME TERMINATED   "
                        print "         Goodbye!         "
main_menu()
 
def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
        while True:
                        ok = raw_input(prompt)
                        if ok in ('y', 'ye','yes'):
                                return True
                        if ok in ('n', 'no', 'nop', 'nope'):
                                return False
                        retries = retries - 1
                        if retries < 0:
                                raise IOError('refusenik user')
                        print complaint
reply = ask_ok('Now answer these questions')
if reply:
                        print "Number of people (age +12): "
                        print "Number of children (age 2-11): "
                        print "Number of children (age -2): "
else:
                        print ('Goodbye!')
 
ask_ok()

