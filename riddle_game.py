import random
import pyttsx3
import turtle
from datamuse import datamuse
# the code above is import the external libraries we need to make this game work 



# --- INITIALIZING THE GAME SCREEN --- #
screen = turtle.Screen()
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()
pen.goto(150, 250)
pen.write('SCORE: ', move=False, font=['Courier', 16])
api = datamuse.Datamuse()
engine = pyttsx3.init()
end_game = False

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
    index = random.randint(0, len(game_dictionary))
    question_list = game_dictionary[index]
    game_dictionary.remove(question_list)
    # The question_list is a list containing the question and the answer 
    raw_answer = question_list[1].replace(",", "", 1)
    raw_answer = raw_answer.replace(".", "")
    # formatting answer to a single word
    x = raw_answer.split()
    primary_answer = x[len(x)-1]
    hint_rhymes = api.words(rel_rhy = primary_answer, max = 5)
    return [question_list[0], question_list[1], hint_rhymes]

def formatString(sentence, max):
    #print(len(sentence))
    count = 0
    start = 0
    spaces = 0
    sentence_list = []
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            spaces +=1
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

def verify_answer(real_answer, user_answer):
    normalized_answer = real_answer.lower()
    normalized_user_answer = user_answer.lower()
    if normalized_user_answer in normalized_answer:
        print('Correct')
        # then we increase the score or something
    print('i am working')


riddle_list = Pick_question()
question = riddle_list[0]
pen.goto(-250, 100)
new_question = formatString(question, 7)
new_question.reverse()
for i in range(len(new_question)):
    current_y = pen.ycor()
    pen.goto(-250, current_y + 14)
    print(new_question[i])
    pen.write(new_question[i], False, font=["Courier", 13])

answer = riddle_list[1]
hint = riddle_list[2]
if hint is None:
    print("null")
else:
    print(hint[0]['word'])
engine.say(question)
engine.say("I'll give you a word that rhymes with it: " + hint[0]['word'])
engine.say("The answer is " + answer)
engine.runAndWait()

user_input = screen.textinput("INPUT", "what am i?")
verify_answer(answer, user_input)

screen.exitonclick()
