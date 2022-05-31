#YouTube Video downloader by @fcalve4 on GitHub
from tkinter import *
from pytube import YouTube
import os
import os.path

#Find path, check for downloaded folder, if doesn't exist, create.
dir_path = os.path.dirname(os.path.realpath(__file__))
path_download = dir_path + "/downloaded"
dir_exists = os.path.isdir(path_download)
if dir_exists == True:
    pass
else:
    os.makedirs("downloaded")
path = path_download

#Initialize window
root = Tk()
root.state = False # Set the value of the window to false by default, indicates whether in fullscreen or not
def get_scale_mult():
    if root.state == False:
        scale_mult = 1
    else:
        scale_mult = 2
    return scale_mult

#Get window size - 1/2 of screen resolution
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

def get_window_width():
    window_width = int(width * 0.5 * get_scale_mult())
    return window_width
def get_window_height():
    window_height = int(height * 0.5 * get_scale_mult())
    return window_height
def get_window_size():
    window_size = str(get_window_width()) + "x" + str(get_window_height())
    return window_size

#Set up window
def setup_window(): 
    root.resizable(0,0)
    root.geometry(get_window_size())
    root.configure(background="#2b2929")
    root.title("YouTube Video Downloader")

#Create place to insert link WITH LABEL
link = StringVar()
def place_pastelink_text(): 
    paste_link_label = Label(
        root,
        text = 'Paste Link Below',
        font = 'arial ' + str(int(round(30 * get_scale_mult()))) + ' bold underline',
        background = '#2b2929',
        foreground = '#bd433c'
        )
    paste_link_x = int((get_window_width() - (360 * get_scale_mult())) / 2)
    paste_link_y = int(get_window_height() * 0.25)
    paste_link_label.place(x=paste_link_x, y=paste_link_y)

#Insert link
def place_enterlink_text():
    link_enter = Entry(
        root, 
        width = int((70 * get_scale_mult())), 
        textvariable = link,
        background = "#ffffff"
        )
    link_enter_x = int((get_window_width() - (get_window_width() * 0.7)) / 2)
    link_enter_y = int(get_window_height() / 2)
    link_enter.place(x=link_enter_x, y=link_enter_y)

#Fullscreen function
def Fullscreen():
    if root.state == False: #If not in fullscreen, change to fullscreen, change indicator to True, increase scale, destroy and replace buttons/labels.
        root.attributes("-fullscreen", True)
        root.state = True
        for widget in root.winfo_children():
            widget.destroy()
        init_func()
        
    else:                   #If already in fullscreen, change back to normal size, change indicator to False, decrease scale, destroy and replace buttons/labels.
        root.attributes("-fullscreen", False)
        root.state = False
        for widget in root.winfo_children():
            widget.destroy()
        init_func()

#Main download function
def Download():     
    try: #Valid Link
        url = YouTube(str(link.get()))
        video = url.streams.get_highest_resolution()
        video.download(output_path=path)
        downloaded_label = Label(
            root,
            text = 'DOWNLOADED', 
            font = 'arial ' + str(int(round(15 * get_scale_mult()))),
            background = '#2b2929',
            foreground = '#bd433c'
            )
        downloaded_label_x = int((get_window_width() - (get_window_width() * 0.2)) / 2)
        downloaded_label_y = int(get_window_height() * 0.9)
        downloaded_label.place(x=downloaded_label_x, y=downloaded_label_y)
    except: #Invalid Link
        fail_label = Label(
            root,
            text = '<<INVALID>>',
            font = 'arial ' + str(int(round(15 * get_scale_mult()))),
            background = '#2b2929',
            foreground = '#bd433c'
        )
        fail_label_x = int((get_window_width() - (get_window_width() * 0.2)) / 2)
        fail_label_y = int(get_window_height() * 0.9)
        fail_label.place(x=fail_label_x, y=fail_label_y)

#Create Download Button    
def place_download_button():
    download_button = Button(
        root,
        height = 2,
        width = 20,
        text = 'DOWNLOAD',
        font = 'arial ' + str(int(round(15 * get_scale_mult()))) + ' bold' ,
        bg = '#bd433c', 
        padx = 2, 
        command = Download
        )
    dbutton_x = int((get_window_width() - (get_window_width() * 0.4)) / 2)
    dbutton_y = int(get_window_height() * 0.7)
    download_button.place(x=dbutton_x, y=dbutton_y)

#Create fullscreen button
def place_fullscreen_button():
    fullscreen_button = Button(
        root,
        height = 1,
        width = 15,
        text = 'Toggle Fullscreen',
        font = 'arial 10 bold',
        bg = '#bd433c',
        padx = 2,
        command = Fullscreen
        )
    fbutton_x = 0
    fbutton_y = 0
    fullscreen_button.place(x=fbutton_x, y=fbutton_y)

#Initial function to get values & place buttons
def init_func():
    get_scale_mult()
    get_window_width()
    get_window_height()
    get_window_size()
    setup_window()
    place_pastelink_text()
    place_enterlink_text()
    place_download_button()
    place_fullscreen_button()

#Run program
if __name__ == "__main__":
    init_func()
    root.mainloop()
