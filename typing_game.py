from tkinter import *
from tkinter import messagebox
import random

slideTexts = ""
count = 0
correctWord = 0
incorrectWord = 0
k = 0
remainingTime = 60


def timing():
    global remainingTime, k, correctWord, incorrectWord
    if remainingTime > 0:
        remainingTime -= 1
        timeCountLabel.config(text=remainingTime)
        timeCountLabel.after(1000, timing)
    else:
        userInput.config(state=DISABLED)
        result = correctWord - incorrectWord
        inputTextLabel.config(text=f'Correct word {correctWord}, Incorrect word {incorrectWord}\n'
                                   f'Final score {result}')
        if result > 15:
            emojiLabel1.config(image=sadImg)
            emojiLabel2.config(image=sadImg)
        elif result == 15:
            emojiLabel1.config(image=happyImg)
            emojiLabel2.config(image=happyImg)
        else:
            emojiLabel1.config(image=profImg)
            emojiLabel2.config(image=profImg)

        deci = messagebox.askokcancel("Confirm", "Do you wish to play again")
        if deci:
            k, correctWord, incorrectWord, remainingTime = 0, 0, 0, 60
            textCountLabel.config(text="0")
            timeCountLabel.config(text="60")
            userInput.config(state=NORMAL)
            inputTextLabel.config(text="Type the displayed word and hit enter")
            emojiLabel1.config(image="")
            emojiLabel2.config(image="")


def play(event):
    if userInput.get() != "":
        global k, correctWord, incorrectWord
        k += 1
        textCountLabel.config(text=k)
        inputTextLabel.config(text="")
        if remainingTime == 60:
            timing()

        if userInput.get() == typingWordLabel["text"]:
            correctWord += 1

        else:
            incorrectWord += 1

        random.shuffle(listOfWords)
        typingWordLabel.config(text=listOfWords[0])
        userInput.delete(0, END)


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

timeCountLabel = Label(root, text="60", font=("Courier", 15, "bold"), background="DarkSeaGreen4")
timeCountLabel.place(x=40, y=130)

timeLabel = Label(root, text="Timer", font=("Courier", 15, "bold"), background="DarkSeaGreen4")
timeLabel.place(x=20, y=100)

userInput = Entry(root, font=("Courier", 20, "bold"), bd=3, justify=CENTER)
userInput.place(x=200, y=450, anchor=CENTER)
userInput.focus_set()

inputTextLabel = Label(root, text="Type the displayed word and hit enter",
                       font=("Courier", 10, "bold"), background="DarkSeaGreen4", fg="red")
inputTextLabel.place(x=200, y=500, anchor=CENTER)

happyImg = PhotoImage(file='icons/happy.png')
sadImg = PhotoImage(file='icons/happy.png')
profImg = PhotoImage(file='icons/happy.png')

emojiLabel1 = Label(root, background="DarkSeaGreen4")
emojiLabel1.place(x=10, y=350)
emojiLabel2 = Label(root, background="DarkSeaGreen4")
emojiLabel2.place(x=320, y=350)

root.bind("<Return>", play)
root.mainloop()
