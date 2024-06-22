import random
import string
import requests
import os
from termcolor import colored

print(colored('''
░██████╗░██╗░░██╗░█████╗░░██████╗████████╗██╗░░░██╗
██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝╚██╗░██╔╝
██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░░╚████╔╝░
██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░░░╚██╔╝░░
╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░░░░██║░░░
░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░
''', 'blue'))

def ghostygen():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return code

def ghostysave(links, filename):
    with open(filename, 'w') as file:
        for link in links:
            file.write(link + '\n')

def ghostycheck(code):
    url = f"https://discord.com/api/v9/entitlements/gift-codes/{code}?country_code=GB&payment_source_id=1245278692977152051&with_application=true&with_subscription_plan=true"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return True
        elif response.status_code == 404 and response.json().get('code') == 10038:
            return False
    except requests.RequestException:
        pass
    return False

def main():
    numlink = int(input("Enter the number of links to generate: "))
    codes = [ghostygen() for _ in range(numlink)]
    links = [f"https://discord.com/gifts/{code}" for code in codes]
    ghostysave(links, 'ghosty_links.txt')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored('''
░██████╗░██╗░░██╗░█████╗░░██████╗████████╗██╗░░░██╗
██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝╚██╗░██╔╝
██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░░╚████╔╝░
██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░░░╚██╔╝░░
╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░░░░██║░░░
░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░
''', 'blue'))
    
    checklinks = input("Do you want to check the links? (yes/no or y/n): ").strip().lower()
    
    if checklinks in ['yes', 'y']:
        validlinks = []
        invalidlinks = []
        
        for code in codes:
            if ghostycheck(code):
                validlinks.append(f"https://discord.com/gifts/{code}")
            else:
                invalidlinks.append(f"https://discord.com/gifts/{code}")
        
        ghostysave(validlinks, 'valids.txt')
        ghostysave(invalidlinks, 'invalids.txt')
        
        print("Check complete. Valid links saved to valids.txt, invalid links saved to invalids.txt.")

if __name__ == "__main__":
    main()
