from tkinter import *

slideTexts = ""
count = 0


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
root.mainloop()
