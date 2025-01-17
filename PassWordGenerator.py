# Password must have at least 2 capital/lower case leters, 2 numbers and 2 Special characters

# Imports the random module
import random

# Initializes Variables for the different character types (Capital letters, lower case letters, numbers, Special characters)
LowLet_0=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CapLet_1=[]
for x in LowLet_0:
    CapLet_1.append(str(x).upper())
Nums_2=('1','2','3','4','5','6','7','8','9','0')
SpChar_3=('!','@','#','$','%','^','&','*','?','+')
Length=int(input("Enter a number between 8 and 12 to include 8 and 12: ")) # Receives input from the console for the length of the Password
PassWord=""

# Veries of the length entered matches the parameters
while Length > 12 or Length < 8:
    Length=int(input(f"Number you entered was {Length}. Ensure number entered is between 8 and 12 to include 8 and 12: "))

# Assigns a number to represent the different character types. 
# If that number is selected a charachter from that list  is randomly selected and it is added to the "PassWord" variable.
x=0
while x < Length:
    Ran=random.randrange(0,4)
    if Ran == 0:
        PassWord = PassWord + random.choice(LowLet_0); x=x+1
    elif Ran == 1:
        PassWord = PassWord + random.choice(CapLet_1); x=x+1
    elif Ran == 2:
        PassWord = PassWord + random.choice(Nums_2); x=x+1
    elif Ran == 3:
        PassWord = PassWord + random.choice(SpChar_3); x=x+1

                ################################

# Initializes a "counter" that counts the number of times the selected character group was added to the "PassWord" variable.
LLcounter=0
CLcounter=0
NCounter=0
SCCounter=0

for a in LowLet_0:
    if PassWord.count(a):
        LLcounter+=1

for a in CapLet_1:
    if PassWord.count(a):
        CLcounter+=1

for a in Nums_2:
    if PassWord.count(a):
        NCounter+=1

for a in SpChar_3:
    if PassWord.count(a):
        SCCounter+=1

# If ANY of the counters are greater than 2 then the "PassWord" variable will be wiped.
# tems will iteratively be added to it once again.
while SCCounter <2 or NCounter < 2 or CLcounter < 2 or LLcounter < 2:
    print(f"Password is: {PassWord}") # Prints the passwords that did not match. Just for your info.
    PassWord=""
    if Length > 12 or Length < 8:
        input(f"Number you entered was {Length}. Insure number entered is between 8 and 12 to include 8 and 12")
    else:
        x=0
        while x < Length:
            Ran=random.randrange(0,4)
            if Ran == 0:
                PassWord = PassWord + random.choice(LowLet_0); x=x + 1
            elif Ran == 1:
                PassWord = PassWord + random.choice(CapLet_1); x=x + 1
            elif Ran == 2:
                PassWord = PassWord + random.choice(Nums_2); x=x + 1
            else:
                PassWord = PassWord + random.choice(SpChar_3); x=x + 1

    LLcounter=0 
    CLcounter=0
    NCounter=0
    SCCounter=0
    for a in LowLet_0:
        if PassWord.count(a):
            LLcounter+=1
        # if LLcounter >= 2:
    for a in CapLet_1:
        if PassWord.count(a):
            CLcounter+=1
            # if CLcounter >= 2:
    for a in Nums_2:
        if PassWord.count(a):
            NCounter+=1
            # if NCounter >= 2:
    for a in SpChar_3:
        if PassWord.count(a):
            SCCounter+=1
            # if SCCounter >= 2:


print(f"Your entered length was {Length}. Actual length was {PassWord.__len__()}. Password is: {PassWord}. Type: {type(PassWord)}")
