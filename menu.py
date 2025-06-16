print("Welcome to the OT-Demo selection menu, here are the available options:")
print("[1]: Send a HTTP-POST request to the Siemens portal")
print("[2]: Run the Scanning script with added functionality to always turn the PLC off when its status is ""RUNNING""")
print("[3]: Run the Automated scanning script with added functionality to always turn the PLC off when its status is ""RUNNING"", this does not require user input")
print("--------------------------------------------------")
userInput = input("Please enter your choice: ")
if userInput != "1" and userInput != "2" and userInput != "3":
    print("Invalid input, please try again")
 
elif userInput == "1":
    import scripts.PostScript
 
elif userInput == "2":
    import scripts.AlwaysOffScript

elif userInput == "3":
    import scripts.AutomatedAlwaysOffScript
 
else:
    print("error LOL")