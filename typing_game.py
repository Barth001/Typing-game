from tkinter import *
import random

slideTexts = ""
count = 0
listOfWords = ["angle", "angry", "animal", "anniversary", "announce", "annual", "another", "answer", "anticipate",
               "anxiety", "any", "anybody", "beautiful", "beauty", "because", "become", "bed", "bedroom", "beer",
               "before", "begin", "beginning", "behavior", "behind", "being", "belief", "Canadian", "candidate", "cap",
               "capability", "capable", "capacity", "capital", "captain", "decide", "decision", "deck", "declare",
               "write", "wrong", "yard", "yeah", "year", "yell", "yellow", "yes"]


def welcomeTextSlideShow():
    global slideTexts, count
    string = "WELCOME!. IMPROVE YOUR TYPING SPEED"
    slideTexts += string[count]
    movingText.config(text=slideTexts)
    count += 1
    if count >= len(string):
        count = 0
        slideTexts = ""
    movingText.after(300, welcomeTextSlideShow)


root = Tk()
root.title("Typing Game -- created by Barth")
logoIcon = PhotoImage(file='icons/typing-game-icon.png')
root.tk.call('wm', 'iconphoto', root._w, logoIcon)
root.geometry("400x550+900+50")
root.resizable(False, False)
root.config(background="DarkSeaGreen4")
backgroundImg = PhotoImage(file='icons/clock.png')
backgroundLabel = Label(root, image=backgroundImg, background="DarkSeaGreen4")
backgroundLabel.place(x=70, y=100)
movingText = Label(root, text="WELCOME!. IMPROVE YOUR TYPING SPEED",
                   background="DarkSeaGreen4", font=("Courier", 10, "bold"), width=48)
movingText.place(x=0, y=10)
welcomeTextSlideShow()
random.shuffle(listOfWords)
typingWordLabel = Label(root, text=listOfWords[0], font=("Courier", 30, "bold"), background="DarkSeaGreen4")
typingWordLabel.place(x=200, y=390, anchor=CENTER)

textCountLabel = Label(root, text="0", font=("Courier", 15, "bold"), background="DarkSeaGreen4")
textCountLabel.place(x=327, y=130)

staticTextLabel = Label(root, text="Words", font=("Courier", 15, "bold"), background="DarkSeaGreen4")
staticTextLabel.place(x=300, y=100)

timeCountLabel = Label(root, text="0", font=("Courier", 15, "bold"), background="DarkSeaGreen4")
timeCountLabel.place(x=40, y=130)

timeLabel = Label(root, text="Timer", font=("Courier", 15, "bold"), background="DarkSeaGreen4")
timeLabel.place(x=20, y=100)
root.mainloop()
