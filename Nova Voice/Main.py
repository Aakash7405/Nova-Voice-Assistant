import os
import subprocess
import threading
import speech_recognition as sr
import datetime
import openai
import pyttsx3
import wikipedia
import webbrowser
import pyjokes
import ecapture as e
import wolframalpha
import tkinter as tk
from tkinter import *
import time
import pymysql
import messagebox
from PIL import Image, ImageTk
import pyautogui

openai.api_key = "your_openAi_apiKey"

# chat module

def chat(query):
    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {
          "role": "user",
          "content": query
        }
      ],
      temperature=1,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    input = response.choices[0].message["content"]
    th1 = threading.Thread(target=speak, args=(input,))
    th2 = threading.Thread(target=send, args=(input,))
    th1.start()
    th2.start()



# convert text to voice

def speak(audio):

    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate',200)
    engine.setProperty('pitch',0.9);
    engine.say(audio)
    engine.runAndWait()


# greet the user

def Hello():

        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            speak("Good Morning Sir !")

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon Sir !")

        else:
            speak("Good Evening Sir !")

        speak("I am your Nova assistant . How may I help you")

# tells the time

def tellTime():

    time = str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("The time is " + hour + "Hours and" + min + "Minutes")
def tellDay():
    time = datetime.datetime.now()
    speak('Today is'+time.strftime('%A'))
def Take_text():

    val = input("please enter your query ")
    return val

def connectDatabase(command):
    try:
        con = pymysql.connect(host="localhost", user="root", passwd="your_pass", port=3306)
        mycursor = con.cursor()

    except:
        messagebox.showerror('Error', 'Database Connectivity Issue , Please Try Again')
        return
    try:
        query = 'create database CommandData'
        mycursor.execute(query)
        query = 'use CommandData'
        mycursor.execute(query)
        query = 'create table command(command_id int auto_increment primary key not null, commands varchar(100))'
        mycursor.execute(query)
    except:
        mycursor.execute('use CommandData')

    if command != "":
        query = 'insert into command(commands) values(%s)'
        mycursor.execute(query, (command))
        con.commit()
        con.close()



