import tkinter as tk
from tkinter import messagebox
window = tk.Tk()


def message():
    check1 = ""
    check2 = ""
    check3 = ""
    if checkrocks.get() == 1:
        check1 = "Rock"
    if checkpops.get() == 1:
        check2 = "Pop"
    if checkjazzes.get() == 1:
        check3 = "Jazz"
    messagebox.showinfo("Music Preferences", f"Favorite Artist/Band: {entry.get()}\nFavorite genre: {
                        check1} {check2} {check3}\nPrefered Listening Method: {meth.get()}")


window.geometry("600x900")
window.title("My Music Preferences")
label1 = tk.Label(window, font=("Comic Sans MS", 20),
                  fg="purple", text="Welcome to My Music Preferences!")
label1.pack()
label2 = tk.Label(window, font=("Comic Sans MS", 15),
                  text="Who is your Favorite artist or band?")
label2.pack()
entry = tk.Entry(window, font=("Comic Sans MS", 15), width=20)
entry.pack()
label3 = tk.Label(window, font=("Comic Sans MS", 15),
                  text="Select your favorite music genres:")
label3.pack()
checkrocks = tk.IntVar()
checkrock = tk.Checkbutton(window, text="Rock", font=(
    "Comic Sans MS", 10), variable=checkrocks)
checkrock.pack(anchor="w")
checkpops = tk.IntVar()
checkpop = tk.Checkbutton(window, text="Pop", font=(
    "Comic Sans MS", 10), variable=checkpops)
checkpop.pack(anchor="w")
checkjazzes = tk.IntVar()
checkjazz = tk.Checkbutton(window, text="Jazz", font=(
    "Comic Sans MS", 10), variable=checkjazzes)
checkjazz.pack(anchor="w")
label4 = tk.Label(window, font=("Comic Sans MS", 15),
                  text="Choose your prefered listening method:")
label4.pack()
meth = tk.StringVar()
tk.Radiobutton(window, text="Streaming", font=("Comic Sans MS", 10),
               variable=meth, value="Streaming").pack(anchor="w")
tk.Radiobutton(window, text="CDs", font=("Comic Sans MS", 10),
               variable=meth, value="CDs").pack(anchor="w")
tk.Radiobutton(window, text="Vinyl", font=("Comic Sans MS", 10),
               variable=meth, value="Vinyl").pack(anchor="w")
button = tk.Button(window, text="Submit", font=(
    "Comic Sans MS", 20), command=message)
button.pack()
window.mainloop()
