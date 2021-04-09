# Podcast-Backup

## Description
A Python based script to Download/Backup Podcasts


## Usage
###### Setting up
1) Make sure you have python3 installed
2) Install requests (pip install requests  /  pip3 install requests)

###### Creating the JSON file of Podcasts
1) Run the script "PodcastListManager.py" (python3 PodcastListManager.py)
2) Follow the instruction prompted in the script
2a) Press 1 to view current Podcast list
2b) Press 2 to add a new podcast
2c) Give the details requested. Make sure you are giving the xml link not just a link to the Podcast site.
3) If you need to remove a Podcast please open the JSON file and remove it. I will add the functionality to remove Podcasts in future updates.
4) If you need to change a Podcast please open the JSON file and ammend. I will add the functionality to edit Podcasts in future updates.

###### Downloading the Podcasts
1) Make sure you have got your list of Podcasts
2) Run the script "Podcast Download.py"  (python3 Podcast Download.py)
3) It will create the folders it needs and download the XMLs, Podcasts and create a CSV for each Podcast with the details in it.


## Plans
1) Add extra functionalities into the Podcast Manager to delete and edit entries
2) Get extra infomation from the podcasts such as cover art, comments, etc
3) Create a GUI / WebUI for easier management and Organisation


## Thanks / Credit

XML and CSV parsing / Writing

https://www.geeksforgeeks.org/working-csv-files-python/

https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/

https://www.geeksforgeeks.org/xml-parsing-python/


Downloading MP3 Files

https://stackoverflow.com/a/65529455


Colouring Terminal

https://stackoverflow.com/a/26445590