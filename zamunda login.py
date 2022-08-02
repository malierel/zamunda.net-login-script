import requests
from bs4 import BeautifulSoup as bs


url = "https://zamunda.net/takelogin.php"
user = "YOUR USERNAME"
password = "YOUR PASSWORD"

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
    'origin': 'https://zamunda.net',
    'referer': 'https://zamunda.net/login.php'
}
payload = {
    "username": user,
    "password": password
}

s = requests.Session()
token = s.get(url).cookies

p = s.post(url, headers=HEADERS, data=payload)

print("Code: {}".format(p.status_code))

cookies = p.cookies
soup = bs(s.get('https://zamunda.net/bananas').text, 'html.parser')

with open("output.html", "w", encoding='utf-8') as file:
    file.write(str(soup.prettify()))

print("Finished")