def Take_query():


    while (True):

        query = takeCommand().lower()
        connectDatabase(query)
        l=len(query)
        if "open google" in query:
            speak("Opening Google ")
            webbrowser.open("https://www.google.com")
            continue
        if "open youtube" in query:
            speak("Opening youtube ")
            query = query.replace("search","")
            query = query.replace("and", "")
            web = "https://www.youtube.com/results?search_query=" + query
            webbrowser.open(web)
            continue
        if "open vs code" in query:
            speak("Opening vs code ")
            vs=r"C:\Users\chhav\Desktop\Visual Studio Code.lnk"
            os.startfile(vs)

        if 'screenshot' in query:
            im1 = pyautogui.screenshot()
            im1.save(r"D:\Echo saviour Project\screenshot.png")
        if "open notepad" in query:
            speak("Opening notepad ")
            n=r"C:\Windows\notepad.exe"
            os.startfile(n)
            exit()

        if 'open gmail' in query:
            webbrowser.open_new_tab("mail.google.com")
            speak("Google Mail open now")
            time.sleep(5)

        if 'news' in query:
            webbrowser.open_new_tab("https://timesofindia.indiatimes.com/city/delhi")
            speak('Here are some headlines from the Times of India, Happy reading')
            time.sleep(6)

        if 'cricket' in query:
            webbrowser.open_new_tab("cricbuzz.com")
            speak('This is live news from cricbuzz')
            time.sleep(6)

        elif "which day" in query:
            tellDay()
            continue

        elif "tell me the time" in query:
            tellTime()
            continue

        elif 'joke' in query:
            input = pyjokes.get_joke()
            th1 = threading.Thread(target=speak, args=(input,))
            th2 = threading.Thread(target=send, args=(input,))
            th1.start()
            th2.start()

        elif "volume up" in query:
            from Keyboard import volumeup

            speak("Turning volume up,sir")
            volumeup()

        elif "volume down" in query:
            from Keyboard import volumedown

            speak("Turning volume down, sir")
            volumedown()
        elif  "take a photo" in query or  "take a selfie"in query:
            e.capture(0,"frame","img.jpg")
            exit()

        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
            continue

        elif "from wikipedia" in query:
            speak("Checking the wikipedia")
            query = query.replace("wikipedia", "")

            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")

            th1 = threading.Thread(target=speak, args=(result,))
            th2 = threading.Thread(target=send, args=(result,))
            th1.start()
            th2.start()

        elif "calculate" in query:

            app_id = "your_wolframalpha_apikey"
            client = wolframalpha.Client(app_id)
            index = query.lower().split().index('calculate')
            query = query.split()[index + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)

            ans = "The answer is "+answer
            th1 = threading.Thread(target=speak, args=(ans,))
            th2 = threading.Thread(target=send, args=(ans,))
            th1.start()
            th2.start()


        elif 'play music' in query or "play song" in query or "open music" in query:
            speak("Here you go with music")
            # music_dir = "G:\\Song"
            music_dir = "D:\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

            

        elif "google" in query:
            if 'google' in query:
                l=len(query)
                src=query[7:l]
                print(src)
                link="https://www.google.com/search?q="+src
                webbrowser.open(link)


        elif 'shutdown' in query:
            speak(' Do you really want to shutdown your computer ')
            shutdown = takeCommand().lower()
            if 'yes' in shutdown:
             #speak("Hold On a Sec ! Your system is on its way to shut down")
             os.system("shutdown /s /t 1")
            else:
             break


        elif "tell me your name" in query:
            speak("My name is Nova Voice assistant")

        elif "pause" in query:
            pyautogui.press("k")
        elif "play" in query:
            pyautogui.press("k")
        elif "mute" in query:
            pyautogui.press("m")
        elif "unmute" in query:
            pyautogui.press("m")





        elif "who made you" in query or "who created you" in query:
            print("I have been created by Aakash")
            speak("I have been created by Aakash")


        elif "exit" in query or "bye" in query:
            speak("thank you")
            exit()


        elif 'nova' in query:
         chat(query)



# takes the command from user
def takeCommand():
    r = sr.Recognizer()


    with sr.Microphone() as source:
     print('Listening')


     r.pause_threshold = 0.7
     audio = r.listen(source)

    try:
            print("Recognizing")


            Query = r.recognize_google(audio, language='en-in')
            # print("the command is printed=", Query)

    except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

    return Query


#GUI module

def send(query):

        win = Tk()
        win.title("Nova Voice Assistant")
        BG_GRAY = "#6495ED"
        BG_COLOR = "WHITE"
        TEXT_COLOR = "BLACK"
        FONT = "Helvetica 14"
        FONT_BOLD = "Helvetica 13 bold"

        lable1 = Label(win, bg="WHITE", fg=TEXT_COLOR, text="WELCOME", font=FONT_BOLD, width=20, height=1).grid(row=0)
        txt = Text(win, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)

        txt.grid(row=1, column=0)
        send1 = query
        txt.insert(END,"\n"+send1)
        win.mainloop()

class landingPage:
    def __init__(self,root):
        self.root = root
        self.root.geometry('900x700')
        self.root.title('Nova Voice Assistant')
        self.root.resizable(False,False)
        self.root.iconbitmap("D:\python\icon.ico")
        frame1 = Frame(root, bg='#161925', width=700, height=950)
        frame1.pack()
        photo1 = PhotoImage(file=r"icon8.png")
        photoimage = photo1.subsample(3, 3)

        b1 = Button(frame1,
                    text="Voice",
                    image=photoimage,
                    width=150,
                    height=60,
                    borderwidth=2,
                    command=lambda: [Hello(), Take_query()]

                    )
        b1.pack(side=BOTTOM, expand=False, fill=None, anchor='center', pady=15)
        img = ImageTk.PhotoImage(Image.open(r"3.gif"))
        label = Label(frame1, image=img, anchor='center')
        label.pack()
        root.mainloop()

def start():
    root=Tk()
    landingPage(root)
    root.mainloop()

if __name__ == '__main__':

   start()






