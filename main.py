import tkinter as tk 
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry('600x450')
canvas['bg']='black'

rootpath = "C:\\Users\LENOVO\Music"
pattern = "*.mp3"

mixer.init()

pre_Button_img = tk.PhotoImage(file="./img/icon/rev.png")
next_Button_img = tk.PhotoImage(file="./img/icon/forward.png")
play_pause_Button_img = tk.PhotoImage(file="./img/icon/play_pause.png")
pause_Button_img = tk.PhotoImage(file="./img/icon/pause_img.png")
stop_Button_img = tk.PhotoImage(file="./img/icon/stop.png")

def select():
    lable.config(text= listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear("active")

def pause():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else:
        mixer.music.unpause()
        pauseButton["text"]= "Pause"

def next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    lable.config(text= next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(next_song)
    listBox.select_set(next_song)


def Previus():
    pre_song = listBox.curselection()
    pre_song = pre_song[0] - 1
    pre_song_name = listBox.get(pre_song)
    lable.config(text= pre_song_name)
    mixer.music.load(rootpath + "\\" + pre_song_name)
    mixer.music.play()

    listBox.select_clear(0, "end")
    listBox.activate(pre_song)
    listBox.select_set(pre_song)



listBox = tk.Listbox(canvas, fg="white", bg="black", width=100, font=("poppins", 12))
listBox.pack(padx = 15 , pady=15)

lable = tk.Label(canvas, text="", bg="black", fg="white", font=("oppins", 12))
lable.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10 , pady=5 , anchor= "center")

prevButton = tk.Button(canvas, text="Prev", image= pre_Button_img, bg="black", borderwidth=0, command= Previus)
prevButton.pack(padx = 15 , pady=15, in_=top, side="left")

nextButton = tk.Button(canvas, text="Next", image= next_Button_img, bg="black", borderwidth=0, command= next)
nextButton.pack(padx = 15 , pady=15, in_=top, side="left")

playPauseButton = tk.Button(canvas,text ="Play/pause", image= play_pause_Button_img, bg="black", borderwidth=0, command= select)
playPauseButton.pack(padx = 15 , pady=15, in_=top, side="left" )

pauseButton = tk.Button(canvas, text="Pause", image= pause_Button_img, bg="black", borderwidth=0, command= pause)
pauseButton.pack(padx = 15 , pady=15, in_=top, side="left")

stopButton = tk.Button(canvas, text="Stop", image= stop_Button_img, bg="black", borderwidth=0, command= stop)
stopButton.pack(padx = 15 , pady=15, in_=top, side="left")

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)
canvas.mainloop()