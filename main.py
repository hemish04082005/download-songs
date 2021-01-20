import webbrowser
import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4
from requests import get
def search(term, num_results=10, lang="en"):
    usr_agent = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/61.0.3163.100 Safari/537.36'}

    def fetch_results(search_term, number_results, language_code):
        escaped_search_term = search_term.replace(' ', '+')

        google_url = 'https://www.google.com/search?q={}&num={}&hl={}'.format(escaped_search_term, number_results+1,
                                                                              language_code)
        response = get(google_url, headers=usr_agent)
        response.raise_for_status()

        return response.text

    def parse_results(raw_html):
        soup = BeautifulSoup(raw_html, 'html.parser')
        result_block = soup.find_all('div', attrs={'class': 'g'})
        for result in result_block:
            link = result.find('a', href=True)
            title = result.find('h3')
            if link and title:
                yield link['href']

    html = fetch_results(term, num_results, lang)
    return list(parse_results(html))
print("")
print("Enter the name of song: ")
inputquery = input()
listoflinks = search(str(inputquery + " youtube"), num_results = 7)
linkofsong = listoflinks[0] #I needed only first indice but queried 7 results in above line
print("")
print(linkofsong)
apisite = "https://y1.youtube-to-mp3.org/searchdl.php"
payload = {"url": linkofsong,
"type": "mp3"}
postrequest = requests.post(apisite, data = payload)
responsehtml = postrequest.text
bs = BeautifulSoup(responsehtml, 'html.parser')
table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="tab_mp3") 
rows = table.findAll(lambda tag: tag.name=='tr')
print('''
Quality Levels
1: Very High
2: High
3: Medium
4: Low 
5: Very Low
''')
print("Enter the quality level:")
qualitylevel = input()
for y in [1,2,3,4,5]:
	if str(y) == str(qualitylevel):
		myrequirment = rows[y]
print("")
myrequirement = str(myrequirment) #This part is the funniest one!
hrefstring = myrequirement.find('href="') #First used beautiful soup to parse the table but then using simple string find methods! I should do it in bs4 itself!
requiredhrefstartstring = str((int(hrefstring) + 6))
requiredhrefstopstring = (int(myrequirement.find('" onclick="ads()"'))) #yes that apisite has ads which popup when you click the download button!
finallink = (myrequirement[int(requiredhrefstartstring):int(requiredhrefstopstring)])
print('''To download with python, press Enter (Default mode)
To download with your default browser, press b and enter.
If you enter any random character then, it would switch to default mode.''')
browserorpython = input(">")
if browserorpython != "b":
	print("Downloading...")
	downloadrequest = requests.get(finallink, allow_redirects=True)
	open((inputquery+".mp3"), 'wb').write(downloadrequest.content)
if browserorpython == "b" or browserorpython == "B":
	webbrowser.open(finallink)
