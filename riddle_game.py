import random
from tkinter.constants import BOTTOM, LEFT, RIGHT
import pyttsx3
import turtle
import tkinter 
from tkinter.ttk import *
from datamuse import datamuse
import time
from requests.models import StreamConsumedError
# the code above is import the external libraries we need to make this game work 



# --- INITIALIZING THE GAME SCREEN --- #
TK = tkinter.Tk(className="Riddle Game")
screen = tkinter.Canvas(master= TK, width=500, height=500)
screen.pack()
pen = turtle.RawTurtle(screen)
bottom_frame = tkinter.LabelFrame(TK, bd=1, text="Your Score")
bottom_frame.pack(side=LEFT)
scoreLabel = tkinter.Label(bottom_frame, bd=1)
scoreLabel.pack()
pen.hideturtle()
pen.penup()
# scoreTurtle.hideturtle()
# scoreTurtle.penup()
# scoreTurtle.goto(150, 250)
score = 0
# scoreTurtle.color('grey')
# scoreTurtle.write('SCORE: ' + str(score), move=False, font=['Courier', 16])
api = datamuse.Datamuse()
engine = pyttsx3.init()
end_game = False
ans = pen.clone()
user_input_answer = "$"
answer = ""
hintGlobal = ""
question = ""

# style.configure('TkButton', font=('calibri', 20,'bold'), borderwidth = '2')

# -- INITIALIZE GAME VOICE -- #
def Init_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 175)
Init_voice()

# -- GETTING RIDDLES --- #
asset_file = open("output.txt")
game_dictionary = []
for line in asset_file:
    x = line.split("?")
    game_dictionary.append(x)



# -- PICKING A QUESTION -- #
def Pick_question():
    index = random.randint(0, len(game_dictionary) - 1)
    print(index, len(game_dictionary))
    question_list = game_dictionary[index]
    print(question_list[0], index, question_list[1])
    game_dictionary.remove(question_list)
    print(question_list[1])
    # The question_list is a list containing the question and the answer 
    raw_answer = question_list[1].replace(",", "", 1)
    raw_answer = raw_answer.replace(".", "")
    # formatting answer to a single word
    x = raw_answer.split()
    primary_answer = x[len(x)-1]
    hint_rhymes = api.words(rel_rhy = primary_answer, max = 5)
    return [question_list[0], question_list[1], hint_rhymes]

# Pick_question()
print(game_dictionary[1])
def formatString(sentence, max):
    #print(len(sentence))
    count = 0
    start = 0
    spaces = 0
    sentence_list = []
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            spaces +=1
    if spaces < max:
        sentence_list.append(sentence)
        return sentence_list
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            count +=1
            if count % max == 0:
                new_sentence = sentence[start:i]
                sentence_list.append(new_sentence)
                print(new_sentence)
                start = i
            if count == (spaces // max) * max:
                sentence_list.append(sentence[start:])
                print(sentence[start:])
    return sentence_list

def verify_answer():
    normalized_answer = answer.lower()
    normalized_user_answer = user_input.get().lower()
    correct = True
    if normalized_user_answer in normalized_answer:
        print('Correct')
        global score
        score += 1
        scoreLabel.configure(text="Score: " + str(score))
        # scoreTurtle.undo()
        # scoreTurtle.write('SCORE: ' + str(score), move=False, font=['Courier', 16])
        writeAnswer(normalized_user_answer, correct)
        time.sleep(2)
        pen.clear()
        ans.clear()
        gameLoop()
        # then we increase the score or something
    else:
        correct = False
        writeAnswer(normalized_user_answer, correct)


def writeAnswer(answer, isCorrect):
    y = pen.ycor()
    ans.goto(0, y - 100)
    concat = " is correct"
    if isCorrect == True:
        ans.color('green')
    else:
        ans.color("red")
        concat = " is wrong, start again"
    ans.write(answer + " " + concat, move= False, font=['Courier', 16], align='center')


def gameLoop():
    riddle_list = Pick_question()
    global question
    question = riddle_list[0]
    pen.goto(-100, 100)
    pen.color('black')
    new_question = formatString(question, 7)
    new_question.reverse()
    for i in range(len(new_question)):
        current_y = pen.ycor()
        pen.goto(0, current_y + 14)
        print(new_question[i])
        pen.write(new_question[i], False, font=["Courier", 13], align='center')

    global answer
    answer = riddle_list[1]
    global hintGlobal
    hintGlobal = riddle_list[2]
    engine.say(question)
    # engine.say("The answer is " + answer)
    engine.runAndWait()

    # user_input = screen.textinput("INPUT", "what am i?")
   
    # verify_answer(answer, user_input_answer)

user_input = tkinter.Entry(TK)
user_input.pack()
btn = tkinter.Button(master = TK, text="Submit")
btn.pack()
btn.configure(command= verify_answer)


def hint_generator():
    global hint
    hint = hintGlobal
    print(hint)
    hintIndex = random.randint(0, 4)
    if hint == []:
        wordToSay = "Sorry, there are no hints for this question"
    else:
        wordToSay = "I'll give you a word that rhymes with it: " + hint[hintIndex]['word']
    engine.say(wordToSay)
    engine.runAndWait()

hintBtn = tkinter.Button(master = TK, text="Generate Hint")
hintBtn.pack(side=RIGHT)
hintBtn.configure(command= hint_generator)


def repeatQuestion():
    engine.say(question)
    engine.runAndWait()

repeatBtn = tkinter.Button(master= TK, text="Repeat Question", bg="#6495ED")
repeatBtn.pack(side=RIGHT)
repeatBtn.configure(command= repeatQuestion)



gameLoop()
screen.mainloop()