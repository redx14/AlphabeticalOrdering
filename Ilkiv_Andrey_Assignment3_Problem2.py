#Andrey Ilkiv Assignment 3 Problem 2 10/05/2020 section 01

#---------------------------------------------------
#Program asks user to input three different strings
#also prints header with instructions
print('Instructions: Please enter three strings.')
String1 = input('Enter the first string:      ')
String2 = input('Enter the second string:     ')
String3 = input('Enter the thrid string:      ')
#---------------------------------------------------

#---------------------------------------------------
#prints header for sorted strings
print('' , 'Here are the strings in ascending alphabetical order:' , sep='\n')
#---------------------------------------------------

#---------------------------------------------------
#Converts Strings in to all lower case strings
FS = String1.lower()
SS = String2.lower()
TS = String3.lower()

#if statements to compare lower to higher strings and print in correct format
#alphabetically
if FS < SS and FS < TS:
    print (FS)
    if SS < TS:
        print (SS)
        print (TS)
    else:
        print (TS)
        print (SS)
if SS < FS and SS < TS:
    print (SS)
    if FS < TS:
        print (FS)
        print (TS)
    else:
        print (TS)
        print (FS)
if TS < SS and TS < FS:
    print (TS)
    if SS < FS:
        print (SS)
        print (FS)
    else:
        print (FS)
        print (SS)
        
#---------------------------------------------------
        
