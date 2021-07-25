import random
import time
from tkinter import Entry, Label
from tkinter.constants import END
from turtle import RawTurtle
from datamuse import datamuse

def InitializeRiddleList():
    riddle_bank = open("output.txt")
    riddle_library = []
    for line in riddle_bank:
        riddle = line.split("?")
        riddle_library.append(riddle)
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

def verify_answer(user_input: Entry, shortened_answer: str, score: int, pen: RawTurtle, score_label: Label):
    user_input = user_input.get().lower()
    shortened_answer = shortened_answer.lower()
    if user_input == shortened_answer:
        score += 50
        user_input.delete(0, END)
        score_label.configure(text="Score: " + str(score))
        time.sleep(2)
        pen.clear()
        if score >= 100:
            return


riddlelist = InitializeRiddleList()
riddleitem = RandomRiddleItem(riddle_library=riddlelist)
print(riddleitem)