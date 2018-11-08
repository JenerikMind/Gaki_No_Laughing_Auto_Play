# Author: JenerikMind
# To open in separate, interactable window
from selenium import webdriver as web
# For the sleep command
from time import sleep

# The file which contains the batsu library
from Gaki_Playlist import *

# to lazy to research if already exists
def to_min(int):
    minutes = int * 60
    return minutes

def play(batsu_game_array, episode=0):

    # The raw string is where you should have your chromedriver located.
    # Ideally would be in your PATH, but who has the time to wikiHow that?
    chrome = web.Chrome(r"C:\Users\jm\Desktop\chromedriver.exe")

    # Just a check to make sure playlist starts at first ep
    # or to adj for the 0 count that arrays use
    if episode > 0:
        episode -= 1
    else:
        episode = 0

    # For each dictionary in the array
    for dict in batsu_game_array[episode:]:
        for key, value in dict.items():
            chrome.get(key) # pass the link to chrome
            print("{} minutes until the next video plays".format(value))
            sleep(to_min(value)) # sleep the program until ep finished




### Start the UI(ish) Section ###

def create_titles_list():
    playlist = open("Gaki_Playlist.py")
    titles = []
    playlist_text = playlist.readlines()

    for line in playlist_text:
        if " = " in line:
            titles.append(line)

    titles.pop(0) # to remove the demo line in the comments
    i = 0         # int used to overwrite array line
    
    for line in titles: # in each line from the playlist
        end_index = line.index(" =") # look for " ="
        titles[i] = line[0:end_index]# slice the line using the end_index
        i += 1          #increment i

    return titles


def start():
    titles = create_titles_list()
    print("Available playlists : {} ".format(titles))
    choice = input("Which would you like to see:  ").lower()

    if choice == "yugawara":
        play(yugawara)
    elif choice == "hotel":
        play(hotel)
    elif choice == "edf":
        play(edf)
    elif choice == "science":
        play(science)
    elif choice == "apo":
        play(apo)
    else:
        print("""Either a wrong entry, or list doesn't exist. Either way,
 these aren't the droids you're looking for.""")

start()
