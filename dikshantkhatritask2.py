import string
print("Swallow Speed Analysis: Version 1.0")
print("")
x = 0
#Creating empty lists
num = ["1","2","3","4","5","6","7","8","9","0"]
sym = ["{","}","(",")","[","]",".",":",";","+","-","*","/","&","|","<",">","=","~","_"]
al = list(string.ascii_letters)
record = []
miles_hr = []
kms_hr = []
#Loops until the value of x crosses 1
while x <= 1:
    speed = input("Enter the Next Reading: ")
    sp = speed[1:]
    if speed == "":
        #Since, the input was none, the loops breaks as x increments
        print("No recordings entered. Nothing to do")
        x = x + 2  
    elif any(ext in al for ext in sp):
        print("Bad Input. It will not be recorded")  
    elif any(ext in sym for ext in sp):
        print("Bad Input. It will not be recorded")   
    else:
        if speed[0] == "U" or speed[0] == "E":
            if any(ext in num for ext in sp):
                print("Recording Saved")
                record.append(speed)
            
                if speed[0] == "U":
                    #speed has its beginning alphabet removed
                    nostring_britishsys = speed[1:]
                    #float_britishsys will have the variable in float number type now
                    float_britishsys = float(nostring_britishsys)
                    miles_hr.append(float_britishsys)
                    #k_h now coverts British system(miles) into European System(km)
                    kms_hr_convert = float_britishsys * 1.61
                    kms_hr.append(round(kms_hr_convert,2)) #Adding European System values into its list
                
                elif speed[0] == "E":
                    #speed has its beginning alphabet removed
                    nostrin_europeansys = speed[1:]
                    #float_europeansys will have the variable in float number type now
                    float_europeansys = float(nostrin_europeansys)   
                    kms_hr.append(float_europeansys) #Adding European System into its list
                    #Changes European system(km) into British system(miles)
                    miles_hr_convert = float_europeansys/1.61
                    miles_hr.append(round(miles_hr_convert,2)) # Adding British system values to its list
            else:
                print("Bad Input. It will not be recorded")
    
        else:
            #Bad inputs are ignored
            print("Bad Input. It will not be recorded")    

#Null inputs means no execution
if miles_hr == [] and kms_hr == []:
    exit()
else:    
    max_value_miles = max(miles_hr)#Max value from British System
    max_values_kilo = max(kms_hr)#Max value from European System
    min_values_miles = min(miles_hr)#Min value from British System
    min_values_kilo = min(kms_hr )#Min value from European System
    avg_british = sum(miles_hr)/(len(miles_hr)) #Average for both
    avg_european = sum(kms_hr)/(len(kms_hr))      

#Printing the Output
print("")
#For number of analysis
if len(record) > 1:
    print(f"{len(record)} Readings Analyzed")
else:
    print(f"{len(record)} Reading Analyzed")

#For Max Speed
print("")
print("Max Speed" +":" + " " + str(round(max_value_miles,1)) + " " \
    +"MPH" + "," + " " + str(round(max_values_kilo,1)) + " "\
    +"KPH"    )
print("")

#For Min Speed
print("Min Speed" +":" + " " + str(round(min_values_miles,1)) + " " \
    +"MPH" + "," + " " + str(round(min_values_kilo,1)) + " "\
    +"KPH"    )  
print("")

#For Average Speed
print("Avg Speed" +":" + " " + str(round(avg_british,1)) + " " \
    +"MPH" + "," + " " + str(round(avg_european,1)) + " "\
    +"KPH"    )       


      