import requests
from bs4 import BeautifulSoup as bs
import webbrowser



url = "https://zamunda.net/takelogin.php"
user = "YOUR USERNAME"
password = "YOUR PASSWORD"
search = "YOUR SEARCH"


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77',
    'origin': 'https://zamunda.net',
    'referer': 'https://zamunda.net/login.php'
}
payload = {
    "username": user,
    "password": password
}

searchGenerated = "https://zamunda.net/bananas?search=" + \
    search.lower().replace(" ", "+")+"&page=0"

s = requests.Session()

p = s.post(url, headers=HEADERS, data=payload)

print("Code: {}".format(p.status_code))
p2 = s.get(url)

soup = bs(s.get(searchGenerated).text, 'html.parser')

with open("output.html", "w", encoding='utf-8') as file:
    file.write(str(soup.prettify()))

s.close()
print ("FINISHED")

webbrowser.open_new_tab('output.html')

