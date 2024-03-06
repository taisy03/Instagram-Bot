import pip
import random 
import maskpass
from PIL import Image, ImageTk

#os is used to create folders
import os 

# shutil will move the file from one folder to another
import shutil


# Type you instagram username and password here
username =""
password = ""

# This is to log in through the instagram API
from instagrapi import Client
client = Client()
def start():
    client.login(username,password)
    client.dump_settings("session.json")
