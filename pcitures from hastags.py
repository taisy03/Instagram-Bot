from start import *
start()

import tkinter as tk
window = tk.Tk()

##paths
### Fill this in with your own path 
path = "/Users/yourname/Desktop/instagram bot/pictures/"

## hastags
hashtag_used = "y2knails"




medias = client.hashtag_medias_top(hashtag_used, 10)
#media type 1 = photo
#media type 8 = album

class Hashtag:
    name = f"{hashtag_used}"
    path = ""

hashtag = Hashtag()


def create_folder(name):
    folder_name = name
    folder_location = path
    folder_p = os.path.join(folder_location, folder_name)
    os.mkdir(folder_p)
    hashtag.path = folder_p
    print(f"{folder_name} folder created.")
    print(f"Folder path: {hashtag.path}")


create_folder(hashtag_used)


## download photos

for i, media in enumerate(medias):
    if media.media_type == 1:
        client.photo_download(
        media.pk, 
        folder = hashtag.path
        )
        print("photo" + i + "Downloaded")
    elif media.media_type == 8:
        client.album_download(
        media.pk, 
        folder = hashtag.path
        )
        print("Album" + i + "Downloaded")
    else :
        continue





##### folder for ready to upload
#Make sure to change the paths
class folder_upload:
        name = "folder_upload"
        path = "/Users/yourname/Desktop/instagram_bot/pictures/folder_upload"

folder_upload = folder_upload()


###### move photos to folder_upload that I want
def create_window(path):
     im = Image.open(path)
     width , height = im.size
     window.geometry(f"{width}x{height}")
     test = ImageTk.PhotoImage(im)
     label1 = tk.Label(image=test)
     label1.image = test
     label1.place(x=0, y=0)
     
     def answer_yes():
        print("User chose : yes")
        shutil.move(path ,folder_upload.path)
        window.quit()
        

     def answer_no():
        print("User chose : no")
        answer = "no"
        window.quit()

     buttonframe = tk.Frame(window)
     buttonframe.columnconfigure(0 , weight=1)
     buttonframe.columnconfigure(1 , weight=1)

     button = tk.Button(buttonframe , text= "No" , font= ('Arial' , 18), command = answer_no)
     button.grid(row = 0 , column=0 , sticky= tk.W + tk.E)

     button2 = tk.Button(buttonframe , text= "Yes" , font= ('Arial' , 18), command = answer_yes)
     button2.grid(row = 0 , column=1 , sticky= tk.W + tk.E)
     buttonframe.pack(fill = 'x')

     window.mainloop()
     


#create fucntion for window to display images

new_path = f"{path}{hashtag_used}"

image_list = os.listdir(f"{new_path}")
           
for i in image_list:
        if i.endswith(".jpg"):
            tempTuple = f"{new_path}" + "/" + i
            create_window(tempTuple)
        else:
            tempTuple = f"{new_path}" + "/" + i
            os.remove(tempTuple)
           
