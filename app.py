from bs4 import BeautifulSoup

import requests
import re

url = 'https://soundcloud.com/firstcirclemusic'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

# email_pattern = re.compile(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})')


element_list = soup.findAll('p')
for element in element_list:
    elementTxt = element.get_text()
    emails = re.findall(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4})', elementTxt)
    print(emails)
    
    
    

# <div class="infoStats__description" bis_skin_checked="1"></div>
#     <div class="truncatedUserDescription m-overflow" bis_skin_checked="1"><div class="truncatedUserDescription__wrapper" style="" bis_skin_checked="1">
#   <div class="truncatedUserDescription__content" bis_skin_checked="1">
#     <div bis_skin_checked="1"><p>Paris <br>Contact : <a href="mailto:lolamngmnt@gmail.com">lolamngmnt@gmail.com</a></p><p>25/09/22 @<a href="/radiokapital" class="g-link-user">radiokapital</a><br>21/12/22 @<a href="/ola_radio" class="g-link-user">ola_radio</a><br>12/04/23 @<a href="/radio28" class="g-link-user">radio28</a></p><p>💻 _shhshhshhshhshh</p></div>
#   </div>
# </div>
# <a class="truncatedUserDescription__collapse sc-link-dark sc-link-primary g-link-collapse" href="#">Show less</a>
# </div>
#   </div>

# <a href="mailto:lolamngmnt@gmail.com">lolamngmnt@gmail.com</a>