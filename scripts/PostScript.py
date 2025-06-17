"""
This script logs into a the Siemens S7-1200 PLC web interface
and writes a value to a specific variable.

The goal is to manipulate the PLC's variable directly via HTTP POST requests.
"""
import requests

def hack_plc(username, password, fill_time):
    base_url = "http://192.168.0.1"
    login_url = f"{base_url}/FormLogin"
    write_url = f"{base_url}/awp/Demobox/Demobox+.html"

# Inloggegevens
username = input("Voer gebruikersnaam in: ")
password = input("Voer wachtwoord in: ")

# Nieuwe waardes voor de tijd om de ballon te vullen en leeg te laten (in seconden)
fill_time = input("Voer de nieuwe tijd in om de ballon te vullen (in seconden): ")
empty_time = input("Voer de nieuwe tijd in om de ballon leeg te laten (in seconden): ")

# Variabelen en waardes om te schrijven
payload_fill = {
    '"DB_HMI".Statuses.T_VULLEN': fill_time 
}

payload_empty = {
    '"DB_HMI".Statuses.T_LEGEN': empty_time
}

    session = requests.Session()
    session.verify = False  # Geen SSL-verificatie

    login_data = {
        "Redirection": "",
        "Login": username,
        "Password": password
    }

    # Login
    resp_login = session.post(login_url, data=login_data)
    if resp_login.status_code != 200:
        return f"❌ Login mislukt: {resp_login.status_code}"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": write_url
    }

# Post request om de tijd vullen variabele te schrijven
print(f"[*] Variabele schrijven naar {write_url} ...")
resp_write_fill = session.post(write_url, data=payload_fill, headers=headers)
print("Write status:", resp_write_fill.status_code)

if resp_write_fill.status_code == 200:
    print("Waarde succesvol geschreven :D")
else:
    print("Waarde schrijven mislukt >:(")

"""
---------------------------------
Nu de tijd om de ballon leeg te laten schrijven
---------------------------------
"""

# Post request om de tijd legen variabele te schrijven
print(f"[*] Variabele schrijven naar {write_url} ...")
resp_write_empty = session.post(write_url, data=payload_empty, headers=headers)
print(f"Write status:", resp_write_empty.status_code)

if resp_write_empty.status_code == 200:
    print("Waarde succesvol geschreven :D")
else:
    print("Waarde schrijven mislukt >:(")