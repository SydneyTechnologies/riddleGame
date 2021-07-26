from tkinter import *
from turtle import color


showMenuAll = True

window = Tk()
window.geometry("500x450")
window.configure(bg="#5d8fee")
canvas = Canvas(
    window,
    bg="#5d8fee",
    height=450,
    width=500,
    bd=0,
    highlightthickness=0
)
canvas.place(x= 0, y= 0)

def showMenuTitle(text, fontSize):
    canvas.create_text(
        242.0, 127.0,
        text=text,
        fill="white",
        font= ("Calibri", int(fontSize))
    )

showMenuTitle("Riddle Game", 37.0)

def tester():
    print("printing")

def btnClicked():
    global showMenuAll
    showMenuAll = False
    print("clearing")
    # if showMenuAll:
    #     showMenuBtn()
    #     showInstructions()
    # else:
    #     # tempBtn.delete()
    canvas.delete("menu")
    # tempBtn.destroy()

def showMenuBtn():
    if showMenuAll == True:
        btnFunc = btnClicked
        cordY = 216
    else:
        btnFunc = tester
        cordY = 380
    button = Button(
        borderwidth=0,
        highlightthickness=0,
        text="Play",
        relief="flat",
        bg="#407CF3",
        fg="white",
        command= lambda:[btnFunc(), button.destroy()],
        # command=btnFunc,
    )
    button.place(
        x= 186, y= cordY,
        width=127,
        height=30
    )
    # return button


def showInstructions():
    canvas.create_text(
        250.0, 375.0,
        text="HOW TO WIN:\n\nAnswer 10 riddles consecutively to win the game. Good luck!",
        fill="white",
        font=("Calibri", int(10.0)),
        tags="menu"
    )
    canvas.create_text(
        250.0, 420.0,
        text="Made by Harith & Sydney",
        fill="white",
        font=("Calibri", int(10.0), "italic"),
        tags="menu"
    )

# tempBtn = 
showMenuBtn()
showInstructions()

window.resizable(False, False)
window.mainloop()