import requests
from bs4 import BeautifulSoup


url = "https://scrapeops.io/python-web-scraping-playbook/python-fake-user-agents/"
response = requests.get(url)
html = "<h1>Python Fake User-Agents: How to Manage User Agents When Scraping</h1>"
soup = BeautifulSoup(html, 'html.parser')

h1_text = soup.find('h1').text
print(h1_text)
