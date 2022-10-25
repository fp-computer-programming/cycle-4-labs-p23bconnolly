#lab 4-8
from msilib import sequence


dna = input("enter your 6 letter DNA sequence")
corrispondingletter = ""
# this will check each letter inputted, and give each letter a corrisponding letter 

if dna[0] == "a":
    corrispondingletter += "t"
elif dna[0] == "t":
    corrispondingletter += "a"
elif dna[0] == "c":
    corrispondingletter += "g"
elif dna[0] == "g":
    corrispondingletter += "c"

if dna[1] == "a":
    corrispondingletter += "t"
elif dna[1] == "t":
    corrispondingletter += "a"
elif dna[1] == "c":
    corrispondingletter+= "g"
elif dna[1] == "g":
    corrispondingletter += "c"

if dna[2] == "a":
    corrispondingletter += "t"
elif dna[2] == "t":
    corrispondingletter += "a"
elif dna[2] == "c":
    corrispondingletter+= "g"
elif dna[2] == "g":
    corrispondingletter += "c"

if dna[3] == "a":
    corrispondingletter += "t"
elif dna[3] == "t":
    corrispondingletter += "a"
elif dna[3] == "c":
    corrispondingletter+= "g"
elif dna[3] == "g":
    corrispondingletter += "c"

if dna[4] == "a":
    corrispondingletter += "t"
elif dna[4] == "t":
    corrispondingletter += "a"
elif dna[4] == "c":
    corrispondingletter+= "g"
elif dna[4] == "g":
    corrispondingletter += "c"

if dna[5] == "a":
    corrispondingletter += "t"
elif dna[5] == "t":
    corrispondingletter += "a"
elif dna[5] == "c":
    corrispondingletter+= "g"
elif dna[5] == "g":
    corrispondingletter += "c"

print (corrispondingletter) 
#after each letter is selected, this print statement will print the DNA string 

