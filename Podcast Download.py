import csv
import requests
import xml.etree.ElementTree as ET
import sys
import json
import os
import re
import time





##########################################################
###   Defining function to remove special charactors   ###
##########################################################
def RemoveSpecialChar(inStr):
    FixedStr = inStr.replace('(ad free)','')
    FixedStr = FixedStr.replace('(ad-free)','')
    FixedStr = FixedStr.replace('&#8217;','')
    FixedStr = FixedStr.replace('/','-')
    #FixedStr = FixedStr.replace('.','-')
    FixedStr = FixedStr.replace(':','-')
    FixedStr = FixedStr.replace(' & ',' and ')
    FixedStr = FixedStr.replace('&',' and ')
    FixedStr = FixedStr.replace('  ',' ')
    FixedStr = re.sub('[^A-Za-z0-9- .]+', '', FixedStr)

    return FixedStr




#########################################
###   Defining Podcast XML Download   ###
#########################################
def DownloadPodcastXML(PodcastName,PodcastURL,PodcastUser,PodcastPass):

    #Sending request for XML
    resp = requests.get(PodcastURL, auth=(PodcastUser, PodcastPass))

    #Check if ./XMLs/ exists and if not creates
    if not os.path.exists('./XMLs'):
        os.makedirs('./XMLs')

    # saving the xml file
    PodcastXmlFile = './XMLs/' + PodcastName + '.xml'
    with open(PodcastXmlFile, 'wb') as f:
        f.write(resp.content)

    return PodcastXmlFile




################################
###   Defining XML Parsing   ###
################################
def parseXML(PodcastName, xmlfile):
  
    # create element tree object
    tree = ET.parse(xmlfile)
  
    # get root element
    root = tree.getroot()

    # Creating Array
    arrPodcasts = []
  
    # iterate news items
    for item in root.findall('./channel/item'):

        arrPod = {}

        PodTitle = item.find('./title').text
        PodTitle = RemoveSpecialChar(PodTitle)
        PodMp3Link = item.find('./enclosure').get('url')

        arrPod['Title'] = item.find('./title').text
        arrPod['Link'] = item.find('./link').text
        arrPod['PubDate'] = item.find('./pubDate').text
        arrPod['Description'] = item.find('./description').text
        arrPod['AudioLink'] = item.find('./enclosure').get('url')
        #arrPod['Author'] = item.find('./{http://www.itunes.com/dtds/podcast-1.0.dtd}author').text
        #arrPod['ItunesImage'] = item.find('./{http://www.itunes.com/dtds/podcast-1.0.dtd}image').get('href')
        #arrPod['Duration'] = item.find('./{http://www.itunes.com/dtds/podcast-1.0.dtd}duration').text

        #Downloading MP3
        Mp3Download(PodcastName,PodTitle,PodMp3Link)


        #Adding to array
        arrPodcasts.append(arrPod)

    #Returning the array
    return arrPodcasts




#######################################
###   Defining the MP3 Downloader   ###
#######################################
def Mp3Download(PodcastName, Mp3Tile, Mp3Link):

    #Setting Name Variables
    PodcastDir = './Podcasts/' + PodcastName
    PodcastFile = './Podcasts/' + PodcastName + '/' + Mp3Tile + '.mp3'

    #Check if file Exists
    if not os.path.exists(PodcastFile):

        print("Downloading - " + Mp3Tile)
        time.sleep(5)

        #Trying to get the MP3 file
        try:
            u = requests.get(Mp3Link)
        except Exception as e:
            print(e)
            sys.exit()


        #Check if Directories exist
        if not os.path.exists('./Podcasts'):
            os.makedirs('./Podcasts')

        if not os.path.exists(PodcastDir):
            os.makedirs(PodcastDir)


        #Writing to file
        with open(PodcastFile, 'wb') as f:
            for chunk in u.iter_content(chunk_size=1024): 
                if chunk: # filter out keep-alive new chunks
                    f.write(chunk)
        return None

    else:
        print("Exists - " + Mp3Tile)





#############################################
###   Defining the Save to CSV function   ###
#############################################
def savetoCSV(arrPodcasts, PodcastName):
  
    #Setting File Details
    CsvFilePath = './CSVs/' + PodcastName + '.csv'

    #Check if Directories exist
    if not os.path.exists('./CSVs'):
        os.makedirs('./CSVs')

    # specifying the fields for csv file
    fields = ['Title', 'Link', 'PubDate', 'Description', 'AudioLink']# 'Author', 'ItunesImage', 'Duration'
  
    # writing to csv file
    with open(CsvFilePath, 'w') as csvfile:
  
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames = fields)
  
        # writing headers (field names)
        writer.writeheader()
  
        # writing data rows
        writer.writerows(arrPodcasts)





######################################
###   Defining The Main Function   ###
######################################
def main():
    # Opening the JSON Podcast List
    f = open('Podcasts.json',)
   
    # returns JSON object as a dictionary
    data = json.load(f)

    # Iterating through the json list
    for i in data['Podcasts']:
        
        #Downloading the XML
        XmlPath = DownloadPodcastXML(i['Name'],i['XML'],i['User'],i['Password'])

        #Parsing the XML, Downloading MP3s and Returning Array
        arrPods = parseXML(i['Name'], XmlPath)

        #Saving the Podcast Details to CSV File
        savetoCSV(arrPods, i['Name'])




#####################################
###   Running The Main Function   ###
#####################################
if __name__ == "__main__":
  
    #Running Main
    main()