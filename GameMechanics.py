import random
import time
from tkinter import Entry, Label, Text
from tkinter.constants import END
from turtle import RawTurtle
from datamuse import datamuse
import pyttsx3
engine = pyttsx3.init()

def InitializeRiddleList():
    riddle_bank = open("output.txt")
    riddle_library = []
    for line in riddle_bank:
        riddle = line.split("?")
        riddle_library.append(riddle)
    _init_voice()
    return riddle_library

def RandomRiddleItem(riddle_library: list):
    index = random.randint(0, len(riddle_library) - 1)
    riddle = riddle_library[index]
    # after a riddle is picked we remove it from the list 
    riddle_library.remove(riddle)
    riddle_question = riddle[0].replace(".", "", 1)
    riddle_answer = riddle[1].replace(",", "", 1)
    riddle_answer = riddle_answer.replace(".", "", 1)
    riddle_answer = riddle_answer.replace("\n", "", 1)
    # here we format the riddle question and the answer and then return a dictionary
    hint_dictionary = _generateHint(riddle_answer)
    return {"question": riddle_question, "answer": riddle_answer, "shortened_answer": hint_dictionary[0], "hints": hint_dictionary[1]}



def _generateHint(answer: str):
    api = datamuse.Datamuse()
    try:
        if "/" or "\\" in answer:
            print('weird symbol in answer')
    except:
        pass
    split_answer = answer.split()
    answer_head = split_answer[len(split_answer) - 1]
    hint = api.words(rel_rhy= answer_head, max = 5)
    return [answer_head, hint]

def verify_answer(user_input: Entry, shortened_answer: str, score: int, pen: RawTurtle, read_aloud:bool):
    userInput = user_input.get().lower()
    shortenedAnswer = shortened_answer.lower()
    result_text = ''
    if userInput == shortenedAnswer:
        score += 10
        user_input.delete(0, END)
        # score_label.configure(text="Score: " + str(score))
        # time.sleep(2)
        result_text = "THAT IS CORRECT"
        pen.write(result_text, move=False, align="center")
        if score >= 100:
            result_text = "CONGRATULATIONS YOU HAVE COMPLETED THE GAME"
            pen.write(result_text, move=False, align="center")
    else:
        result_text = "THAT IS INCORRECT"
        pen.write(result_text, move=False, align="center")

    if read_aloud:
        readAloud(result_text)

def readAloud(text:str):
    engine.say(text)
    engine.runAndWait()

def _init_voice():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 175)
