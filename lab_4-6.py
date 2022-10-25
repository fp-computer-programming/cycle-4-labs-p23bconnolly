#lab 4-6
animal = input ("Print an animal that is allowed to bring a dish to the feast: ") 
dish = input ("print a dish that the animal is allowed to bring")
#promps the user to input an animal and dish
firstletter = animal[0]
secondletter = dish[0]
secondletter_two = dish[-1:] 
#determines if the animal can bring the dish to the feast
if (firstletter == secondletter and secondletter_two == firstletter):
    print("your animal is allowed to bring this dish to the feast")
else: 
    print("your animal is not allowed to bring this dish to the feast") 
#prints the text as to you can or cant bring the food to the feast 