#import teamsconnector # comment out if you are not using Teams
import json
import urllib.request
from time import sleep
import logging
#this script will get the RSS feed and post it to a Teams channel if the subject mentions XDR

root = logging.getLogger()
root.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
root.addHandler(handler)

def getRSSFeed():
    try:
        newsfeed = urllib.request.urlopen("https://security.paloaltonetworks.com/json/")
        outputJson = json.loads(newsfeed.read())
        return outputJson
    except Exception as e:
        logging.error(e)
listofFeeds = getRSSFeed()
#get latest feed
rssID = []
while True:
    if "XDR" in listofFeeds[0]['product']:
        if listofFeeds[0]['ID'] not in rssID:
            print(f"Vulnerability name: {listofFeeds[0]['title']}\nAffected version: {', '.join(filter(None, listofFeeds[0]['affected']))}\nFixed version: {', '.join(filter(None, listofFeeds[0]['fixed']))}")
            rssID.append(listofFeeds[0]['ID'])
            logging.info(f"Found {listofFeeds[0]['title']}")
        else:
            logging.info("Already posted")

    #sleep for 2 hours
    logging.info("Sleeping for 2 hours")
    sleep(7200)