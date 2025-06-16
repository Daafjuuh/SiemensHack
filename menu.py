print("Welcome to the OT-Demo selection menu, here are the available options:")
print("[1]: Send a HTTP-POST request to the Siemens portal")
print("[2]: Run the Scanning script with added functionality to always turn the PLC off when its status is ""RUNNING""")
print("[3]: Run the Automated scanning script with added functionality to always turn the PLC off when its status is ""RUNNING"", this does not require user input")
print("--------------------------------------------------")
user_input = input("Please enter your choice: ")
if user_input != "1" and user_input != "2" and user_input != "3":
    print("Invalid input, please try again")
 
elif user_input == "1":
    import scripts.PostScript
 
elif user_input == "2":
    import scripts.AlwaysOffScript

elif user_input == "3":
    import scripts.AutomatedAlwaysOffScript
 
else:
    print("error LOL")