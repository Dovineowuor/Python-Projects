# import all Tkinter libraries from the module
from tkinter import Entry, StringVar
from tkinter import * 
# From the  installed Pytube module, import the youtube library
from Pytube import YouTube 
root = Tk()
root.geometry('500 X 300') # Size of the window
root.resizable(0, 0) # makes the window adjustable with its features
root.title('Video downloader')

root.mainloop()
# Initialize link entry
Label(root, text="Video Downloader", font='san-serif 14 bold').pack()
link = StringVar() # Specifying the variable type
Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)
# Download button
Button(root, text='Download', font='san-serif 16 bold', bg='sky-blue', padx=2,command="download").place(x=100, y=150)

# Enabling download function
def download():
    url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
    video = url.streams.first() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
    video.download() # This is the method with the instruction to download the video.
    Label(root, text="Downloaded", font="arial 15").place(x=100, y=120) #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.

    