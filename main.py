from bs4 import BeautifulSoup
import requests

URL = "https://wuzzuf.net/search/jobs/?q=tech&a=hpb"  # WUZZUF JAVA JOBS PAGE RESULT
techno = input(str("Input a technologie "))

URL = URL.replace("tech", techno)

src = requests.get(URL).text


soup = BeautifulSoup(src, "lxml")

jobs_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_name = soup.find_all("a", {"class": "css-17s97q8"})
locations_name = soup.find_all("span", {"class": "css-5wys0k"})
jobs_skils = soup.find_all("div", {"class": "css-1lh32fc"})

jobs_size = len(jobs_titles)

for i in range(jobs_size):
    jobs_titles[i] = jobs_titles[i].text
    company_name[i] = company_name[i].text
    locations_name[i] = locations_name[i].text
    jobs_skils[i] = jobs_skils[i].text

print(jobs_titles)
