#q1 Using BeautifulSoup (docs), print, then save as ELECTION_ID, a list containing the years and election IDs in exactly this format.
#first import webpage and parse it
import requests
page = requests.get("http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General")
from bs4 import BeautifulSoup as bs
soup=bs(page.content,'html.parser')
# to make lists of id and year
tag=soup.find_all('tr','election_item')
electionid = [x.get("id").split("-")[2] for x in tag]
yearid=soup.find_all('td', attrs={'class':'year first'})
year = [pt.get_text() for pt in yearid]
# to make list with ids and years
id_plus_year=[]
for i in range (0,23):
    new=year[i], electionid[i]
    id_plus_year.append(new)

with open ('ELECTION_ID', 'w') as file:
    for i in id_plus_year:
        file.write("{}\n".format(i[0]+' '+i[1]+ ' '))
        print(i[0],i[1])
