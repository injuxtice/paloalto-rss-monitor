import teamsconnector # comment out if you are not using Teams
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
    if str(listofFeeds[0]['title']).lower().find("xdr") != -1:
        if listofFeeds[0]['ID'] not in rssID:
            teamsconnector.sendMessage(f"NEW XDR ADVISORY   " + "\n   " + listofFeeds[0]['title'] + "\n   " + "Affected versions:   " + str(listofFeeds[0]['affected'])) # replace with action to take if xdr advisory is found, in this case a teams message is sent
            rssID.append(listofFeeds[0]['ID'])
            logging.info("Found XDR in title")
            logging.info(listofFeeds[0]['title'])
            logging.info(f"Affected versions {listofFeeds[0]['affected']}")
        else:
            logging.info("Already posted")
    #sleep for 2 hours
    logging.info("Sleeping for 2 hours")
    sleep(7200)