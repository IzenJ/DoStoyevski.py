import requests
import random

# Define the URL you want to send requests to
url = "https://aizen-pr.co.il//"

# Define a list of 1000 random IP addresses
ips = [f"{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}" for i in range(1000)]

# Iterate through each IP address and send a request to the web-server
for ip in ips:
    headers = {'X-Forwarded-For': ip}
    response = requests.get(url, headers=headers)
    print(f"IP address {ip} returned status code {response.status_code}")
