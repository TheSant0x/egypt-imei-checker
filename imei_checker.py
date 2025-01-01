import requests
from re import sub

url = "https://api-citizens-prod-imei.gs-ef.com/ceirimeicheck/api/v1/imei/check"

def print_separator():
    print("\n" + "-" * 48 + "\n")

while True:
    imei_number = input("Enter IMEI (or 'q' to quit): ").strip()
    if imei_number.lower() == 'q': break
    imei_number = sub(r'\s+', '', imei_number)

    if len(imei_number) not in [15, 16] or not imei_number.isdigit():
        print("Invalid IMEI. Please enter a valid IMEI number.\n")
        continue

    print_separator()
    print(f"Processed IMEI: {imei_number}")
    print_separator()

    try:
        response = requests.post(url, json={"imeiNumber": [imei_number]})
        if response.status_code == 200:
            result = response.json()

            status = result['result']['status']
            active = result['result']['active']
            model = result['result']['model']
            number_of_trials = result['result']['numberOfTrialsLeft']
            amount = result['result'].get('amount', 'N/A')

            if status == 'REGISTERED' and active == 'ACTIVE':
                print(f"Device: {model}")
                print(f"Status: Active & Registered")
                print(f"Trials Left: {number_of_trials}")
            elif status == 'UNREGISTERED' and active == 'ACTIVE':
                print(f"Device: {model}")
                print(f"Status: Unregistered")
                print(f"Amount: {amount} EGP")
                print(f"Trials Left: {number_of_trials}\n")
        elif "You have reached the maximum tries" in response.json().get("status", {}).get("errorMsg", ""):
            print("Max tries reached. Change your IP (VPN) or try again after 24 hours.\n")
        else:
            print("IMEI not found.\n")
    except requests.RequestException as e:
        print(f"Error: {e}\n")
    print_separator()