print("\nWELCOME TO POP CHAT")
print("One of our operator will talk with you\n")
import random
#functions for random module
def randomm(listt = []):
    a = random.choice(listt)
    return a

def operator():
    net_num = randomm([1,2,3,4,5,6,7,8,9,0])#called another fucntion
    if net_num == 1:   
        print("***Network Error***")
        print("Thanks for using popchat. Love from",random_operator)
        exit()  

#email will be officialy entered here
email_input = input("Enter the email address: ")

#n will be used for condition as below
n = 0
        
for x in range(len(email_input)):
    if email_input[x] == "@" :
        n = n + 1
        #the below expression shall have all the strings before @
        name_in_email = (email_input[:email_input.index("@")])
        
#n will always be one if there is @ present in the input
if n == 1:
    #first two characetrs shouldnot be @
    if email_input[0:1] == "@" or email_input[1:2] == "@":
        print("Invalid Input")
        exit()#terminates the program
    else:
    #this is simply to check if the domain name is correct    
        myemail_ = email_input[email_input.index("@"):]
        if myemail_ != "@pop.ac.uk":
            print("Invalid Input")
            exit()
        else:
            ac_user = name_in_email
else:
        print("Invalid Input")
        exit() 

#these are our operators
operators = ["Sanji","Naruto","Goku","Bulma","Kelly","Shikshya","Sita","Emily"]
#used the random fucntion here to select a random name
random_operator = randomm(operators)

print("\nHello"+" " + ac_user.capitalize() + "." + " " + random_operator + " " + "speaking here"\
    +"."+"\n")
       
#Popchat begins    
while True:    
        ques_t = input("How May I Help You? \n-->")
        operator()
        #if input is null the loop stops
        if not ques_t:
            print("Thank You for your Valuable Time. Love from",random_operator)
            break
        else:
            #If the below words are inputted the corresponding output is shown    
            if "LIBRARY" in ques_t.upper() or "BOOK" in ques_t.upper():
                library_excuses = ["The Library Is Closed Today","The Librarian is Sick"]
                print(random.choice(library_excuses))
              
            elif "WIFI"  in ques_t.upper() or "INTERNET" in ques_t.upper() :
                net_excuses = ["WIFI is excellent across the campus","Our Wifi is stable"]            
                print(random.choice(net_excuses))
                  
            elif "DEADLINE" in ques_t.upper() or "ASSIGNMENT" in ques_t.upper():                
                work_excuses = ["Your deadline has been extended by two working days",
                "Contact Professor for latest update","Do it early and relax"]            
                print(random.choice(work_excuses))

            elif "CANTEEN" in ques_t.upper() or "FOOD" in ques_t.upper():               
                food_excuses = ["The food in canteen is both nutritious and delicious",
                "Canteen uses only best materials","You are what you eat"]           
                print(random.choice(food_excuses)) 

            elif "SPORT" in ques_t.upper() or "P.E" in ques_t.upper() :                
                sports_excuses = ["We are planning to add e-sports too",
                "We are always helping our athletes", "Mental games are good too"]           
                print(random.choice(sports_excuses))

            elif "HELP" in ques_t.upper() or "CONFUSE" in ques_t.upper():
                print("Thanks for using popchat. Love from",random_operator) 
                exit()  

            elif "BYE" in ques_t.upper() or "EXIT" in ques_t.upper():
                print("Thanks for using popchat. Love from",random_operator) 
                exit()

            else:
                random_excuses = ["Interesting","Fascinating","Not sure about it","Need to listen more"]            
                print(random.choice(random_excuses))


