from cgitb import text
import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract(page):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
    url = f"https://in.indeed.com/jobs?q=python%20developer&l=Bengaluru,%20Karnataka&start={page}&vjk=fd9650ae4e4c229d"
    r = requests.get(url=url,headers=headers)
    soup = BeautifulSoup(r.content,'html.parser')
    return soup

def transform(soup):
    divs = soup.find_all('div',class_ = 'slider_container')
    for jobs in divs:
        title = jobs.find('h2').text.strip()
        company = jobs.find('span',class_ = 'companyName' ).text.strip().replace('\n','')
        job = {
            'title' : title,
            'company' : company
        }
        joblist.append(job)
    return
joblist = []

for i in range(0,40,10):
    print('Getting info')
    c = extract(0)
    transform(c)
df = pd.DataFrame(joblist)
print(df.head())
df.to_csv('jobs.csv')
