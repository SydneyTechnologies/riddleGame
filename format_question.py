word = input()

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
    
print(formatString(word, 7))