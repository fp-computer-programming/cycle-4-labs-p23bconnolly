#lab_4-5 
person_1 = input ("please enter your first name: ")
#first person enters their first name, which = the vairiable person_1
person_2 = input("second person, please enter your first name: ") 
#person 2 enters their name, which is person_2
fs = "hello, {0}, my name is {1},".format (person_1,person_2) 
#this line of code provides the text, which greets person one coming from person 2.  this is possible using 0 and 1, and using person_1 and 2 as variables
print (fs) 