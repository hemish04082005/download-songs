# imports
import requests #pip install requests
import sys
import time
import os
from requests import get
from bs4 import BeautifulSoup #pip install bs4

# ---------should be removed for android termux-start------------
from tkinter import Tk # Most standard python for windows installations include tkinter. You may have to install them on many linux distros and macs.
# ---------should be removed for android termux-end------------

#----------------------------------------------


# removed dependency of googlesearch-python by implementing its code here
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
# -------------googlesearch-python implementation end----------------



#Check whether internet connection is present or not
print("Checking Internet Connection...")
time.sleep(0.5)
url = "http://www.google.com"
timeout = 5
try:
    request = requests.get(url, timeout=timeout)
    print("Connected to the Internet")
    time.sleep(0.5)
except (requests.ConnectionError, requests.Timeout) as exception:
    print("No internet connection.")
    time.sleep(0.5)
    sys.exit()
#------------------------------------
temporaryboolean = None

print("Quality Levels:")
time.sleep(0.5)
print('''
1: Very High
2: High
3: Medium
4: Low 
5: Very Low
''')
print("Enter the quality level:")
qualitylevel = input()
if os.path.exists("songs.txt"):
    file = open("songs.txt", "rt")
    filelocation = "songs.txt"

# ---------should be removed for android termux-start------------
if not os.path.exists("songs.txt"):
    time.sleep(0.4)
    print("")
    print("songs.txt not found. Please select the text file manually which contains list of songs.")
    from tkinter.filedialog import askopenfilename
    Tk().withdraw()
    templocation = askopenfilename()
    filelocation = str(templocation)
    file = open((str(filelocation)), "rt")
# ---------should be removed for android termux-end------------

Counter = 0
Content = file.read() 
CoList = Content.split("\n")
for i in CoList: 
    if i: 
        Counter += 1
Counter += 1
iterationNo= 1
file.seek(0)
while iterationNo < Counter:
    try:
        inputquery = file.readline()
        inputquery = inputquery.rstrip()
        if inputquery == "":
            continue
        listoflinks = search(str(inputquery + " song" + " youtube"), num_results=7)
        linkofsong = listoflinks[0]
        print(inputquery)
        print(linkofsong)
        apisite = "https://y1.youtube-to-mp3.org/searchdl.php"
        payload = {"url": linkofsong,
        "type": "mp3"}
        postrequest = requests.post(apisite, data = payload)
        responsehtml = postrequest.text
        bs = BeautifulSoup(responsehtml, 'html.parser')
        table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="tab_mp3") 
        rows = table.findAll(lambda tag: tag.name=='tr')
        for y in [1,2,3,4,5]:
            if str(y) == str(qualitylevel):
                myrequirement = str(rows[y])
        hrefstring = myrequirement.find('href="')
        requiredhrefstartstring = str((int(hrefstring) + 6))
        requiredhrefstopstring = (int(myrequirement.find('" onclick="ads()"')))
        finallink = (myrequirement[int(requiredhrefstartstring):int(requiredhrefstopstring)])
        print("Downloading...")
        downloadrequest = requests.get(finallink, allow_redirects=True)
        open((inputquery+".mp3"), 'wb').write(downloadrequest.content)
        iterationNo += 1
    except:
        tempfile = open("templog.txt", "a")
        print("Failed")
        tempfile.write(inputquery+"\n")
        tempfile.close()
        iterationNo += 1
print("If any download has failed, the name is stored in templog.txt")
file.close()
print("Do you want to empty songs.txt so that next time you run the code, it does not pickup the previous songs? Type y for yes or n for no and then press enter.")
def takeinputYesOrNo():
    yesorno = input(">>")
    global temporaryboolean
    if yesorno != "y" and yesorno != "n" and yesorno != "Y" and yesorno != "N":
        print("Sorry write correct input")
        takeinputYesOrNo()
    if yesorno == "y" or yesorno == "Y":
        temporaryboolean = True
    if yesorno == "n" or yesorno == "N":
        temporaryboolean = False
takeinputYesOrNo()
if temporaryboolean == True:
    with open(filelocation, "wt") as filetobecleared:
        filetobecleared.write("")
