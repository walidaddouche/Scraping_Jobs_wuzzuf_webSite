from bs4 import BeautifulSoup
import requests

URL = "https://wuzzuf.net/search/jobs/?q=java&a=hpb"  # INDEED JAVA INTERNSHIP PAGE RESULT
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/50.0.2661.102 Safari/537.36'}

f = open("index.html", "r")
src = f.read()
soup = BeautifulSoup(src, "lxml")

jobs = soup.find_all("a", {"class": "css-1gatmva"})

# div id="jobsearch-JapanPage" inside another div who has not a name inside
# div class="jobsearch-JapanPageLayout jobsearch-JapanSerpContainer is-i18n"
# inside div class="jobsearch-SerpMainContent "
# inside div class="jobsearch-LeftPane"
# inside div id="mosaic-jobcards" && class="mosaic-zone"
# than UL

# the presentation of our Jobs proposition are enrolled in an ul (list) and each Job is a li of this list
# the ul is identified by this name class, class="jobsearch-ResultsList css-0"
jobs_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_name = soup.find_all("a", {"class": "css-17s97q8"})
locations_name = soup.find_all("span", {"class": "css-5wys0k"})
jobs_skils = soup.find_all("div", {"class": "css-1lh32fc"})

for i in range(len(jobs_titles)):
    jobs_titles[i] = jobs_titles[i].text
    company_name[i] = company_name[i].text
    locations_name[i] = locations_name[i].text
    jobs_skils[i] = jobs_skils[i].text
