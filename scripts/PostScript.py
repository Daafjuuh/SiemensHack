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

    payload = {
        '"DB_HMI".Statuses.T_VULLEN': fill_time
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

    # Variabele schrijven
    resp_write = session.post(write_url, data=payload, headers=headers)

    if resp_write.status_code == 200:
        return "✅ Waarde succesvol geschreven!"
    else:
        return f"❌ Waarde schrijven mislukt: {resp_write.status_code}"
