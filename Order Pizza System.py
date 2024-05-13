def menu():
        option = 1
        output = False
        while output == False:
                print"======================================\n"
                print"Welcome to Home Pizza!"
                print"======================================\n"
                print "1. Enfield"
                print "2. Whetsone"
                print "3. Barnet"
                print "4. Hendon"
                print "5. North Finchley\n"
                print "Press 'Q' to quit...\n"
                option = input("Select your location {1-5}\n")
                if option in (1, 2, 3, 4, 5): 
                        location = option
                        output=True
                        print"======================================"
                        address = raw_input("\nType your delivery address: ")
                        while True:
                                try:
                                        address =(raw_input('Confirm your delivery address: ') or address)
                                        break
                                except ValueError:
                                        print 'Invalid Input'
                        print"======================================\n"
                        print "1. Small 9inches (6 Slices)"
                        print "2. Medium 11.5inches (8 Slices)"
                        print "3. Large 13.5inches (10 Slices)"
                        print "4. Max 15inches (12 Slices)\n"
                        print "5. Main Menu"
                        option = input("\nSelect pizza size {1-4}\n")
                        if option in (1, 2, 3, 4):
                                size = option
                                output=True
                                print"======================================\n"
                                print "1. Meataroni"
                                print "2. Cheese and Tomato"
                                print "3. Cheese and Garlic"
                                print "4. Hawaiian Dream"
                                print "5. Farmhouse Classic"
                                print "6. Perfect Pepperoni"
                                print "7. Vegetarian Perfection"
                                print "8. Chicken BBQ Sizzler"
                                print "9. Coriander Chilli Chicken\n"
                                print "10. Main Menu"
                                option = input("\nSelect your pizza topping {1-9}\n")
                                if option in (1, 2, 3, 4, 5, 6, 7, 8, 9):
                                        topping = option
                                        output=True
                                        print"======================================"
                                        amount = input("\nHow many of this selected pizza do you want?: ")
                                        while True:
                                                try:
                                                        amount =int(input('Confirm how mny of this selected pizza that you want: ') or amount)
                                                        break
                                                except ValueError:
                                                        print 'Invalid Input'
                                        print"======================================\n"
                                else:
                                        print"Invalid Input"
                                        output=False
                        else:
                                print"Invalid Input"
                                output=False
                else:
                        print"Invalid Input"
                        output= False
        option = 1

        if topping == 1:
                if size == 1: print "Your order costs " + u"\u00A3" + str (amount*6.50) + " and will be delivered to " + str (address)
                elif size == 2: print "Your order costs " + u"\u00A3" + str (amount*8.50) + " and will be delivered to " + str (address)
                elif size == 3: print "Your order costs " + u"\u00A3" + str (amount*10.50) + " and will be delivered to " + str (address)
                elif size == 4: print "Your order costs " + u"\u00A3" + str (amount*12.50) + " and will be delivered to " + str (address)
                return option                       
        elif topping == 2:
                if size == 1: print "Your order costs " + u"\u00A3" + str (amount*5.80) + " and will be delivered to " + str (address)
                elif size == 2: print "Your order costs " + u"\u00A3" + str (amount*7.80) + " and will be delivered to " + str (address)
                elif size == 3: print "Your order costs " + u"\u00A3" + str (amount*9.80) + " and will be delivered to " + str (address)                         
                elif size == 4: print "Your order costs " + u"\u00A3" + str (amount*11.80) + " and will be delivered to " + str (address)
                return option
        elif topping == 3:
                if size == 1: print "Your order costs " + u"\u00A3" + str (amount*5.80) + " and will be delivered to " + str (address)
                elif size == 2: print "Your order costs " + u"\u00A3" + str (amount*7.80) + " and will be delivered to " + str (address)
                elif size == 3: print "Your order costs " + u"\u00A3" + str (amount*9.80) + " and will be delivered to " + str (address)                         
                elif size == 4: print "Your order costs " + u"\u00A3" + str (amount*11.80) + " and will be delivered to " + str (address)
                return option
        elif topping == 4:
                if size == 1: print "Your order costs " + u"\u00A3" + str (amount*6.50) + " and will be delivered to " + str (address)
                elif size == 2: print "Your order costs " + u"\u00A3" + str (amount*8.50) + " and will be delivered to " + str (address)
                elif size == 3: print "Your order costs " + u"\u00A3" + str (amount*10.50) + " and will be delivered to " + str (address)
                elif size == 4: print "Your order costs " + u"\u00A3" + str (amount*12.50) + " and will be delivered to " + str (address) 
                return option  
        elif topping == 5:
                if size == 1: print "Your order costs " + u"\u00A3" + str (amount*6.70) + " and will be delivered to " + str (address)
                elif size == 2: print "Your order costs " + u"\u00A3" + str (amount*8.70) + " and will be delivered to " + str (address)
                elif size == 3: print "Your order costs " + u"\u00A3" + str (amount*10.70) + " and will be delivered to " + str (address)
                elif size == 4: print "Your order costs " + u"\u00A3" + str (amount*12.70) + " and will be delivered to " + str (address) 
                return option  
        elif topping == 6:
                if size == 1: print "Your order costs " + u"\u00A3" + str (amount*7) + " and will be delivered to " + str (address)
                elif size == 2: print "Your order costs " + u"\u00A3" + str (amount*9) + " and will be delivered to " + str (address)
                elif size == 3: print "Your order costs " + u"\u00A3" + str (amount*11) + " and will be delivered to " + str (address)
                elif size == 4: print "Your order costs " + u"\u00A3" + str (amount*13) + " and will be delivered to " + str (address)
                return option   
        elif topping == 7:
                if size == 1: print "Your order costs " + u"\u00A3" + str (amount*6.50) + " and will be delivered to " + str (address)
                elif size == 2: print "Your order costs " + u"\u00A3" + str (amount*8.50) + " and will be delivered to " + str (address)
                elif size == 3: print "Your order costs " + u"\u00A3" + str (amount*10.50) + " and will be delivered to " + str (address)
                elif size == 4: print "Your order costs " + u"\u00A3" + str (amount*12.50) + " and will be delivered to " + str (address)  
                return option
        elif topping == 8:
                if size == 1: print "Your order costs " + u"\u00A3" + str (amount*6.50) + " and will be delivered to " + str (address)
                elif size == 2: print "Your order costs " + u"\u00A3" + str (amount*8.50) + " and will be delivered to " + str (address)
                elif size == 3: print "Your order costs " + u"\u00A3" + str (amount*10.50) + " and will be delivered to " + str (address)
                elif size == 4: print "Your order costs " + u"\u00A3" + str (amount*12.50) + " and will be delivered to " + str (address)
                return option  
        elif topping == 9:
                if size == 1: print "Your order costs " + u"\u00A3" + str (amount*6) + " and will be delivered to " + str (address)
                elif size == 2: print "Your order costs " + u"\u00A3" + str (amount*8) + " and will be delivered to " + str (address)
                elif size == 3: print "Your order costs " + u"\u00A3" + str (amount*10) + " and will be delivered to " + str (address)
                elif size == 4: print "Your order costs " + u"\u00A3" + str (amount*12) + " and will be delivered to " + str (address) 
                return option

def rerun():
        run = "yes"
        while run == "yes":
                location =0
                while location ==0:
                        location = menu()
                        if location ==5:
                                return
                print"======================================\n" 
                rerun = raw_input("Do you want to make another order?\n")
                if rerun in ("y","ye","yes"):
                        continue
                elif rerun in ("n","no","nop","nope"):
                        run = "no"
                        print"Thank you for ordering"
                else:                        
                        print"Invalid Input"
        

rerun()

