import json
import Modules.ColouredConsole as ColCon


###################################
###   Function to add to JSON   ###
###################################
def write_json(data, filename='Podcasts.json'):
    with open(filename,'w') as f:
        json.dump(data, f, indent=4)
      



###########################################
###   Function to add Details to JSON   ###
###########################################
def AddDetailsToJson(PodcastName, PodcastXml, PodcastDesc, PodcastWeb, PodcastUser, PodcastPassword):
    with open('Podcasts.json') as json_file:
        data = json.load(json_file)

        temp = data['Podcasts']
    
        # python object to be appended
        y = {
            "Name": PodcastName,
            "XML": PodcastXml,
            "Description": PodcastDesc,
            "Website": PodcastWeb,
            "User": PodcastUser,
            "Password": PodcastPassword
            }
    
    
        # appending data to emp_details 
        temp.append(y)

    write_json(data) 




#############################################
###   Function to Show Current Podcasts   ###
#############################################
def ShowCurrentPodcasts():
    f = open('Podcasts.json',)
   
    # returns JSON object as a dictionary
    data = json.load(f)
   
    print(ColCon.colours.bold + ColCon.colours.fg.red + "Podcast List: ")
    print(ColCon.colours.reset)

    # Iterating through the json list
    for i in data['Podcasts']:
        print(ColCon.colours.fg.cyan + i['Name'])
   
    # Closing file
    f.close()




#####################################
###   Running The Main Function   ###
#####################################
if __name__ == "__main__":

    print(ColCon.colours.fg.lightgreen + "Welcome to the Podcast Manager")
    print(ColCon.colours.fg.lightgreen + "Please choose one of the below options")
    print(ColCon.colours.fg.green + "1 - Show Current Podcast")
    print(ColCon.colours.fg.green + "2 - Add a new Podcast")
    optionpicked = input(ColCon.colours.fg.orange + "Choice: " + ColCon.colours.fg.pink)

    if optionpicked == "1":
        ShowCurrentPodcasts()

    elif optionpicked == "2":
        PodName = input(ColCon.colours.fg.orange + "Podcast Name: " + ColCon.colours.fg.pink)
        PodXml = input(ColCon.colours.fg.orange + "Podcast XML Link: " + ColCon.colours.fg.pink)
        PodDesc = input(ColCon.colours.fg.orange + "Podcast Description: " + ColCon.colours.fg.pink)
        PodWeb = input(ColCon.colours.fg.orange + "Podcast Website: " + ColCon.colours.fg.pink)
        PodUser = input(ColCon.colours.fg.orange + "Podcast Authencation Username (Blank if not required): " + ColCon.colours.fg.pink)
        PodPassword = input(ColCon.colours.fg.orange + "Podcast Authencation Password (Blank if not required): " + ColCon.colours.fg.pink)
        AddDetailsToJson(PodName,PodXml,PodDesc,PodWeb,PodUser,PodPassword)
        print(ColCon.colours.fg.blue + "Added " + PodName + " to podcast list.")
        print("")
        ShowCurrentPodcasts()

    else:
        print(ColCon.colours.bold + ColCon.colours.fg.red + "Invalid option. Valid options are 1 and 2")
