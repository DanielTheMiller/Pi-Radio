#getNextTrack(int nextProgramTime)
    #check the override schedule hasn't booked something instead

    #if it is the hour, put on the news clip
    
    #check the schedule.




#checkForUpdates()

#Run this repeatedly in the background forever.
# have a config cvs with xmls for all the podcasts.
# configfile Format: (Podname, RssXmlUrl, lastUpdated)
import csv
import sys
import os.path
import requests
from bs4 import BeautifulSoup

OUTPUT_DIR = "./podfiles/"

def readRSS(podAlias,podRSSurl):
    print("Reading",podAlias,"at",podRSSurl)
    page = requests.get(podRSSurl)
    parser = BeautifulSoup(page.content, "xml")
    episodes = parser.findAll("item") #This is correct format
    for podcast in episodes: #Enclosure is where a download is placed.
        if podcast.enclosure['type'] != u'audio/mpeg': #Skips videos.
            continue
        podUrl = podcast.enclosure['url']
        fetchFile(podAlias,podUrl)
        break    

def fetchFile(podAlias, podUrl):
    filepath = OUTPUT_DIR + podAlias + "downloading.mp3"
    if os.path.exists(filepath): #File can't already exist
        return False
    print ("fetching",podAlias,"from",podUrl,"...")
    try:
        r = requests.get(podUrl, allow_redirects=True)
        open(filepath, 'wb').write(r.content)  
    except IOError as ex:
        print("IO error saving ",url, ":",ex)
        os.remove(filepath)
        return False
    except Exception as ex:
        print("Exception saving ",url,":",ex)
        os.remove(filepath)
        return False
    print("Done!")
    return True
            
with open('podFeeds.csv',mode='r',encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            #This is the header line
            #id, url, lastupdate, inUse (Reading or writing)
            print(f'Column names are {", ".join(row)}')
        else:
            #Read the body
            podAlias = row['alias']
            podRSSurl = row['url']
            readRSS(podAlias, podRSSurl)
        line_count += 1
    #csv_reader.close()
print("Done...")
