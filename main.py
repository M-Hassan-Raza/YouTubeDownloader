from tkinter import *
import tkinter
from tkinter import messagebox
from pytube import YouTube


window_height = 300
window_width = 500


canvas = Tk()
canvas.geometry("500x300")
canvas.title("YouTube Downloader")
canvas.iconbitmap('images/icon.ico')
canvas.configure(bg='white')
canvas.resizable(False, False)
screen_width = canvas.winfo_screenwidth()
screen_height = canvas.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
canvas.geometry("{}x{}+{}+{}".format(window_width,
                                     window_height, x_coordinate, y_coordinate))


link = StringVar()

Label(canvas, text = 'Paste Link Here:', font = 'SAN_SERIF 15 bold').place(x= 160 , y = 50)
link_enter = Entry(canvas, width = 55,textvariable = link, justify=CENTER).place(x = 32, y = 95)


def video_downlaoder():
    if not link.get():
        return
        
    url = YouTube(str(link.get()))
    video = url.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    video.download()
    messagebox.showinfo(
        "Information", "Download Successful! Output placed in the Source folder")


browse_button = tkinter.Button(canvas, text="Download",
                          command=video_downlaoder, font=("SAN_SERIF", 15, "bold"), relief=FLAT, activebackground="black", activeforeground="white").place(x = 170, y = 200)


canvas.mainloop()