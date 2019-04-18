# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:15:23 2019

@author: Abir
"""
from gtts import gTTS
import speech_recognition as sr
from tempfile import TemporaryFile
from pygame import mixer
from weather import Weather
import pyautogui
import re
from random import randint
import webbrowser
import wolframalpha
from time import sleep

def talkToMe(audio):
     print(audio)
     tts1 = gTTS(audio,'en')
     mixer.init()
     sf1 = TemporaryFile()
     tts1.write_to_fp(sf1)
     sf1.seek(0)
     mixer.music.load(sf1)
     mixer.music.play()
     
def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        sleep(5)
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def assistant(command):
    if "who are you" ==command or  "what are you" == command:
        response=['I am whatever you want me to be', 'I can be your friend or your enemy',
                      'What do you think I am?','I am an pseudo A.I created by a boy who has nowhere to go' ]
        a=randint(0, 3)
        print(response[a])
        talkToMe(response[a])
    elif "who made you" ==command or "who created you" == command or "who built you" == command:
        response1=['I was created by a man who refused to give up', 'I was inspired from a strong and amazing woman',
                       'Like all creation in the cosmos, I was built up from tiny particles yet to be discovered by man']
        b=randint(0, 2)
        print(response1[b])
        talkToMe(response1[b])
    elif "exit"==command or "quit"==command:
        track==False
    elif "search for" in command:
        reg_ex = re.search('search for (.*)', command)
        url="https://www.google.com/search?q="
        if reg_ex:
            search=reg_ex.group(1)
            url = url + search
        webbrowser.open(url)
        print("done")
    elif "open youtube" or "play" in command:
        url2="https://www.youtube.com/results?search_query="
        reg_ex = re.search('open youtube (.*)', command)
        if reg_ex:
            search2=reg_ex.group(1)
            url2 = url2 + search2
        webbrowser.open(url2)
        sleep(2)
        pyautogui.click(585, 214)
        print("done")
    else:
        app_id="WYPU95-T5W9K54VQX"
        client=wolframalpha.Client(app_id)
        res=client.query(command)
        answer=next(res.results).text
        talkToMe(answer)
        
talkToMe('I am BETH, here to help')
track=True
while track:
    assistant(myCommand())
        
        