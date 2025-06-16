"""
This script logs into a the Siemens S7-1200 PLC web interface
and writes a value to a specific variable.

The goal is to manipulate the PLC's variable directly via HTTP POST requests.
"""

import requests

base_url = "http://192.168.0.1"
login_url = f"{base_url}/FormLogin"
write_url = f"{base_url}/awp/Demobox/Demobox+.html"  

# Inloggegevens
username = input("Voer gebruikersnaam in:")
password = input("Voer wachtwoord in:")

# Variabele en waarde om te schrijven
payload = {
    '"DB_HMI".Statuses.T_VULLEN': '25' 
}

# Sessie aanmaken
session = requests.Session()
session.verify = False  # Geen SSL-verificatie

# Login data
login_data = {
    "Redirection": "",
    "Login": username,
    "Password": password
}

# Login request
print("Inloggen...")
resp_login = session.post(login_url, data=login_data)
print("Login status:", resp_login.status_code)

if resp_login.status_code != 200:
    print("Login mislukt")
    exit(1)

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": write_url
}

# Post request om de variabele te schrijven
print(f"[*] Variabele schrijven naar {write_url} ...")
resp_write = session.post(write_url, data=payload, headers=headers)
print("Write status:", resp_write.status_code)

if resp_write.status_code == 200:
    print("Waarde succesvol geschreven :D")
else:
    print("Waarde schrijven mislukt >:(")