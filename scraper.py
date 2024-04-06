from bs4 import BeautifulSoup
import requests
import re
import streamlit as st


emailsList = []

userUrl = ''

def scrape_emails():
    url = userUrl
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    urls = []

    for link in soup.find_all('a'):
        href = link.get('href')
        urls.append(href)
    
    for url in urls:
        new_url = f"https://soundcloud.com/{url}"
        # print(new_url)
        page = requests.get(new_url)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        element_list = soup.findAll('p')
        for element in element_list:
            elementTxt = element.get_text()
            emails = re.findall(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})', elementTxt)
            if emails:
                emailsList.append(emails)



st.title("soundcloud email scraper")

st.text("enter your soundcloud follower page and recieve a list of those follower's emails")

url_input = st.text_input("input your soundcloud follower url: ")

submit = st.button("submit")

if submit:
    userUrl = url_input
    scrape_emails()
   

for item in emailsList:
    st.markdown(''.join(item))

