from tkinter import *
from turtle import *
from GameMechanics import *
import random

showMenuAll = True
userInput = ""
labelScore = 0

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
turtleCanvas = TurtleScreen(canvas)
turtleCanvas.bgcolor("#5d8fee")
pen = RawTurtle(turtleCanvas)
pen.hideturtle()

def showMenuTitle(text, fontSize):
    canvas.create_text(
        10, -150,
        text=text,
        fill="white",
        font= ("Calibri", int(fontSize)),
        tags="menu",
        width=450
    )
def showQuestion(text, fontSize):
    canvas.create_text(
        10, -150,
        text=text,
        fill="white",
        font= ("Calibri", int(fontSize)),
        tags="menu",
        width=450
    )

riddle_list = InitializeRiddleList()
riddle_item = RandomRiddleItem(riddle_library=riddle_list)


showMenuTitle("Riddle Game", 37.0)

def tester():
    print("printing")

def btnClicked():
    global showMenuAll
    showMenuAll = False
    print("clearing")
    canvas.delete("menu")
    showQuestion(riddle_item["question"], 12.0)
    global userInput
    userInput = showEntry()
    submitBtn()
    showHintBtn()
    userInput.bind("<Button-1>", clearPlaceholder)



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
        0, 150,
        text="HOW TO WIN:\n\nAnswer 10 riddles consecutively to win the game. Good luck!",
        fill="white",
        font=("Calibri", int(10.0)),
        tags="menu"
    )
    canvas.create_text(
        0, 200,
        text="Made by Harith & Sydney",
        fill="white",
        font=("Calibri", int(10.0), "italic"),
        tags="menu"
    )

# tempBtn = 
showMenuBtn()
showInstructions()

def showEntry():
    entry = Entry(
        borderwidth=0,
        highlightthickness=0,
        relief="flat"
    )
    entry.place(
        x= 186, y= 300,
        width=127,
        height=30
    )
    entry.insert(0, "Enter your answer here")
    return entry


def clearPlaceholder(e):
    userInput.delete(0, "end")


def showScore(score):
    label = Label(
        text="Score: " + str(score),
        bg="#5d8fee",
        fg="white"
    )
    label.place(
        x = 430, y = 0 
    )

def showHintBtn():
    hint = Button(
        borderwidth=0,
        highlightthickness=0,
        text="Generate Hint",
        relief="flat",
        bg="#407CF3",
        fg="white",
        command= lambda:[readAloud(text="The answer rhymes with " + riddle_item["hints"][generateIndex()]["word"]), generateIndex()]
    )
    hint.place(
        x= 350, y= 400,
        width=107,
        height=30
    )

showScore(labelScore)

def generateIndex():
    indexRand = random.randint(0, 5)
    print(indexRand, riddle_item["shortened_answer"])
    return indexRand

def submitBtn():
    submit = Button(
        borderwidth=0,
        highlightthickness=0,
        text="Submit",
        relief="flat",
        bg="#407CF3",
        fg="white",
        command=lambda:[verify_answer(user_input=userInput, shortened_answer=riddle_item["shortened_answer"], score=labelScore, pen=pen, read_aloud=True)]
    )
    submit.place(
        x=186, y=350,
        width=127,
        height=30
    )




window.resizable()
window.mainloop()