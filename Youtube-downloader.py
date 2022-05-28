# import all Tkinter libraries from the module
from tkinter import Entry, StringVar
from tkinter import * 
# From the  installed Pytube module, import the youtube library
from pytube import YouTube 
root = Tk()
root.geometry('500 X 300') # Size of the window
root.resizable(0, 0) # makes the window adjustable with its features
root.title('youtube downloader')

root.mainloop()
# Initialize link entry
Label(root, text="Download Youtube videos for free", font='san-serif 14 bold').pack()
link = StringVar() # Specifying the variable type
Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=85)

