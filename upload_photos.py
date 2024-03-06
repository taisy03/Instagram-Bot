
from start import *
username = "r.e.aper"
start()

#### HASHTAGS
hashtags = "#fashion #fashionstyle #y2k #trendyoutfits #pintrest #styleinspo #y2koutfits #trendyclothes #ootd #ootdfashion #90s "

###Caption
caption = input("Caption for post: ")

##path to picutres folder
path = "/Users/yourname/Desktop/instagram bot/pictures/"

## Save PICTURES TO FOLDER
## These are just some accounts that i used for my inspo page
account = "pintfairt"
other_account = ["pintfairy" ,"purplerang" "styleinsqo","aestootd","glossifier","inspofolio"]
account_id = client.user_id_from_username(account)
medias = client.user_medias(account_id, 3)
#list of folder names for pictures
folder_names = []

for i, media in enumerate(medias):
        if media.media_type == 8:
                folder_name = f"{account} Folder {i+1}"
                folder_names.append(folder_name)
                folder_location = path
                folder_path = os.path.join(folder_location, folder_name)
                os.mkdir(folder_path)
                print(f"{folder_name} created.")
                
                client.album_download(
                        media_pk = media.pk, 
                        folder = f"{path}{folder_name}")
        else:
                continue


image_list = os.listdir(f"{path}{folder_names[0]}")


combined_path = []
for i in image_list:
        tempTuple2 = f"{path}{folder_names[0]}" + "/" + i 
        print(tempTuple2)
        combined_path.append(tempTuple2)

## UPLOAD ALBUM
from instagrapi.types import Usertag
user = client.user_info_by_username(username)
media = client.album_upload(
        paths = combined_path,
        #make the path the path of the photo collected from online 
        caption = f"""{caption}
        .
        .
        .
        .
        .
        {hashtags}""" ,
        )

