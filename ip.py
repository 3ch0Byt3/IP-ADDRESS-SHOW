import requests

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    ip = response.json()["ip"]
    return ip

print("Your public IP address is:", get_public_ip())

import requests
from bs4 import BeautifulSoup

def get_ip_httpbin():
    response = requests

def get_ip_ipinfo():
    response = requests.get('https://ipinfo.io/ip')
    return response.text.strip()

def get_ip_ifconfigme():
    response = requests.get('https://ifconfig.me')
    return response.text.strip()

def get_ip_whatismyipaddress():
    url = 'https://whatismyipaddress.com/ip'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Attempt to locate the IP address in the page's content
    ip_address = None
    for div in soup.find_all('div', class_='ip'):
        if 'Your IP address is' in div.text:
            ip_address = div.find('span').text.strip()
            break
    
    if ip_address:
        return ip_address
    else:
        return "IP address not found"

def main():
    ip_sources = {
        'httpbin': get_ip_httpbin,
        'ipinfo': get_ip_ipinfo,
        'ifconfigme': get_ip_ifconfigme,
        'whatismyipaddress': get_ip_whatismyipaddress
    }
    
    for name, func in ip_sources.items():
        try:
            ip = func()
            print(f"Your public IP address from {name}: {ip}")
        except Exception as e:
            print(f"Failed to get IP from {name}: {e}")

if __name__ == "__main__":
    main()
