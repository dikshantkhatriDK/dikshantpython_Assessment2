#DikshantKhatri 
name = "Stop! Who would cross the \
Bridge of Death \n\
Must answer me these questions \
three, 'ere \
the other side he see.\n"
print(name)

name_of_traveller = input("What is your name? ")

if  name_of_traveller.upper() == "ARTHUR":
    #Since the name given is arthur
    print("My liege! You may pass!")

elif name_of_traveller == "":
    print("You havenot given your name")

else:
    #Since the name is other than arthur
    quest = input("What is your quest? ")

    if "GRAIL"  in quest.upper():
        firstletter_name = name_of_traveller[0]
        #Variable 'letter' contains the first digit of name

        color = input("What is your favourite colour? ") 
        
        Upper_firstletter = firstletter_name.upper()
        #Variable 'up' contains the capitalized version of varibale 'letter'
        
        Upper_color = color.upper()
        #Variable 'upp' contains the capitalized version of varibale 'c'
        if len(Upper_color) > 0:
                if Upper_firstletter in Upper_color[0]:
                    #Since the first digit of inputted color and name match
                    print("You may pass!")
                else:
                    #Since the first digit of inputted color and name donot match
                    print("Incorrect! You must now face the Gorge of Eternal Peril.") 
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")           

    else:
        print("Only those who seek the Grail may pass.")    
   
