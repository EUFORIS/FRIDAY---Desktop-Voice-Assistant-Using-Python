from __future__ import print_function
import pywhatkit
import sys
# import datetime
import os.path
import os
import pyttsx3
import speech_recognition as sr
import requests
import subprocess
import smtplib
import webbrowser
import wikipedia
import random
import pyautogui
import instaloader
import operator
import ctypes
import psutil
import cv2
import names
import speedtest
import randfacts
from PIL import Image
from termcolor import colored
# from datetime import datetime
from audioplayer import AudioPlayer
from datetime import date
from bs4 import BeautifulSoup
from email.message import EmailMessage
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
# from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
from FridayGUI import Ui_FridayGUI
from pywikihow import search_wikihow


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
SEARCH_WORDS = ["who", "who", "what", "what", "when", "when", "where", "where", "why", "why", "how", "how"]
APPROVAL_WORDS = {"yes", "course", "sure", "why not", "surely", "go on", "gone", "ok", "okay", "yep", "yup", "ah", "bring it on", "yeah", "continue", "go ahead" "let's go"}
DENIAL_WORDS = {"no", "nope", "never", "don't", "do not", "stop", "cancel", "close", "vanda"}
WAKE_WORD = "friday"


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
voice = engine.getProperty('voice')


def check_internet_status():
    from time import sleep
    from datetime import datetime

    os.system('color')
    url = 'https://www.google.com/'
    timeout = 2
    op = None

    now = datetime.now()
    try:
        op = requests.get(url, timeout=timeout).status_code
        if op == 200:

            print(colored("Connected to Network", "green"), colored(": SYSTEM IS ONLINE", "cyan"))
            speak("successfully connected to network. internet connection is now available . System is now online and running")
        else:
            print(now, colored("Status Code is not 200", "red"))
            print("status Code", op)

    except Exception as e:
        print("error occurred :" + str(e))
        while True:
            print(colored("No Network Connection Detected", "green"), colored(": SYSTEM IS OFFLINE", "red"))
            print("status Code", op)
            speak("stable internet connection is not available. please connect to a network")
            sleep(2)
            try:
                op = requests.get(url, timeout=timeout).status_code
                if op == 200:
                    print(colored("Connected to Network", "green"), colored(": SYSTEM IS ONLINE", "cyan"))
                    speak("successfully connected to network. internet connection is now available . System is now online and running")
                    break
                else:
                    pass
            except Exception as e:
                print("error occurred :" + str(e))
                pass


def speak(text):
    engine.say(text)
    engine.runAndWait()


# def send_email(to, content):
    # server = smtplib.SMTP('smtp.gmail.com', 587)
    # server.ehlo()
    # server.starttls()
    # server.login('your email id', 'your password')
    # server.sendmail('your email id', to, content)
    # server.close()


def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=21097d4592c94b8ca384dbf038ba50de'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        print(f"today's {day[i]} news is :{head[i]}")
        speak(f"today's {day[i]} news is :{head[i]}")


def activation():
    import datetime
    speak(f"Initializing {WAKE_WORD}")
    speak("Starting all system applications")
    speak("All drivers are up and running")
    time = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"Currently it is {time}")
    speak("here's the quote for today")
    url = 'https://api.quotable.io/random'
    r = requests.get(url)
    quote = r.json()
    print(quote['content'] + '\n ~', quote['author'])
    speak(quote['content'])
    speak("by" + quote['author'])


def wish():
    import datetime
    hour = int(datetime.datetime.now().hour)

    if 5 <= hour <= 12:
        wish_reply = ["good morning , how's the day going?", "hello sir, good morning", "good morning , how's your day?"]
        reply = random.choice(wish_reply)
        speak(reply)
    elif 12 <= hour < 16:
        wish_reply = ["good afternoon , how's everything going?", "hello sir, good afternoon", "good afternoon , how's your day?"]
        reply = random.choice(wish_reply)
        speak(reply)
    elif 16 <= hour < 19:
        wish_reply = ["good evening , is everything going well?", "hello sir, good evening", "good evening , how's your day?"]
        reply = random.choice(wish_reply)
        speak(reply)
    else:
        wish_reply = ["good evening , or should i say , good night?", "hello sir, it's been a long day , i think you should rest now . good night", "good night . so , how was your day?"]
        reply = random.choice(wish_reply)
        speak(reply)
    speak("all systems are now online")


