'''
This script is designed to delete phone extensions in the VICIdial 
system one by one. When run, it prompts the user to enter a specific 
phone extension number to be deleted. After submitting the extension 
number, the script makes an API request to VICIdial to delete the 
specified phone extension. Upon completion of each deletion, the script 
asks the user if they wish to delete another extension. If the user 
responds with 'Y', the script continues and prompts for the next 
extension number. If 'N' is chosen, the script terminates.
'''


import requests

def delete_phone():
    base_url = "https://YourServer.com/vicidial/non_agent_api.php"
    common_params = {
        "source": "ANYTHING",
        "user": "6666",  #Your NON AGENT API USER / PASSWORD
        "pass": "6666",
        "server_ip": "10.118.10.27", #YOUR VICIDIAL SERVER IP
        "delete_phone": "Y",
        "function": "update_phone"
    }

    while True:
        extension = input("Enter the extension number to be deleted: ")
        delete_phone_params = common_params.copy()
        delete_phone_params["extension"] = extension

        response = requests.get(base_url, params=delete_phone_params)
        print(f"Deleting phone with extension {extension}: {response.text}")

        another = input("Do you wish to delete another extension? (Y/N): ")
        if another.upper() != 'Y':
            break

if __name__ == "__main__":
    delete_phone()
