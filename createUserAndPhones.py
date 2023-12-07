
####
"""
This script automates the process of creating and updating users in the VICIdial system. 
It prompts the user for a unique User ID and Full Name, uses these to create a new user 
based on a template, sets up phone configuration for this user, and updates user details. 
After each user creation, it asks if the user wants to create another user, allowing for 
multiple user creations in a sequence. Each step involves sending specific parameters to 
the VICIdial API and handling responses.
"""

import requests

def create_and_update_user_and_phone():
    user_id = input("Enter the User extension to be created: ")
    full_name = input("Enter the Agent's Name: ")

    base_url = "https://yourServer.com.com/vicidial/non_agent_api.php"
    common_params = {
        "source": "Working",
        "user": "6666",   # Vicidial NON API USER
        "pass": "6666"
    }
    user_phone_id = str(user_id)

    # Copy User
    yourServer.com_params = common_params.copy()
    copy_user_params.update({
        "function": "copy_user",
        "agent_user": user_phone_id,
        "agent_pass": user_phone_id,
        "source_user": "9999",              #I created a user as a template so script can copy.
        "agent_full_name": full_name
    })
    copy_user_response = requests.get(base_url, params=copy_user_params)
    print(f"Creating user {user_phone_id}: {copy_user_response.text}")

    # Create Phone
    add_phone_params = common_params.copy()
    add_phone_params.update({
        "function": "add_phone",
        "extension": user_phone_id,
        "dialplan_number": user_phone_id,
        "voicemail_id": user_phone_id,
        "phone_login": user_phone_id,
        "phone_pass": user_phone_id,
        "server_ip": "10.118.10.7",    # Enter your server IP
        "protocol": "SIP",
        "registration_password": "U22uu9YEPsmbKXN",
        "phone_full_name": "Wave 10 agents",       #Enter custom name
        "local_gmt": "-4.00",    #Edit to local GMT
        "outbound_cid": "0",
        "is_webphone": "Y",     # If you use webphone
        "template_id": "vicibox11-RTC"  # enter your own template ID
    })
    add_phone_response = requests.get(base_url, params=add_phone_params)
    print(f"Creating phone for {user_phone_id}: {add_phone_response.text}")

    # Update User
    update_user_params = common_params.copy()
    update_user_params.update({
        "function": "update_user",
        "agent_user": user_phone_id,
        "agent_pass": user_phone_id,
        "phone_login": user_phone_id,
        "phone_pass": user_phone_id
    })
    update_user_response = requests.get(base_url, params=update_user_params)
    print(f"Updating user {user_phone_id}: {update_user_response.text}")

 # Ask to create another user
        create_another = input("Do you want to create another user & phone? (Y/N): ")
        if create_another.upper() != 'Y':
            break

if __name__ == "__main__":
    create_and_update_user_and_phone()