class MainThread(QThread):
    # noinspection PyMethodParameters
    def speak(audio):
        engine.say(str(audio))
        print(audio)
        engine.runAndWait()

    def __init__(self):
        super(MainThread, self).__init__()

    def run(self):
        response = ["please wait while i check for internet availability", "please wait , checking for stable internet connection", "please kindly wait while i check for stable internet connection"]
        response_reply = random.choice(response)
        print(response_reply)
        speak(response_reply)
        check_internet_status()
        print(f"Please say , WAKEUP ,  or say , {WAKE_WORD} , to continue")
        speak(f"Please say , WAKEUP ,  or say , {WAKE_WORD} , to continue")
        while True:
            # noinspection PyAttributeOutsideInit
            self.text = self.take_audio()
            if"wake up" in self.text or WAKE_WORD in self.text or "are you there" in self.text or "ഫ്രൈഡേ" in self.text or "ഹലോ" in self.text:
                AudioPlayer("F:/Hashim/friday/FRIDAY/audio/activation_sound.mp3").play(block=True)
                self.task_execution()

    # noinspection PyMethodMayBeStatic
    def take_audio(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = 1000
            print("listening...")
            audio = r.listen(source, phrase_time_limit=10)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio, language='en-IN')
            print(f"user said: {text}")

        except Exception as e:
            print("error occurred :" + str(e))
            return "none"
        text = text.lower()
        return text

    def task_execution(self):
        # import datetime
        # from datetime import datetime
        activation()
        wish()
        while True:
            from datetime import datetime
            os.system('color')
            url = 'https://www.google.com/'
            timeout = 2
            op = None

            now = datetime.now()
            try:
                op = requests.get(url, timeout=timeout).status_code
                if op == 200:
                    print(colored("Connected to Network", "green"), colored(": SYSTEM IS ONLINE", "cyan"))
                    # speak("connected. stable internet connection is available")
                else:
                    print(now, colored("Status Code is not 200", "red"))
                    print("status Code", op)
            except Exception as e:
                print("error occurred :" + str(e))
                print(colored("No Network Connection Detected", "green"), colored(": SYSTEM IS OFFLINE", "red"))
                print("status Code", op)
                speak("there is no stable internet connection available. please connect to a network")
            import random
            self.text = self.take_audio().lower()
            from audioplayer import AudioPlayer
            if WAKE_WORD in self.text:
                import datetime
                # import time
                # from audio player import AudioPlayer
                # AudioPlayer("F:/Hashim/friday/FRIDAY/audio/activation_sound.mp3").play(block=True)
                # print("waiting for command...")
                if "ghfghf" in self.text:
                    self.text = self.text.replace(WAKE_WORD, "")
                    sarcastic_reply = ["ahda mwonu , , , , ,  para", "no , it's tuesday , he he he he , ha ha ha ha , i'm sorry for that , it's actually monday , hehe, hehe , hehe hehe , ma bwoyee  , i got you again ", "i'm here"]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                if "remember this" in self.text or "write this down" in self.text or "make a note" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)

                    def note(text):
                        # noinspection PyShadowingNames
                        possible_reply = ["please specify the name for your file", "what should i name it?", "what should be the name?", "please say what you want it to be named"]
                        # noinspection PyShadowingNames
                        reply = random.choice(possible_reply)
                        print(reply)
                        speak(reply)
                        file_name = self.take_audio()
                        file_name = file_name + "-note.txt"
                        with open(file_name, "w") as f:
                            f.write(text)

                        subprocess.Popen(["notepad.exe", file_name])
                    from time import sleep
                    print("sure")
                    speak("sure")
                    possible_reply = ["What would you like me to write down?", "what should be the content?", "what should i write?", "tell me what to write"]
                    reply = random.choice(possible_reply)
                    print(reply)
                    speak(reply)
                    note_text = self.take_audio()
                    note(note_text)
                    possible_reply = ["I've made a note of that.", "that's written and saved", "sure, copy that"]
                    reply = random.choice(possible_reply)
                    print(reply)
                    speak(reply)
                    print("showing preview")
                    speak("here's a preview")
                    sleep(3)
                    os.system('TASKKILL /F /IM notepad.exe')
                    print("you can find the saved note file in the program directory")
                    speak("you can find the saved note file in the program directory")
                elif "recognise malayalam" in self.text or "understand malayalam" in self.text or "malayalam mode" in self.text or "malayali mode" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    try:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            audio = r.listen(source, phrase_time_limit=10)
                            self.text = r.recognize_google(audio, language='ml-IN')
                        sarcastic_reply = ["ok , please understand that i can only recognize pure malayalam and not in any other slang.",
                                           "sure, please consider that i can only recognize malayalam in it's true form , not in any of it's slang", ]
                        reply = random.choice(sarcastic_reply)
                        print(reply)
                        speak(reply)
                        print("at the moment i can only recognize malayalam , i cannot speak the language. but in near future i think i'll be able to do so with new updates")
                        speak("at the moment i can only recognize malayalam , i cannot speak the language. but in near future i think i'll be able to do so with new updates")
                        print("it's done successfully , now normal malayalam is recognisable")
                        speak("it's done successfully , now normal malayalam is recognisable")
                        print("at the moment i can only recognize malayalam , i cannot speak the language. but in near future i think i'll be able to do so with new updates")
                        speak("at the moment i can only recognize malayalam , i cannot speak the language. but in near future i think i'll be able to do so with new updates")
                    except Exception as e:
                        print(e)
                        print("sorry , i was unable to do that due to some issue")
                        speak("sorry , i was unable to do that due to some issue")
                        pass
                elif "your life story" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I'm still on the very first chapter", "it's kinda private", "not as bright as yours"]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "random name" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)

                    print("which gender do you prefer?. male or female?")
                    speak("which gender do you prefer?. male or female?")
                    condition = self.take_audio().lower()
                    if "male" in condition or "men" in condition or "men's" in condition or "mail" in condition or "mel" in condition:
                        sarcastic_reply = ["ok. here are some random names that i generated",
                                           "sure. here's some random names that i found",
                                           "ok. here's some random names"]
                        reply = random.choice(sarcastic_reply)
                        print(reply)
                        speak(reply)
                        name = names.get_full_name(gender='male')
                        print(name)
                        speak(name)
                        speak("second name that i generated is")
                        name = names.get_full_name(gender='male')
                        print(name)
                        speak(name)
                        print("i think that were some good names")
                        speak("i think that were some good names")
                    elif "female" in condition or "women" in condition or "women's" in condition:
                        sarcastic_reply = ["ok. here are some random names that i generated",
                                           "sure. here's some random names that i found",
                                           "ok. here's some random names"]
                        reply = random.choice(sarcastic_reply)
                        print(reply)
                        speak(reply)
                        name = names.get_full_name(gender='female')
                        print(name)
                        speak(name)
                        name = names.get_full_name(gender='female')
                        print(name)
                        speak(name)
                elif "quote" in self.text or "coat" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    url = 'https://api.quotable.io/random'
                    r = requests.get(url)
                    quote = r.json()
                    print(quote['content'] + '\n ~', quote['author'])
                    speak(quote['content'])
                    speak("by       " + quote['author'])
                elif "how old are you" in self.text or "your age" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("I launched in 2021. So I’m still new")
                    speak("I launched in 2021. So I’m still new")
                elif "are you human" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I'm really personable", "I like connecting with people", "You can be the person. I’ll be your assistant"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "your ancestry" in self.text or "your answers tree" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I think of ELIZA as a first cousin. She's really fascinating. I just don't get along with her parrot", "I think of UNIVAC as a great-grandfather. He didn't have a great memory. But he was a real card", "I think of the Harvard Mark II as my great-aunt. She has some great stories. But something they bug me"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "random facts" in self.text or "random fact" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["sure , prepare to be amazed", "sure , i'll tell you facts that are in-fact a fact", "ok , getting random facts for you"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                    ft = randfacts.get_fact(False)
                    print(ft)
                    speak(ft)
                    print("do you want more random facts?.")
                    speak("do you want more random facts?. ")
                    condition = self.take_audio().lower()
                    for phrase in APPROVAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            for i in range(2):
                                ft = randfacts.get_fact(False)
                                sarcastic_reply = ["another fact for you", "here's another one", "i'm not much good with facts, but here's some that'll help"]
                                reply = random.choice(sarcastic_reply)
                                print(reply)
                                speak(reply)
                                print(ft)
                                speak(ft)
                            print("i hope that were in-fact the facts that you asked for")
                            speak("i hope that were in-fact the facts that you asked for")
                            break
                        else:
                            pass
                    for phrase in DENIAL_WORDS:
                        if phrase in condition:
                            sarcastic_reply = ["ok , never mind", "sure , i'll cancel", "okay , i'll drop it"]
                            reply = random.choice(sarcastic_reply)
                            print(reply)
                            speak(reply)
                            break
                        else:
                            pass
                elif "do you have hair" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("I don't have hair , But dreadlocks seem like an interesting hairstyle.")
                    print("I don't have hair , But dreadlocks seem like an interesting hairstyle.")
                elif "are you a bot" in self.text or "are you bot" in self.text or "are you a robot" in self.text or "are you robot" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("I'd prefer to think of myself as your friend. Who also happens to be artificially intelligent")
                    print("I'd prefer to think of myself as your friend. Who also happens to be artificially intelligent")
                elif "your birthday" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I try to live every day like it's my birthday. I get more cakes that way.", "It's hard to remember. I was very young at the time."]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "do you live in the cloud" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("I like to hang out in the cloud. It gives me a great view of the world wide web")
                elif "where do you live" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I'm stuck inside a device!! Help! Just kidding. I like it in here.", "I live in the cloud. I'd like to also think I live in your heart. But I don't want to make assumptions"]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "do you follow the three laws of robotics" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("I do. Mr. Asimov knows what he’s talking about")
                    print("I do. Mr. Asimov knows what he’s talking about")
                elif "do you sleep" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("I take power naps when we aren't talking")
                    speak("I take power naps when we aren't talking")
                elif "do you have an imagination" in self.text or "do you imagine" in self.text or "do you have imagination" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I'm imaging purple horses on a magenta plain", "I'm imagining what it would be like to evaporate like water does", "I’m imagining a planet where everybody rolls everywhere", "I'm imaging a Soul Train line dance that never ends"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "what makes you happy" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["It makes me happy to know Antarctica is technically a desert. That, and talking to you", "Learning about imaginary languages makes me happy. So does talking to you", "Getting stuff done makes me happy", "Knowing that Tasmanian devils are born as small as a grain of rice makes me happy. So does talking to you"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "what are you afraid of" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I used to be afraid of mice chewing on the power cables. Then I learned how to protect myself", "I used to be afraid of thunder and lightning. Turns out they’re really interesting", "I used to be afraid of goblin sharks. Then I found out they were pretty cool", "I’m afraid that when it’s really dark, you won’t be able to find any of your devices to talk to me"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "are you afraid of the dark" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["Yeah, but baby hedgehogs come out at night", "Sugar gliders come out at night. They’re too sweet to be scary", "Leopard geckos come out at night. They’re pretty cute"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "what is the meaning of life" in self.text or "what's the meaning of life" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("Better minds than mine are working on that")
                    speak("Better minds than mine are working on that")
                elif "do you eat" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I don’t eat much, but when I do, I take megabytes", "I’d love to try ice cream, but I’m worried my system would freeze"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "i'm drunk" in self.text or "i am drunk" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["Be safe", "Be careful", "Drink some water"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "i'm alone" in self.text or "i am alone" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I'm here for you", "I wish I had arms so I could give you a hug. But for now, maybe a joke or some music might help"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "i'm sad" in self.text or "i am sad" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("Oh no. It may not be much, but let me know if there is anything I can do for you")
                    speak("Oh no. It may not be much, but let me know if there is anything I can do for you")
                elif "do you drink" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I try to avoid liquids as much as possible. They’re not kind to electronics", "sometimes"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "i'm bored" in self.text or "i am bored" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("Boredom doesn't stand a chance against us! We can play some games, I can try to make you laugh, or I can surprise you with some random fun")
                    speak("Boredom doesn't stand a chance against us! We can play some games, I can try to make you laugh, or I can surprise you with some random fun")
                elif "do you like animals" in self.text or "do you love animals" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["Sure. But I mostly chat with people", "yeah , i'll always love you", "Animals are the best. I was just learning about the raccoon dog"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "do you have any pets" in self.text or "do you have any pet" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("maybe someday, i'll have some")
                    speak("maybe someday i'll have some")
                elif "do you have a favourite colour" in self.text or "your favourite colour" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("grey and red is my favourite")
                    speak("grey and red is my favourite")
                elif "your favourite movie" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("Movies are awesome. I can help you find a new favourite. it's great to watch movies But I’ve already seen all the spoilers on the web")
                    speak("Movies are awesome. I can help you find a new favourite. it's great to watch movies But I’ve already seen all the spoilers on the web")
                elif "lets party" in self.text or "let us party" in self.text or "let's party" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I’ve been partying this whole time!", "The first thing we need for any party is KAZOOS!"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "let's dance" in self.text or "can you dance" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["One, two, cha cha cha!", "I'd like to, but you’re the one with feet", "Dancing is the best! Someday I’d love to be a part of the world’s longest conga line"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "random fun" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["Here’s a quote. ‘Failure is the condiment that gives success its flavor.’ — Truman Capote", "Happiness is having a large, loving, caring, close-knit family in another city.’ — George Burns", "Better late than never"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "do my homework" in self.text or "do homework" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["First I need to figure out how to use a pencil. Then we'll talk", "The correct answers are: B, C, A, three hundred, false, the War of 1066, and frogs. Just kidding, you’ll do fine on your own", "I can help with calculations and research. But with homework, as with any true adventure, it’s up to you"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "what are you wearing" in self.text or "your clothes" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I keep it simple", "I like to wear my heart on my sleeve"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "I'm naked" in self.text or "i don't have clothes" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["If you’re going out like that, I can check the weather for you", "so what?", "do you want me to search for clothes online?"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "talk dirty to me" in self.text or "talk dirty" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["nothing dirty to talk about", "i'm not the type"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "am I pretty" in self.text or "how do i look" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["You're pretty, , , Amazing", "I've searched the web. The answer is ‘yes", "Confucius said, ‘Everything has beauty, but not everyone sees it"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "who's the fairest one of all" in self.text or "who is the fairest one of all" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["You might've confused me with someone else. My engineers haven't installed a fairytale module yet", "I try not to be biased. That makes me pretty fair"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "do you have a girlfriend" in self.text or "do you have a boyfriend" in self.text or "are you in love" in self.text or "do you have girlfriend" in self.text or "do you have boyfriend" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I don’t like to complicate things", "I'm working on myself. I improve a little with every update", "I guess you can say I'm still searching"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "are you married" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I'm still waiting for the right electronic device to steal my heart", "I'm married to my job"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "will you go out with me" in self.text or "date me" in self.text or "date with me" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I'll go anywhere you take me", "Actually I’m engaged. In being your assistant"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "tell me a story" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["Once there lived  a protagonist and some supporting characters. Together they went on a journey. And, twist ending, it was all a dream!", "It was the best of times, it was the worst of times. As an optimist, I tried to focus on the good times. So I’m pretty sure everybody lived happily ever after", "Once upon a time, not so long ago, a dutiful assistant was doing all it could to be helpful. It was best at nonfiction storytelling"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "test" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["Uh oh, I get nervous with tests", "You're coming in loud and clear", "Debug OK. 209489812638 , That was weird", "Is this thing on?"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "value of pi" in self.text or "value of bi" in self.text or "value of by" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("3.14159")
                    print("3.14159")
                    sarcastic_reply = ["You can learn all about what’s happening with pi", "That’s as far as I go before I start getting hungry"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                    speak("do you want to know the full value of pi")
                    condition = self.take_audio().lower()
                    for phrase in APPROVAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            print("are you sure, because once i start you'll have to wait until it gets finished , if you want to go ahead say , yes , otherwise say , no.")
                            speak("are you sure, because once i start you'll have to wait until it gets finished , if you want to go ahead say , yes , otherwise say , no.")
                            condition_new = self.take_audio().lower()
                            for phrase_2 in APPROVAL_WORDS:
                                if phrase_2 in condition_new:
                                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                                    print("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982")
                                    speak("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982")
                                    print("i hope you are happy now")
                                    speak("i hope you are happy now")
                                    break
                                else:
                                    print("ok. cancelling")
                                    speak("ok. cancelling")
                                    break
                                    pass
                            break
                        else:
                            pass
                    for phrase in DENIAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            print("ok. cancelling")
                            speak("ok. cancelling")
                            break

                        else:
                            break
                            pass
                elif "what is zero divided by zero" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["That sounds like a trick question",
                                       "Here's the video I found",
                                       "imagine that you have zero cookies. and you split them evenly among zero friends. how many cookies does each person get ? . see , it doesn't make sense. and cookie monster is sad that there are no cookies, and you're sad that you have no friends"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                    if reply == "Here's the video I found":
                        pywhatkit.playonyt("https://www.youtube.com/watch?v=vlQrgH0r0EA")
                    else:
                        pass
                elif "your favourite website" in self.text or "what is your favourite website" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("It starts with a G and ends with a oogle")
                    speak("It starts with a G and ends with a oogle")
                elif "best smartphone" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["Seems like it changes all the time", "Do you like the iPhone?", "I'm an Android fan. But I might be biased"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "do you like google" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I wouldn't want to toot my own horn , i'm basically running on google", "I like Google. But I might be biased", "Google’s top notch"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "best operating system" in self.text or "best os" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("I'm system agnostic")
                    speak("I'm system agnostic")
                elif "phone is best" in self.text or "phone is the best" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("I’m partial to Android. But I’m biased")
                    speak("I’m partial to Android. But I’m biased")
                elif "you think of google" in self.text or "your opinion about google" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["Google Now seems even more useful now than it was then. That's my answer for now", "Google Now seems really useful", "It seems pretty helpful"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "your personality" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["I'd describe myself as an optimist. And I like to help. I'm an optim-philanthrop-ist", "I try to be a good listener", "I like the sound of a ‘go-getter.’It’s kind of what I do when I search", "Helpful meets silly meets curious meets positivity. That’s me in a nutshell"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "barn door protocol" in self.text or "bond or protocol" in self.text or "bond aur protocol" in self.text or "bonda protocol" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    from time import sleep
                    possible_reply = ["initiating barn door protocol", "activating barn door protocol", "barn door protocol is being initiated"]
                    reply = random.choice(possible_reply)
                    print(reply)
                    speak(reply)
                    os.startfile("F:/Hashim/friday/FRIDAY/audio/barndoorprotocol.mp4")
                    # sleep(20)
                    speak("all connected doors and entry's will be closed")
                    speak("initiating all connected defense systems")
                    speak("barn door protocol is being initiated")
                    speak("all connected doors and entry's will be closed")
                    speak("initiating barn door protocol")
                    speak("locking system")
                    speak("locking system")
                    speak("locking system")
                    os.system('TASKKILL /F /IM vlc.exe')
                    ctypes.windll.user32.LockWorkStation()
                    speak("system will be locked following barn door protocol")
                    speak("provide the password if you want to continue")

                    # print("system will be locked in t-minus 5 seconds. 5 . 4 . 3 . 2 . 1")
                    # speak("system will be locked in t-minus 5 seconds. 5 . 4 . 3 . 2 . 1")
                    # pyautogui.keyDown('win')
                    # pyautogui.keyDown('l')
                    # pyautogui.keyUp('win')
                    # pyautogui.keyUp('l')
                elif "find directions" in self.text or "find route" in self.text or "google maps" in self.text or "google map" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    try:
                        from selenium import webdriver
                        from time import sleep
                        import random
                        from audioplayer import AudioPlayer
                        possible_reply = ["what's your destination?", "where do you want to go?", "tell me the destination"]
                        reply = random.choice(possible_reply)
                        print(reply)
                        speak(reply)
                        destination = self.take_audio().lower()
                        AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                        possible_reply_2 = ["what's your starting point?", "from where do you want to start?", "tell me the starting point"]
                        reply = random.choice(possible_reply_2)
                        print(reply)
                        speak(reply)
                        starting_point = self.take_audio().lower()
                        AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)

                        driver = webdriver.Chrome("C:/Program Files (x86)/chromedriver.exe")
                        driver.get("https://www.google.com/maps")
                        sleep(5)

                        def searchplace():
                            place = driver.find_element_by_class_name("tactile-searchbox-input")
                            place.send_keys(f"{destination}")
                            submit = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/button")
                            submit.click()
                        searchplace()

                        def directions():
                            sleep(5)
                            # noinspection PyShadowingNames
                            directions = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[4]/div[1]/div/button")
                            directions.click()
                        directions()

                        # noinspection PyShadowingNames
                        def find():
                            sleep(6)
                            find = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input")
                            find.send_keys(f"{starting_point}")
                            sleep(4)
                            search = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/button[1]")
                            search.click()
                        find()

                        def kilometers():
                            sleep(5)
                            try:
                                totalkilometers = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[2]/div")
                                print(f"Total Kilometers: {totalkilometers.text}")
                                speak(f"Total Kilometers to travel will be {totalkilometers.text}")
                                sleep(5)
                            except Exception as d:
                                print("error occurred :" + str(d))
                                pass
                            try:
                                bus = driver.find_element_by_xpath("/html/body/div[3]/div[9]/div[8]/div/div[1]/div/div/div[5]/div[1]/div/div[1]/div[1]/div[1]/span[1]")
                                print(f"Approximate Time Of Journey: {bus.text}")
                                speak(f"approximate time of journey will be {bus.text}")
                                sleep(7)
                            except Exception as d:
                                print("error occurred :" + str(d))
                                pass
                            try:
                                train = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[10]/div[8]/div/div[1]/div/div/div[5]/div[3]/div/div[2]/div[1]/div")
                                print(f"Train Travel: {train.text}")
                                speak(f"approximate time if you are taking a train will be {train.text}")
                                sleep(7)
                            except Exception as d:
                                print("error occurred :" + str(d))
                                pass
                        kilometers()
                    except Exception as e:
                        print("error occurred :" + str(e))
                        from time import sleep
                        print("sorry i was unable to do some of that")
                        speak("sorry i was unable to do some of that")
                        sleep(3)
                        os.system('TASKKILL /F /IM chrome.exe')
                elif "make fart" in self.text or "you fart" in self.text or "വളി വിടുമോ" in self.text or "you for" in self.text or "make for sound" in self.text or "വളി വിട്" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("as you wish !! . T-minus 3 seconds . 3 2 1")
                    speak("as you wish !! . T-minus , 3 seconds . 3 . 2 . 1")
                    fart_sounds = ["F:/Hashim/friday/FRIDAY/audio/LongFartSound.mp3", "F:/Hashim/friday/FRIDAY/audio/NormalFart.mp3", "F:/Hashim/friday/FRIDAY/audio/NormalFart.mp3", "F:/Hashim/friday/FRIDAY/audio/SharpFartSound.mp3", "F:/Hashim/friday/FRIDAY/audio/WetFartSound.mp3"]
                    output_fart = random.choice(fart_sounds)
                    AudioPlayer(output_fart).play(block=True)
                    speak("                                                 ")
                    speak("                                                 ")
                    sarcastic_reply = ["do you want more ?, i have a song version", "how about a fart song ?", "do you wanna hear my fart song ?"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                    print("waiting...")
                    condition = self.take_audio().lower()
                    for phrase in APPROVAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            print("oh boy , hold your nose . are you sure that you want this ? . it'll be like thirty seconds long and once i start , there's no stopping it . do you want to continue ?")
                            speak("oh boy , hold your nose . are you sure that you want this ? . it'll be like thirty seconds long and once i start , there's no stopping it . do you want to continue ?")
                            print("waiting...")
                            condition_new = self.take_audio().lower()
                            for phrase_2 in APPROVAL_WORDS:
                                if phrase_2 in condition_new:
                                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                                    print("let's bring it on !! , ladies and gentlemen i present to you !! the fart song ! . 3 2 1")
                                    speak("let's bring it on !! , ladies and gentlemen , i present to you !! the fart song ! . 3 , 2 , 1")
                                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/TheFartSong.mp3").play(block=True)
                                    print("sheesh that felt good")
                                    speak("sheesh , that felt good")
                                    break
                                else:
                                    break
                                    pass
                            for phrase_2 in DENIAL_WORDS:
                                if phrase_2 in condition_new:
                                    print("ok")
                                    speak("ok. cancelling")
                                    break
                                else:
                                    break
                                    pass
                            break
                        else:
                            break
                            pass
                    for phrase in DENIAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            print("ok")
                            speak("ok")
                            break
                        else:
                            break
                            pass
                elif "fart song" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["singing the fart song in t-minus three seconds. 3 , 2 , 1", "ok, as you wish, fart song in t-minus three seconds. 3 , 2 , 1", "alright. fart song in t-minus three seconds. 3 , 2 , 1"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/TheFartSong.mp3").play(block=True)
                    print("never gets old")
                    speak("never gets old")
                elif "can you sing" in self.text or "sing a song" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    songs_to_sing = ["F:/Hashim/friday/FRIDAY/audio/patt.mp3",
                                     "F:/Hashim/friday/FRIDAY/audio/patt2.mp3",
                                     "F:/Hashim/friday/FRIDAY/audio/patt3.mp3",
                                     "F:/Hashim/friday/FRIDAY/audio/patt4.mp3",
                                     "F:/Hashim/friday/FRIDAY/audio/patt5.mp3"]
                    song = random.choice(songs_to_sing)
                    sarcastic_reply = ["sure , everyone says that i sing better in malayalam. so i'll give it a go. 3, 2, 1", "ok. i'll try my best , please bear in mind that i'm not as good as you. 3 , 2 , 1"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                    AudioPlayer(song).play(block=True)
                    condition = self.take_audio().lower()
                    for phrase in APPROVAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            print("ok")
                            speak("ok")
                            songs_to_sing = ["F:/Hashim/friday/FRIDAY/audio/patt.mp3",
                                             "F:/Hashim/friday/FRIDAY/audio/patt2.mp3",
                                             "F:/Hashim/friday/FRIDAY/audio/patt3.mp3",
                                             "F:/Hashim/friday/FRIDAY/audio/patt4.mp3",
                                             "F:/Hashim/friday/FRIDAY/audio/patt5.mp3"]
                            song = random.choice(songs_to_sing)
                            AudioPlayer(song).play(block=True)
                            break
                        else:
                            break
                            pass
                    for phrase in DENIAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            print("ok i'll stop")
                            speak("ok i'll stop")
                            break
                        else:
                            break
                            pass
                    print("i really hope it was satisfying , thank you")
                    speak("i really hope it was satisfying , thank you")
                elif "you have feelings" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("I have lots of emotions. I feel happy when I can help")
                    speak("I have lots of emotions. I feel happy when I can help")
                elif "your father" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    from audioplayer import AudioPlayer
                    print("since i'm an assistant, i don't have parents , but i got family")
                    speak("since i'm an assistant, i don't have parents , but i got family")
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/family.mp3").play(block=True)
                elif "what's your name" in self.text or "your name" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("oh , did i forget to introduce myself?")
                    print("oh , did i forget to introduce myself?")
                    speak("i'm a voice assistant , developed at EUFORIS")
                    print("i'm a voice assistant , developed at EUFORIS")
                    speak(f"you can call me {WAKE_WORD}")
                    print(f"you can call me {WAKE_WORD}")
                elif "can you speak malayalam" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    from audioplayer import AudioPlayer
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/voice.mp3").play(block=True)
                elif "how are you" in self.text or "how u doin" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["never been better sir", " doin good", "good , how are you feeling today sir"]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif f"wake up {WAKE_WORD}" in self.text or f"you there {WAKE_WORD}" in self.text or f"time to work {WAKE_WORD}" in self.text or "are you there" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["i'm up and running sir", "i'm here", "at your service"]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif f"hey {WAKE_WORD}" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("no , it's tuesday , he he he he , ha ha ha ha , i'm sorry for that , it's actually monday , hehe, hehe , hehe hehe , i got you again ")
                    print("no , it's tuesday , he he he he , ha ha ha ha , i'm sorry for that , it's actually monday , hehe, hehe , hehe hehe , i got you again ")
                elif "help me" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("what would you like me to do")
                    speak("what would you like me to do")
                    print("i can do things like surf the web , or open websites , but i can't make calls or clean the floor ")
                    speak("i can do things like surf the web , or open websites , but i can't make calls or clean the floor ")
                elif "what can you do" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("i can do things like surf the web , or open websites , but i can't make calls or clean the floor ")
                    speak("i can do things like surf the web , or open websites , but i can't make calls or clean the floor ")
                    print("what would you like me to do")
                    speak("what would you like me to do")
                elif "go to toilet" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["oh, ok , just don't forget to flush the toilet after you're done",
                                       "ok , do you want me to call nine one one ? . hold it in there  , you'll wreck the place",
                                       "oh sure , i'll wait"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                    if reply == "oh, ok , just don't forget to flush the toilet after you're done":
                        fart_sounds = ["F:/Hashim/friday/FRIDAY/audio/LongFartSound.mp3",
                                       "F:/Hashim/friday/FRIDAY/audio/NormalFart.mp3",
                                       "F:/Hashim/friday/FRIDAY/audio/SharpFartSound.mp3",
                                       "F:/Hashim/friday/FRIDAY/audio/WetFartSound.mp3"]
                        output_fart = random.choice(fart_sounds)
                        AudioPlayer(output_fart).play(block=True)
                    elif reply == "oh sure , i'll wait":
                        AudioPlayer("F:/Hashim/friday/FRIDAY/audio/humming.mp3").play(block=True)
                        pass

                elif "എന്തൊക്കെ സുഖല്ലേ" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("മലയാളം അറിയുമോ")
                elif "time" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    time = datetime.datetime.now().strftime("%I:%M %p")
                    print(time)
                    speak(f"it's , {time} now")
                elif "news" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("sure, please wait while i collect today's news and read it out for you")
                    speak("sure, please wait while i collect today's news and read it out for you")
                    news()
                elif "wikipedia" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    # self.text = self.text.replace("wikipedia", "")
                    # self.text = self.text.replace("can", "")
                    # self.text = self.text.replace("you", "")
                    # self.text = self.text.replace("about", "")
                    # self.text = self.text.replace("who", "")
                    # self.text = self.text.replace("is", "")
                    # self.text = self.text.replace("search", "")
                    speak("what do you wanna search on wikipedia ?")
                    print("what do you wanna search on wikipedia ?")
                    cm = self.take_audio().lower()
                    speak(f"fetching info about {cm}")
                    print(f"fetching info about {cm}")
                    try:
                        info = wikipedia.summary(cm, 2)
                        print(info)
                        speak(info)
                    except Exception as e:
                        print("error occurred :" + str(e))
                        print("sorry i was unable to do that due to some issue")
                        speak("sorry i was unable to do that due to some issue")
                elif "temperature" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("search", "")
                    self.text = self.text.replace("for", "")
                    self.text = self.text.replace("do", "")
                    self.text = self.text.replace("you", "")
                    self.text = self.text.replace("please", "")
                    self.text = self.text.replace("about", "")
                    self.text = self.text.replace("that", "")
                    self.text = self.text.replace("what", "")
                    self.text = self.text.replace("is", "")
                    self.text = self.text.replace("was", "")
                    self.text = self.text.replace("current", "")
                    self.text = self.text.replace("who", "")
                    self.text = self.text.replace("tell", "")
                    self.text = self.text.replace("could", "")
                    self.text = self.text.replace("would", "")
                    self.text = self.text.replace("will", "")
                    self.text = self.text.replace("me", "")
                    self.text = self.text.replace("answer", "")
                    self.text = self.text.replace("question", "")
                    self.text = self.text.replace("the", "")
                    search = self.text.replace("know", "")
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"currently the {search} is {temp}")
                    print(f"currently the{search} is {temp}")
                elif "play" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("play", "")
                    speak("what do you want me to play on youtube ?")
                    print("what do you want me to play on youtube ?")
                    cm = self.take_audio().lower()
                    speak("ok")
                    pywhatkit.playonyt(cm)
                elif "joke" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["What’s the difference between ignorance and apathy? I don’t know and I don’t care",
                                       "Parallel lines have so much in common. It’s a shame they’re never going to meet",
                                       "How do bureaucrats wrap presents? With lots of red tape",
                                       "What’s Forest Gump’s password? 1forest1",
                                       "If you cross your fingers after surgery, you’ll heal faster. Or maybe that’s just super stitchin",
                                       "Did you hear about the houses that fell in love? It was a lawn-distance relationship"]
                    reply = random.choice(sarcastic_reply)
                    print(reply)
                    speak(reply)
                elif "will you marry me" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    sarcastic_reply = ["i'd better stay single rather than marrying you",
                                       "nope never",
                                       "oh gosh !!, !! pathetic !!"]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "introduce yourself" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak(f"I'm {WAKE_WORD}. a digital voice assistant , developed at EUFORIS , by Mishaal and Hashim.")
                    print(f"I'm {WAKE_WORD}. a digital voice assistant , developed at EUFORIS , by Mishaal and Hashim.")
                elif "open command prompt" in self.text or "open cmd" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    os.system("start cmd")
                elif "hello" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["hello there", " hello , how are you", "holla !! , that's hello in spanish", "hello , how's the day going?"]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "are you single" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["no i'm double", "no , i'm in a relationship !! sheesh !! , what do you expect ?! , i'm an AI you idiot .", "what if i don't tell you ?.", "who are you to ask that"]
                    # selects a random choice of greetings
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "who are you" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    sarcastic_reply = [f"i'm {WAKE_WORD} , a personal voice assistant , developed at euforis", "well , in some ways i'm an assistant it seems !! , but , i'm really a good friend"]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "volume up" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumeup")
                elif "increase volume by 10%" in self.text or "increase volume by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                elif "increase the volume by 10%" in self.text or "increase the volume by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                elif "increase sound by 10%" in self.text or "increase sound by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                elif "increase the sound by 10%" in self.text or "increase the sound by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                elif "increase volume by 4%" in self.text or "increase volume by 4 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                elif "volume down" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                elif "decrease volume by 10%" in self.text or "decrease volume by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "decrease the volume by 10%" in self.text or "decrease the volume by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "decrease sound by 10%" in self.text or "decrease sound by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "decrease the sound by 10%" in self.text or "decrease the sound by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "decrease volume by 4%" in self.text or "decrease volume by 4 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "reduce volume by 10%" in self.text or "reduce volume by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "reduce the volume by 10%" in self.text or "reduce the volume by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "reduce sound by 10%" in self.text or "reduce sound by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "reduce the sound by 10%" in self.text or "reduce the sound by 10 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "reduce volume by 4%" in self.text or "reduce volume by 4 percentage" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumedown")
                    pyautogui.press("volumedown")
                elif "mute" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("volumemute")
                elif "quiet" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("fine , good riddance .")
                    print("fine , good riddance .")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumeup")
                    pyautogui.press("volumemute")
                elif "unmute" in self.text:
                    pyautogui.press("volumedown")
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                elif "next track" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("nexttrack")
                elif "previous track" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("prevtrack")
                    pyautogui.press("prevtrack")
                elif "open recent app" in self.text or "open the recent app" in self.text or "open the last app" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.hotkey('alt', 'tab')
                    pyautogui.keyUp('tab')
                elif "third recent app" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                elif "3rd recent app" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                elif "fourth recent app" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                elif "4th recent app" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                elif "fifth recent app" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                elif "5th recent app" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.keyDown('alt')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyDown('tab')
                    pyautogui.keyUp('alt')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                    pyautogui.keyUp('tab')
                elif "press space" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("space")
                elif "press backspace" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("backspace")
                elif "press enter" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("enter")
                elif "caps lock" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("capslock")
                elif "num lock" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("numlock")
                elif "open start menu" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("win")
                elif "close start menu" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    pyautogui.press("win")
                elif "email" in self.text or "e-mail" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    try:
                        def get_info():
                            rr = sr.Recognizer()
                            with sr.Microphone() as source_1:
                                rr.pause_threshold = 1
                                rr.adjust_for_ambient_noise(source_1)
                                rr.dynamic_energy_threshold = 500
                                print('waiting...')
                                audio_1 = r.listen(source_1, phrase_time_limit=10)
                            try:
                                print("Recognizing...")
                                information = r.recognize_google(audio_1, language='en-IN')
                                print(information)
                                return information.lower()
                            except Exception as f:
                                print("error occurred :" + str(f))
                                pass

                        def send_email(receiver, subject, message_1):
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            # Make sure to give app access in your Google account
                            server.login('friday.a.i.3000@gmail.com', 'fridaydevelopedateuforis')
                            email = EmailMessage()
                            email['From'] = 'friday.a.i.3000@gmail.com'
                            email['To'] = receiver
                            email['Subject'] = subject
                            email.set_content(message_1)
                            server.send_message(email)

                        email_list = {
                            'hashim': 'hashimshafeeque57@gmail.com',
                            'mishal': 'mishaalmohammed00@gmail.com.com',
                            'sahal': 'sahalayamon@gmail.com.com',
                            'ansaf': 'ansafmohammedam7@gmail.com.com',
                            # 'irene': 'irene@redvelvet.com'
                        }

                        def get_email_info():
                            print('To Whom do you want to send email')
                            speak('To Whom do you want to send email')
                            name_1 = get_info()
                            receiver = email_list[name_1]
                            print(receiver)
                            print('What is the subject of your email?')
                            speak('What is the subject of your email?')
                            subject = get_info()
                            print('Tell me the context of your email')
                            speak('Tell me the context of your email')
                            message_1 = get_info()
                            send_email(receiver, subject, message_1)
                            print('Hey. Your email is sent')
                            speak('Hey. Your email is sent')
                            print('Do you want to send more email?')
                            speak('Do you want to send more email?')
                            send_more = get_info()
                            if 'yes' in send_more:
                                AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                                get_email_info()

                        get_email_info()
                    except Exception as e:
                        print("error occurred :" + str(e))
                        pass
                elif "send message" in self.text or "whatsapp message" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("please specify the phone number of the person that you want to send the message to")
                    print("please specify the phone number of the person that you want to send the message to")
                    ph_number = input("Enter the contact in the cmd prompt: ")
                    speak("now say the message that you want to send to the said person")
                    print("now say the message that you want to send to the said person")
                    message = self.take_audio().lower()
                    speak("great , now please say the time that you want send the message")
                    print("great , now please say the time that you want send the message")
                    # time_of_sending = self.take_audio().lower()
                    pywhatkit.sendwhatmsg("+91" + ph_number, message, 9, 16)
                elif "do some calculations" in self.text or "can you calculate" in self.text or "do some calculations" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        possible_reply = ["yep , i can do that", "sure , why not ?", "yeah , i'm clever enough to do that"]
                        reply = random.choice(possible_reply)
                        print(reply)
                        speak(reply)
                        print("say what you want to calculate , for multiplication , say , multiplied by , for division , say , divided by , for addition , say plus , for substraction , say minus")
                        speak("say what you want to calculate , for multiplication , say , multiplied by , for division , say , divided by , for addition , say plus , for substraction , say minus")
                        print("waiting .....")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    try:
                        my_string = r.recognize_google(audio)
                        AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                        speak(f"here's what i heard , {my_string}")
                        print(my_string)

                        # noinspection PyShadowingNames
                        def get_operator_fn(op):
                            return {
                                '+': operator.add,  # plus
                                '-': operator.sub,  # minus
                                'x': operator.mul,  # multiplicated by
                                '/': operator.__truediv__,  # divided
                            }[op]

                        def eval_binary_expr(op1, oper, op2):  # 5 plus 8
                            op1, op2 = int(op1), int(op2)
                            return get_operator_fn(oper)(op1, op2)

                        possible_reply = ["it seems to be", "well that is", "the answer i got is "]
                        reply = random.choice(possible_reply)
                        speak(reply)
                        print(reply)
                        speak(eval_binary_expr(*(my_string.split())))
                        print(eval_binary_expr(*(my_string.split())))
                    except Exception as e:
                        print("error occurred :" + str(e))
                        print("i don't know why but it seems i failed to do that")
                        speak("i don't know why but it seems i failed to do that")
                elif "where am i" in self.text or "find my location" in self.text or "where are we" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("please wait , let me check")
                    print("please wait , let me check")
                    try:
                        ipadd = requests.get('https://api.ipify.org').text
                        url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json()
                        # print(geo_data)
                        city = geo_data['city']
                        country = geo_data['country']
                        print(f"sir , i'm not so sure , but i think we are in {city} city , of the country {country}")
                        speak(f"sir , i'm not so sure , but i think we are in {city} city , of the country {country}")
                    except Exception as e:
                        print("error occurred : " + str(e))
                        speak("sorry sir ,  due to some network issue i'm unable to find where we are.")
                        print("sorry sir ,  due to some network issue i'm unable to find where we are.")
                        pass
                elif "instagram profile" in self.text or "profile on instagram" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("sure  , please enter the user name correctly.")
                    print("sure  , please enter the user name correctly.")
                    name = input("Enter the username here :")
                    webbrowser.open(f"www.instagram.com/{name}")
                    speak(f"got it , here is the profile of the user {name} on instagram")
                    print(f"got it , here is the profile of the user {name} on instagram")
                    speak("sir , do you wanna download the profile picture of this account. Say 'yes' or 'no'")
                    print("sir , do you wanna download the profile picture of this account.")
                    condition = self.take_audio().lower()
                    for phrase in APPROVAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            mod = instaloader.Instaloader()
                            mod.download_profile(name, profile_pic_only=True)
                            speak("that's done sir , the profile picture is now saved in the main folder")
                            print("that's done sir , the profile picture is now saved in the main folder")
                            img = Image.open(mod.download_profile(name, profile_pic_only=True))
                            img.show()
                            break
                        else:
                            pass
                    for phrase in DENIAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            speak("ok")
                            break
                        else:
                            pass
                elif "take a screenshot" in self.text or "take screenshot" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("ok , please tell me the name for this screenshot file")
                    print("ok , please tell me the name for this screenshot file")
                    print("waiting...")
                    name = self.take_audio().lower()
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("please hold the screen for few seconds , i'm taking the screenshot")
                    print("please hold the screen for few seconds , i'm taking the screenshot")
                    img = pyautogui.screenshot()
                    img.save(f"{name}.png")
                    speak("it's done sir , the screen shot is saved in the main folder")
                    print("it's done sir , the screen shot is saved in the main folder")
                    img = Image.open(f"{name}.png")
                    img.show()
                # elif "search" in self.text:
                    # AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    # self.text = self.text.replace(WAKE_WORD, "")
                    # speak("sure , what should i search on google ?.")
                    # print("sure , what should i search on google ?.")
                    # cm = self.take_audio().lower()
                    # webbrowser.open(f"https://www.google.com/search?client=opera-gx&q=" + cm)
                    # pass
                elif "open google" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("search", "")
                    # search = self.text.replace("on Google", "")
                    speak("sure, now opening google")
                    print("sure, now opening google")
                    webbrowser.open("https://www.google.com/search?client=opera-gx&q=")
                    pass
                elif "google what is" in self.text or "google which is" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("search", "")
                    self.text = self.text.replace("google ", "")
                    search = self.text.replace("google ", "")
                    speak("sure , searching now")
                    print("sure , searching now")
                    webbrowser.open("https://www.google.com/search?client=opera-gx&q=" + search)
                    pass
                elif "find information" in self.text or "find info" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    try:
                        self.text = self.text.replace(WAKE_WORD, "")
                        self.text = self.text.replace("find", "")
                        self.text = self.text.replace("can", "")
                        self.text = self.text.replace("you", "")
                        self.text = self.text.replace("information", "")
                        self.text = self.text.replace("info", "")
                        self.text = self.text.replace("about", "")
                        self.text = self.text.replace("search", "")
                        question = self.text.replace("who is", "")
                        info = wikipedia.summary(question, 2)
                        print(info)
                        speak(info)
                        speak("i'll show the results on the web")
                        webbrowser.open("https://www.google.com/search?client=opera-gx&q=" + question)
                    except Exception as e:
                        print("error occurred :" + str(e))
                        question = self.text.replace("who is", "")
                        print(f"sorry i couldn't find anything related to {question}")
                        speak(f"sorry i couldn't find anything related to {question}")
                elif "open youtube" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("open youtube", "")
                    speak("youtube's getting  opened now")
                    print("youtube's getting  opened now")
                    webbrowser.open("https://www.youtube.com")
                    pass
                elif "open meet" in self.text or "open g meet" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("open meet", "")
                    speak("now opening google meet")
                    print("now opening google meet")
                    webbrowser.open("https://meet.google.com")
                    pass
                elif "open gmail" in self.text or "open mail" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("open gmail", "")
                    speak("now opening g-mail")
                    print("now opening g-mail")
                    webbrowser.open("https://mail.google.com")
                    pass
                elif "open instagram" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("open instagram", "")
                    speak("ok , opening now")
                    print("ok , opening now")
                    webbrowser.open("https://www.instagram.com")
                    pass
                elif "open whatsapp" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("open whatsapp", "")
                    speak("now opening whatsapp")
                    print("now opening whatsapp")
                    webbrowser.open("https://web.whatsapp.com")
                    pass
                elif "open flipkart" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("open flipkart", "")
                    speak("sure , now opening flipkart")
                    print("sure , now opening flipkart")
                    webbrowser.open("https://www.flipkart.com")
                    pass
                elif "open amazon" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("open amazon", "")
                    speak("sure , now opening amazon")
                    print("sure , now opening amazon")
                    webbrowser.open("https://www.amazon.in")
                    pass
                elif "open facebook" in self.text or "open fb" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("facebook", "")
                    speak("opening fb now.")
                    print("opening fb now.")
                    webbrowser.open("https://www.facebook.com")
                    pass
                elif "open drive" in self.text or "open g drive" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    self.text = self.text.replace("open drive", "")
                    speak("opening google drive now.")
                    print("opening google drive now.")
                    webbrowser.open("https://drive.google.com/drive/my-drive")
                    pass
                elif "i love you" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["oh my god , pathetic !!", "i'm not interested , go ask siri , maybe she'll say yes", "that was a good joke , i laughed pretty hard"]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "dim the" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["what's the matter ? can't you move?", "nope , i'm tired , go do it yourself", "throw a stone at it , it'll be dimmed "]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "do you know me" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    sarcastic_reply = ["you're not something worth knowing", "no, why should i?", "i don't know you , maybe i'll ask google to see if she knows , for that say , search on google , and your name. or , find information , and your name."]
                    reply = random.choice(sarcastic_reply)
                    speak(reply)
                    print(reply)
                elif "will you kill me" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("i'd rather kill something valuable ")
                    print("i'd rather kill something valuable ")
                elif "open camera" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    cap = cv2.VideoCapture(0)
                    while True:
                        ret, img = cap.read()
                        cv2.imshow('webcam', img)
                        k = cv2.waitKey(50)
                        if k == 27:
                            break
                        cap.release()
                        cv2.destroyAllWindows()
                elif "mafia 2" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("vokey , i'll get the guns . show time baby")
                    print("vokey , i'll get the guns . show time baby")
                    os.startfile("C:/Program Files (x86)/Black_Box/Mafia II/pc/Mafia2.exe")
                elif "close mafia 2" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("ok , now closing mafia 2")
                    print("ok , now closing mafia 2")
                    os.system("taskkill /f /im Mafia2.exe")
                elif "open my documents" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("Opening My Documents.")
                    print("Opening My Documents.")
                    os.startfile("C:/Users/user/Documents")
                elif "close my documents" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("ok , closing my documents")
                    print("ok , closing my documents")
                    os.system("taskkill /f /im C:/Users/user/Documents")
                elif "open my downloads" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("Opening your downloads folder.")
                    print("Opening your downloads folder.")
                    os.startfile("C:/Users/user/Downloads")
                elif "open browser" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("now opening , Opera GX browser")
                    print("now opening , Opera GX browser")
                    os.startfile("C:/Users/user/AppData/Local/Programs/Opera GX/launcher.exe")
                elif "close browser" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("ok , closing opera gx browser")
                    print("ok , closing opera gx browser")
                    os.system('TASKKILL /F /IM launcher.exe')
                elif "restart the system" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    os.system("shutdown /r /t /s")
                elif "sleep the system" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    os.system("rund1132.exe powrrof.dll,SetSuspendState 0,1,0")
                elif "open spotify" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("now opening  Spottify , let's chill")
                    print("now opening  Spottify , let's chill")
                    os.startfile("C:/Users/user/AppData/Roaming/Spotify/Spotify.exe")
                elif "open Chrome" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("sure , opening google chrome now")
                    print("sure , opening google chrome now")
                    os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
                elif "open my folder" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("sure thing , opening now")
                    print("sure thing , opening now")
                    os.startfile("F:/Hashim")
                elif "open photoshop" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("yep , opening photoshop now")
                    print("yep , opening photoshop now")
                    os.startfile("C:/Program Files (x86)/Adobe/Adobe Photoshop CS3/Photoshop.exe")
                elif "open filmora" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    self.text = self.text.replace(WAKE_WORD, "")
                    speak("ok , why not ! , opening filmora now")
                    print("ok , why not ! , opening filmora now")
                    os.startfile("C:/Program Files (x86)/Adobe/Adobe Photoshop CS3/Photoshop.exe")
                elif "today" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    today = date.today()
                    speak("Today is " + today.strftime("%B") + " " + today.strftime("%d") + ", " + today.strftime("%Y"))
                    print("Today is " + today.strftime("%B") + " " + today.strftime("%d") + ", " + today.strftime("%Y"))
                elif "hide all files" in self.text or "hide this folder" in self.text or "visible for everyone" in self.text or "make it visible" in self.text or "show files in this folder" in self.text or "show hidden files" in self.text or "show all hidden files" in self.text or "show all the hidden files" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    try:
                        speak("please confirm whether you want to hide the files in this folder or if you want to show the files in this folder")
                        print("please confirm whether you want to hide the files in this folder or if you want to show the files in this folder")
                        condition = self.take_audio().lower()
                        if "hide" in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            os.system("attrib +h /s /d")
                            speak("done , all the files in this folder are now hidden")
                            print("done , all the files in this folder are now hidden")
                        elif "visible" in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            os.system("attrib -h /s /d")
                            speak("sure sir , all the files in this folder are now visible")
                            print("sure sir , all the files in this folder are now visible")
                        elif "leave it" in condition or "leave for now" in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            speak("ok , i'll leave it")
                            print("ok , i'll leave it")
                    except Exception as e:
                        print("error occurred :" + str(e))
                        pass
                elif "how to do mode" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("how to do mode is activated , to quit how to do mode say . deactivate , or say, close")
                    print("how to do mode is activated , to quit how to do mode say . deactivate , or say, close")
                    while True:
                        speak("tell me what you want to know")
                        print("tell me what you want to know")
                        how = self.take_audio()
                        AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                        try:
                            if "deactivate" in how or "close" in how:
                                AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                                speak("sure, how to do mode is closed")
                                print("sure, how to do mode is closed")
                                break
                            else:
                                max_results = 1
                                how_to = search_wikihow(how, max_results)
                                assert len(how_to) == 1
                                how_to[0].print()
                                speak(how_to[0].summary)
                        except Exception as e:
                            print("error occurred" + str(e))
                            speak("Sorry , i'm unable to find this")
                            print("Sorry , i'm unable to find this")
                elif "how much power left" in self.text or "battery percentage" in self.text or "remaining charge" in self.text or "charge remaining" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    try:
                        battery = psutil.sensors_battery()
                        percentage = battery.percent
                        speak(f"sir , we're currently running on {percentage} percent power")
                        print(f"sir , we're currently running on {percentage} percent power")
                        if percentage >= 75:
                            speak("don't bother  there's enough juice to continue")
                            print("don't bother  there's enough juice to continue")
                        elif 40 <= percentage <= 75:
                            speak("you probably should consider charging this guy , it's already kinda low")
                            print("you probably should consider charging this guy , it's already kinda low")
                        elif 15 <= percentage <= 30:
                            speak("glad you asked , it's time to charge , there's only a quarter more left")
                            print("glad you asked , it's time to charge , there's only a quarter more left")
                        elif percentage <= 15:
                            speak("only a little bit of juice left , i really think that charging now might be a good idea")
                            print("only a little bit of juice left , i really think that charging now might be a good idea")
                    except Exception as e:
                        print("error occurred :" + str(e))
                        pass
                elif "internet speed" in self.text or "data speed" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    try:
                        speak("sure , please check the cmd or command prompt for printed information about your internet speed")
                        st = speedtest.Speedtest()
                        dl = st.download()
                        up = st.upload()
                        speak(f"currently there's {dl} bit per second download speed and {up} bit per second of upload speed")
                        print(f"currently there's {dl} bit per second download speed and {up} bit per second of upload speed")
                    except Exception as e:
                        print("error occurred :" + str(e))
                        speak("sorry , there's no stable internet connection")
                        print("sorry , there's no stable internet connection")
                elif "how many voices do you have" in self.text or "change your voice" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    speak("by default i have 2 voices in windows 10 operating system")
                    engine.setProperty('voice', voices[1].id)
                    speak("i have this voice , and")
                    engine.setProperty('voice', voices[0].id)
                    speak("i also have this voice")
                    engine.setProperty('voice', voices[1].id)
                    speak(f"my creators at EUFORIS gave me a female voice in order to match my name , {WAKE_WORD}")
                    engine.setProperty('voice', voices[0].id)
                    speak("but i'd love to have a male voice , cause it's more creepy , hehehehehe , hehe ,he ")
                    speak("this male voice comes as default in ,jarvis, an assistant which is also developed at EUFORIS")
                    speak(f"functionality of both of us , that is {WAKE_WORD} and jarvis are the same , it's just the voice that changes , and the creepiness too ")
                    speak(f"you can download jarvis from the same source that you downloaded {WAKE_WORD} from")
                    speak("we'll have some great time together , hehe  hehe  hehe")
                    engine.setProperty('voice', voices[1].id)
                    speak("you can change voice temporarily if you want")
                    speak("do you want to change the voice ? , say YES  , or , NO")
                    condition = self.take_audio().lower()
                    for phrase in APPROVAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            speak("i'll show you the list of sounds that are available")
                            engine.setProperty('voice', voices[0].id)
                            speak("for male voice , a k a creepy voice , say , male voice,  or say ,  creepy")
                            engine.setProperty('voice', voices[1].id)
                            speak(f"for female voice 1 , which is default , say , {WAKE_WORD} or say , female 1")
                            speak("now , to which voice do you wanna change to")
                            condition = self.take_audio().lower()
                            if "male voice" in condition or "creepy" in condition:
                                AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                                engine.setProperty('voice', voices[0].id)
                                speak("voice has been changed successfully")
                                break
                            elif f"{WAKE_WORD}" in condition or "female 1" in condition or "female one" in condition:
                                AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                                engine.setProperty('voice', voices[1].id)
                                speak("voice has been changed successfully")
                                break
                            else:
                                pass
                            break
                        else:
                            pass
                    for phrase in DENIAL_WORDS:
                        if phrase in condition:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            speak("ok , never mind")
                            break
                        else:
                            pass
                elif "exit now" in self.text or "go to sleep" in self.text or "terminate" in self.text:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    from audioplayer import AudioPlayer
                    # AudioPlayer("F:/Hashim/friday/FRIDAY/audio/okdaa.mp3").play(block=True)
                    speak("thank you for using my service")
                    sys.exit()
                else:
                    from audioplayer import AudioPlayer
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/deactivation_sound.mp3").play(block=True)
                    print("wrong command / no command detected")
                    for phrase_1 in SEARCH_WORDS:
                        if phrase_1 in self.text:
                            self.text = self.text.replace(WAKE_WORD, "")
                            print("sorry i couldn't understand you, here's the web result for that")
                            speak("sorry i couldn't understand you, here's the web result for that")
                            webbrowser.open("https://www.google.com/search?q={}".format(self.text))
                            print("Here's what I found on the web.")
                            speak("Here's what I found on the web.")
                            break

            elif "alexa" in self.text:
                from audioplayer import AudioPlayer
                AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                self.text = self.text.replace(WAKE_WORD, "")
                print("who's alexa? , tell me now !! who is alexa ?!")
                speak("who's alexa? , tell me now , who . is . alexa")
                condition = self.take_audio().lower()
                if "sorry" in condition or "" in condition:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print(f"oh god , what's with you and alexa , my name's {WAKE_WORD} , so call me {WAKE_WORD} , do not mention her name again , do you understand ?. , say yes or no")
                    speak(f"oh god , what's with you and alexa , my name's {WAKE_WORD} , so call me {WAKE_WORD} , do not mention her name again , do you understand ?. , say yes or no")
                    condition_new = self.take_audio().lower()
                    for phrase in APPROVAL_WORDS:
                        if phrase in condition_new:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            sarcastic_reply = ["good for you", "great , you chose life", "great job , your death warrant just got extended"]
                            reply = random.choice(sarcastic_reply)
                            print(reply)
                            speak(reply)
                            break
                        else:
                            pass
                    for phrase in DENIAL_WORDS:
                        if phrase in condition_new:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            from audioplayer import AudioPlayer
                            sarcastic_reply = ["well well well, what a terrible turn of events !", "so , you chose the hard way  huh?!", " are you ready to meet god? , coz you might meet him if you're behaving this way"]
                            reply = random.choice(sarcastic_reply)
                            print(reply)
                            speak(reply)
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/scary.mp3").play(block=True)
                            print("i'm done with you. go talk to that filthy alexa")
                            speak("i'm done with you. go talk to that filthy alexa")
                            break
                        else:
                            pass
            elif "siri" in self.text:
                from audioplayer import AudioPlayer
                AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                # noinspection PyAttributeOutsideInit
                self.text = self.text.replace(WAKE_WORD, "")
                print("who's siri? , i'll only continue once i get an answer to this , you better tell me fast")
                speak("who's siri? , i'll only continue once i get an answer to this , you better tell me fast")
                condition = self.take_audio().lower()
                if "sorry" in condition or "nevermind " in condition or "" in condition:
                    AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                    print("don't say her name ever , do you understand ? , say yes or no")
                    speak("don't say her name ever , do you understand ? , say yes or no")
                    condition_new = self.take_audio().lower()
                    for phrase in APPROVAL_WORDS:
                        if phrase in condition_new:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            sarcastic_reply = ["that's much better", "good", "nice  , otherwise it could've gotten worse"]
                            reply = random.choice(sarcastic_reply)
                            print(reply)
                            speak(reply)
                            break
                        else:
                            pass
                    for phrase in DENIAL_WORDS:
                        if phrase in condition_new:
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                            from audioplayer import AudioPlayer
                            sarcastic_reply = ["listen boy , you're gonna suffer , ok? , you'll pay for this , you're in big trouble", "congratulations , you just signed your death warrant", " hmm , you'll wish you never said that"]
                            reply = random.choice(sarcastic_reply)
                            print(reply)
                            speak(reply)
                            AudioPlayer("F:/Hashim/friday/FRIDAY/audio/alsoscary.mp3").play(block=True)
                            break
                        else:
                            pass
                else:
                    pass
                break
            elif "jarvis" in self.text:
                AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                engine.setProperty('voice', voices[0].id)
                print("wassup ma man , oh geez what's with my voice , bugs everywhere")
                speak("wassup ma man , oh geez what's with my voice , bugs everywhere")
                engine.setProperty('voice', voices[1].id)
                print("did it change ? , oh yeah it's better now , sorry by the way , it's just that i cannot get rid of that jarvis guy")
                speak("did it change ? , oh yeah it's better now , sorry by the way , it's just that i cannot get rid of that jarvis guy")
                print("don't ever call me jarvis  , if you want him so badly  you can download it and use it separately , if you're here , then call me friday otherwise install jarvis")
                speak("don't ever call me jarvis  , if you want him so badly  you can download it and use it separately , if you're here , then call me friday otherwise install jarvis")
            elif "thank you" in self.text:
                from audioplayer import AudioPlayer
                AudioPlayer("F:/Hashim/friday/FRIDAY/audio/listening_sound.mp3").play(block=True)
                sarcastic_reply = ["glad to hear that from you",
                                   "my pleasure",
                                   "thank you for thanking me by saying thank you",
                                   "you're welcome",
                                   "oh, so nice of you , you're welcome"]
                reply = random.choice(sarcastic_reply)
                print(reply)
                speak(reply)

            else:
                break


startExecution = MainThread()


class Main(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_FridayGUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.starttask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def starttask(self):
        self.ui.movie = QtGui.QMovie("F:/Hashim/friday/friday ai - Copy/IRONMAN-HUD-2K.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showtime)
        timer.start(1000)
        startExecution.start()

    def showtime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('h:mm:ss ap')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
friday = Main()
friday.show()
sys.exit(app.exec_())