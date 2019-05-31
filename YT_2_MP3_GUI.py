import tkinter as tk
import subprocess

def yt_dl_mp3():
    subprocess.call(["youtube-dl", 
                    "--extract-audio",
                    "--audio-format",
                    "mp3",
                    e1.get()])
def yt_dl_mp4():
    subprocess.call(["youtube-dl", 
                    e1.get()])

master = tk.Tk()
tk.Label(master, text="Link:").grid(row=0, column=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

b1 = tk.Button(master, 
        text='Quit', 
        highlightbackground='#3E4149',
        command=master.quit)

b1.grid(row=1,
        column=0,
        sticky=tk.W,
        pady=4)

b2 = tk.Button(master, 
        text='Download MP3', 
        highlightbackground='#3E4149',
        command=yt_dl_mp3)

b2.grid(row=1,
        column=1,
        sticky=tk.W,
        pady=4)

b3 = tk.Button(master, 
        text='Download MP4', 
        highlightbackground='#3E4149',
        command=yt_dl_mp4)

b3.grid(row=1,
        column=2,
        sticky=tk.W,
        pady=4)

tk.mainloop()
