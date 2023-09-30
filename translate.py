import gtts
import os

def read_file ():
    global words_bank
    result = os.listdir ("PyLearn7-Assignment8")

    if "translate.txt" in result:

        f = open ("PyLearn7-Assignment8/translate.txt")
        
        temp = f.read().split ('\n')

        words_bank = []
        for i in range (0, len(temp), 2):
            my_dict = {"en": temp[i], "pr": temp[i+1]}
            words_bank.append (my_dict)
        
        f.close ()
    else:
        print ("Words bank file not found!!!")
        exit (0)

def translate_english_to_persian ():
    
    global output
    user_text = input ('enter your english text: ')
    user_words = user_text.split (' ')

    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word ["en"]:
                output = output + word ["pr"] + " "
                break
            elif user_word == word ["en"] + ".":
                output = output + word ["pr"] + "."
                break
        else:
            output = output + user_word + " "

    print (output,'\n')

def translate_persian_to_english ():

    global output
    user_text = input ('enter your Persian text: ')
    user_words = user_text.split (' ')

    output = ""

    for user_word in user_words:
        for word in words_bank:
            if user_word == word ["pr"]:
                output = output + word ["en"] + " "
                break
            elif user_word == word ["pr"] + ".":
                output = output + word ["en"] + "."
                break
        else:
            output = output + user_word + " "

    print (output,'\n')

def voice ():
    v = gtts.gTTS (output, lang= 'en', slow = False)

    v.save ("PyLearn7-Assignment8/voice.mp3")

def add_word ():

    new_word_en = input ("enter your new word in English: ")
    new_word_pr = input ("enter your new word in Persian: ")
    file = open ("PyLearn7-Assignment8/translate.txt", "a")
    file.write ('\n' + new_word_en)
    file.write ('\n' + new_word_pr)


def show_menu ():
    print ("Welcome to my translation program.")
    print ("1- English to Persian translation")
    print ("2- Persian to English translation")
    print ("3- add a new word to database")
    print ("4- exit")


read_file ()

while True:
    show_menu ()
    choice = int (input("enter your choice: "))

    if choice == 1:
        translate_english_to_persian ()
        voice ()
    elif choice == 2:
        translate_persian_to_english ()
        voice ()
    elif choice == 3:
        add_word ()
    elif choice == 4:
        exit (0)