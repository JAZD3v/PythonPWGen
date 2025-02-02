def PasswordGenerator(Min: int,Max: int,RecEmail: str):
    if Min > Max:
        raise Exception("The Minimum number (Min, the first entered) must be lower than the Maximum (Max, the second one entered)")
    # Password must have at least 2 capital/lower case leters, 2 numbers and 2 Special characters
    if Min < 8:
        raise Exception("The Minimum number (Min, the first entered) must be 8 or greater.")

    # Imports the random module
    import random

    # Initializes Variables for the different character types (Capital letters, lower case letters, numbers, Special characters)
    LowLet_0=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    CapLet_1=[]
    for x in LowLet_0:
        CapLet_1.append(str(x).upper())
    Nums_2=('1','2','3','4','5','6','7','8','9','0')
    SpChar_3=('!','@','#','$','%','^','&','*','?','+')
    Length=int(input(f"Enter a number between {Min} and {Max} to include {Min} and {Max}. Number cannot be less than 8: ")) # Receives input from the console for the length of the Password
    global PassWord
    PassWord=""

    # (THE BELOW LINE MAY NOT BE NEEDED) Verifies value entered for Length is within desired parameters for Min and Max Values
    while Length > Max or Length < Min:
        Length=int(input(f"Number you entered was {Length}. Ensure number entered is between {Min} and {Max} to include {Min} and {Max}: "))

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
        print(f"Password did not match criteria: {PassWord}") # Prints the passwords that did not match. Just for your info.
        PassWord=""
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

    # Import smtplib for the actual sending function
    import smtplib

    # Import the email modules.
    # used to represent an email message in Python.
    # You can use it to construct an email message with headers, body, and attachments, and later send it using the smtplib module.
    from email.message import EmailMessage

    msg = EmailMessage()
    


    Sender="Sender@Domain.com"
    # Best to not save the pass words in clear text.
    # This was created with the App Password from Gmail.
    PW="Enter Password"
    Subject="DO NOT SHARE INFO - Your sign-in Credentials"
    Body=f"Hello,\n\nPlease see below for your password.\n{PassWord}"
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
# PasswordGenerator(13,16,"User@YourDomain.com")