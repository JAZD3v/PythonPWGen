def PasswordGenerator(Min: int,Max: int,RecEmail: str):
    if Min > Max:
        raise Exception("The Minimum number (Min, the first entered) must be lower than the Maximum (Max, the second one entered)")
    # Password must have at least 2 capital/lower case leters, 2 numbers and 2 Special characters
    if Min < 8:
        raise Exception("The Minimum number (Min, the first entered) must be 8 or greater.")

    # Imports the random module
    import random

    # Initializes Variables for the different character types (Capital letters, lower case letters, numbers, Special characters)
    LowLet_0=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # 
    CapLet_1=[]
    for x in LowLet_0:
        CapLet_1.append(str(x).upper())
    Nums_2=('1','2','3','4','5','6','7','8','9','0') # 
    SpChar_3=('!','@','#','$','%','^','&','*','?','+') # 
    Length=int(input(f"Enter a number between {Min} and {Max} to include {Min} and {Max}. Number cannot be less than 8: ")) # Receives input from the console for the length of the Password
    print("\n")
    global PassWord
    PassWord=""
    PassWordDict={}
    Redo_Counter=0
    LLcounter=0
    CLcounter=0
    NCounter=0
    SCCounter=0
    # (THE BELOW LINE MAY NOT BE NEEDED) Verifies value entered for Length is within desired parameters for Min and Max Values
    while Length > Max or Length < Min:
        Length=int(input(f"Number you entered was {Length}. Ensure number entered is between {Min} and {Max} to include {Min} and {Max}: "))

    # Assigns a number to represent the different character types.
    # If that number is selected a charachter from that list  is randomly selected and it is added to the "PassWord" variable.
    x = 0


    # If ANY of the counters are less than 2 then the "PassWord" variable will be wiped.
    while SCCounter < 2 or NCounter < 2 or CLcounter < 2 or LLcounter < 2: # SCCounter < 2 or 
        #CurrentDigit=""
        """LLcounter=0
        CLcounter=0
        NCounter=0
        SCCounter=0
        if Redo_Counter >= 1:
            print(f"Password did not match criteria: {PassWord}") # Prints the passwords that did not match. Just for your info.
        PassWord=""
        x=0
        PassWordDict={}"""
        while x <= Length:
            if len(PassWordDict) >= 3:
                if x == Length:
                    CurrentDigit=""
                    """LLcounter=0
                    CLcounter=0
                    NCounter=0
                    SCCounter=0"""
                    if str(PassWordDict.get(f"Digit_{x - 2}")).lower() == str(PassWordDict.get(f"Digit_{x - 1}")).lower() == str(PassWordDict.get(f"Digit_{x}")).lower():
                        print(f"Password {PassWord} has matching sequential numbers.", end="\n\n")
                        print(PassWordDict, end="\n\n")
                        if LowLet_0.count(PassWordDict.get(f"Digit_{x}")):
                            LLcounter -= 1
                        if Nums_2.count(PassWordDict.get(f"Digit_{x}")):
                            NCounter -= 1
                        if CapLet_1.count(PassWordDict.get(f"Digit_{x}")):
                            CLcounter -= 1
                        if SpChar_3.count(PassWordDict.get(f"Digit_{x}")):
                            SCCounter -= 1
                        PassWord = PassWord[:-1]
                        PassWordDict.popitem()
                        x -= 1
                    else:
                        if SCCounter < 2 or SCCounter < 2 or NCounter < 2 or CLcounter < 2 or LLcounter < 2: # SCCounter < 2 or 
                            # if Redo_Counter >= 1:
                            print(f"Password did not match criteria: {PassWord}") # Prints the passwords that did not match. Just for your info.
                            PassWord = ""
                            x = 0
                            PassWordDict = {}
                            LLcounter = 0
                            CLcounter = 0
                            NCounter = 0
                            SCCounter = 0
                            Redo_Counter += 1
                        else:
                            x += 1
                else:
                    while str(PassWordDict.get(f"Digit_{x - 2}")).lower() == str(PassWordDict.get(f"Digit_{x - 1}")).lower() == str(PassWordDict.get(f"Digit_{x}")).lower():
                        print(f"Password {PassWord} has matching sequential numbers.", end="\n\n")
                        print(PassWordDict, end="\n\n")
                        if LowLet_0.count(PassWordDict.get(f"Digit_{x}")):
                            LLcounter -= 1
                        if Nums_2.count(PassWordDict.get(f"Digit_{x}")):
                            NCounter -= 1
                        if CapLet_1.count(PassWordDict.get(f"Digit_{x}")):
                            CLcounter -= 1
                        if SpChar_3.count(PassWordDict.get(f"Digit_{x}")):
                            SCCounter -= 1
                        PassWord = PassWord[:-1]
                        PassWordDict.popitem()
                        x -= 1
                    Ran=random.randrange(0,4)
                    if Ran == 0:
                        LLcounter += 1
                        CurrentDigit=random.choice(LowLet_0)
                        PassWord = PassWord + CurrentDigit; x += 1
                        PassWordDict[f"Digit_{x}"] = CurrentDigit
                    elif Ran == 1:
                        CLcounter += 1
                        CurrentDigit=random.choice(CapLet_1)
                        PassWord = PassWord + CurrentDigit; x += 1
                        PassWordDict[f"Digit_{x}"] = CurrentDigit
                    elif Ran == 2:
                        NCounter += 1
                        CurrentDigit=random.choice(Nums_2)
                        PassWord = PassWord + str(CurrentDigit); x += 1
                        PassWordDict[f"Digit_{x}"] = CurrentDigit
                    elif Ran == 3:
                        SCCounter += 1
                        CurrentDigit=random.choice(SpChar_3)
                        PassWord = PassWord + CurrentDigit; x += 1
                        PassWordDict[f"Digit_{x}"] = CurrentDigit
            else:
                Ran=random.randrange(0,4)
                if Ran == 0:
                    LLcounter += 1
                    CurrentDigit=random.choice(LowLet_0)
                    PassWord = PassWord + CurrentDigit; x += 1
                    PassWordDict[f"Digit_{x}"] = CurrentDigit
                elif Ran == 1:
                    CLcounter += 1
                    CurrentDigit=random.choice(CapLet_1)
                    PassWord = PassWord + CurrentDigit; x += 1
                    PassWordDict[f"Digit_{x}"] = CurrentDigit
                elif Ran == 2:
                    NCounter += 1
                    CurrentDigit=random.choice(Nums_2)
                    PassWord = PassWord + str(CurrentDigit); x += 1
                    PassWordDict[f"Digit_{x}"] = CurrentDigit
                elif Ran == 3:
                    SCCounter += 1
                    CurrentDigit=random.choice(SpChar_3)
                    PassWord = PassWord + CurrentDigit; x += 1
                    PassWordDict[f"Digit_{x}"] = CurrentDigit

        """for a in LowLet_0:
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
                SCCounter+=1"""




    print(f"Your entered length was {Length}. Actual length was {PassWord.__len__()}. Password is: {PassWord}. Type: {type(PassWord)}")

    # Import smtplib for the actual sending function
    import smtplib

    # Import the email modules.
    # used to represent an email message in Python.
    # You can use it to construct an email message with headers, body, and attachments, and later send it using the smtplib module.
    from email.message import EmailMessage

    msg = EmailMessage()

    # Sender also username for the password
    Sender="Sender@Domain.com"
    # Best to not save the pass words in clear text.

    # This was created with the App Password from Gmail.
    PW="PassWord"
    Subject="DO NOT SHARE INFO - Your sign-in Credentials"
    Body=f"Hello,\n\nPlease see below for your password:\n{PassWord}"
    msg.set_content(Body)
    msg['Subject'] = Subject
    msg['From'] = Sender
    msg['To'] = RecEmail


    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(Sender,PW)
        print("Logged in...")
        server.send_message(msg)
        print("Email sent successfully")
    except smtplib.SMTPAuthenticationError:
        print("Username and Password not accepted.")

# See below for a sample function call:
PasswordGenerator(9,16,"RecEmail@Domain.com")