from bs4 import BeautifulSoup as bs
import requests
import csv
import os

scriptDir = os.path.dirname(os.path.abspath(__file__))

username = input("What is the username of the person you are trying to scrape? ")

url = "https://github.com/" + username + "?tab=repositories"
response = requests.get(url)
html_content = response.content

soup = bs(html_content, 'html.parser')


repoDict = []

for i in soup.find_all('a', itemprop='name codeRepository'):
    repoName = i.text.strip()
    repoLink = "https://github.com/" + username + "/" + repoName
    repoDict.append({'Repo Name': repoName, 'Repo Link': repoLink})

if len(repoDict) > 0:
    print("Data Found!")
else:
    print("Data was not found! Please rerun and try again!")
    exit()

response.close()

csvName = os.path.join(scriptDir, 'reposFor' + username + '.csv')

with open(csvName, 'w', newline='', encoding='utf-8') as csvFile:
    fieldnames = ['Repo Name', 'Repo Link']
    writer=  csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(repoDict)

print("Data saved to " + csvName)
