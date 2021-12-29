import pyttsx3
import speech_recognition as sr
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import time
import wikipedia
from pygame import mixer
import pandas as pd
import numpy as np
import requests
import geocoder
import re
import requests
import subprocess
import urllib.parse
import urllib.request
from bs4 import BeautifulSoup
import webbrowser
import psutil
from datetime import date
import pyjokes

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
g = geocoder.ip('me')


def findDate():
    today = date.today()
    speak(today)


def playMusic(music_name):
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen(
        "https://www.youtube.com/results?" + query_string)

    search_results = re.findall(
        r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" +
                        "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for concatMusic1 in yt_title:
        pass

    print(concatMusic1['content'])

    subprocess.Popen(
        "start /b " + "bootstrapper\\mpv.exe " + clip2 +
        " --no-video --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",
        shell=True)


def playMusicVideo(music_name):
    query_string = urllib.parse.urlencode({"search_query": music_name})
    formatUrl = urllib.request.urlopen(
        "https://www.youtube.com/results?" + query_string)

    search_results = re.findall(
        r"watch\?v=(\S{11})", formatUrl.read().decode())
    clip = requests.get("https://www.youtube.com/watch?v=" +
                        "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])

    inspect = BeautifulSoup(clip.content, "html.parser")
    yt_title = inspect.find_all("meta", property="og:title")

    for concatMusic1 in yt_title:
        pass

    print(concatMusic1['content'])

    subprocess.Popen(
        "start /b " + "bootstrapper\\mpv.exe " + clip2 +
        " --loop=inf --input-ipc-server=\\\\.\\pipe\\mpv-pipe > output.txt",
        shell=True)


def weather():
    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(g.latlng[0]) + "&lon=" + str(g.latlng[1])

    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        speak(str(data_json['coord']['lat']) + 'latitude' +
              str(data_json['coord']['lon']) + 'longitude')
        speak('Current location is ' +
              data_json['name'] + data_json['sys']['country'] + 'dia')
        speak('weather type ' + weather_desc['main'])
        speak('Wind speed is ' + str(wind['speed']) + ' metre per second')
        speak('Temperature: ' + str(main['temp']) + 'degree celcius')
        speak('Humidity is ' + str(main['humidity']))


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# def takecommand():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("listening.....")
#         r.pause_threshold = 1
#         audio = r.listen(source,timeout=1,phrase_time_limit=5)

#     try:
#         print("Recognizing.....")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"user said: {query}")

#     except Exception as e:
#         # speak("Say that again please...")
#         return "none"
#     return query


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 494
        r.adjust_for_ambient_noise(source, duration=1.5)
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio, language='en-in')
        print(f'User said: {query}\n')

    except Exception as e:
        # print(e)

        print('Say that again please...')
        return 'None'
    return query


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at" + usage + '%')

    battery = psutil.sensors_battery()
    speak("battery is at" + str(battery.percent) + '%')
    # speak(battery.percent)


def wish():
    hour = int(datetime.datetime.now().hour)
    print("Push commits to origin!!!")
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour > 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")
    weather()
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f'the time is {strTime}')
    cpu()
    memUsed = psutil.virtual_memory().percent
    speak("ram usage is" + str(memUsed) + '%')
    speak("All systems online")
    speak("i am jarvis SIR. please tell me how can i help you")


if __name__ == "__main__":
    wish()
    # os.popen(r"python3.9 C:\Users\atifu\Documents\GitHub\Jarvis\gestureControl.py")
    while True:

        query = takeCommand().lower()

        # logic buiding for tasks
        if 'joke' in query:
            speak(pyjokes.get_joke())

        if "today's date" in query:
            findDate()

        if 'cpu' in query:
            cpu()

        if 'open amazon' in query:
            webbrowser.open_new_tab('https://amazon.com')

        if 'search' in query:
            speak('What do you want to search for?')
            search = takeCommand()
            url = 'https://google.com/search?q=' + search
            webbrowser.open_new_tab(url)
            speak('Here is What I found for' + search)

        if 'your name' in query:
            speak('My name is JARVIS')

        if 'my location' in query:
            speak('What is the location?')
            location = takeCommand()
            url = 'https://google.nl/maps/place/' + location + '/&amp;'
            webbrowser.open_new_tab(url)
            speak('Here is the location ' + location)

        if 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[0].id)
            else:
                engine.setProperty('voice', voices[1].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        if 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        if 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        if "play music" in query:
            speak("Which song would you listen? ")
            choice = takeCommand()
            playMusic(choice)

        if "play music video" in query:
            speak("Which song would you listen? ")
            choice = takeCommand()
            playMusicVideo(choice)

        if "stop music" in query:
            os.system("taskkill /f /im mpv.exe")
            speak("terminated mpv.exe")

        # if "brave" in query:
        #     path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
        #     os.startfile(path)

        if "close brave" in query:
            speak("closed brave")
            os.system("taskkill /f /im brave.exe")

        if "discord" in query:
            path = "C:\\Users\\atifu\AppData\\Local\\Discord\\app-1.0.9002\\Discord.exe"
            speak("opening discord")
            os.startfile(path)

        if "close discord" in query:
            speak("closed discord")
            os.system("taskkill /im Discord.exe")

        if "open youtube music" in query:
            webbrowser.open_new_tab("https://music.youtube.com/")

        if "open google" in query:
            webbrowser.open_new_tab("https://www.google.com/")

        if "open youtube" in query:
            webbrowser.open_new_tab("https://www.youtube.com/")

        if "github" in query:
            webbrowser.open_new_tab("https://github.com/")

        if "teams" in query:
            path = "C:\\Users\\atifu\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            speak("opening teams")
            os.startfile(path)

        if "close teams" in query:
            speak("closed teams")
            os.system("taskkill /f /im Teams.exe")

        if "open calculator" in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            speak("opening calculator")

        if "close calculator" in query:
            speak("closed calculator")
            os.system("taskkill /f /im calc.exe")

        if "open notepad" in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            speak("opening notepad")

        if "close notepad" in query:
            speak("closed notepad")
            os.system("taskkill /f /im notepad.exe")

        if "open wordpad" in query:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
            speak("opening wordpad")

        if "close wordpad" in query:
            speak("closed wordpad")
            os.system("taskkill /f /im write.exe")

        if "call of duty" in query:
            path = "D:\\Call of Duty Advanced Warfare\\s1_sp64_ship.exe"
            speak("opening call of duty")
            os.startfile(path)

        if "close call of duty" in query:
            speak("closed call of duty")
            os.system("taskkill /f /im s1_sp64_ship.exe")

        if "content manager" in query:
            path = "D:\\AssettoCorsav1.16ALLDLCs\\Assetto Corsa\\Assetto Corsa\\Content Manager.exe"
            speak("opening content manager")
            os.startfile(path)

        if "close content manager" in query:
            speak("closed content manager")
            os.system("taskkill /f /im Content Manager.exe")

        if "open steam" in query:
            path = "C:\\Program Files (x86)\\Steam\\steam.exe"
            speak("opening steam")
            os.startfile(path)

        if "steam" in query:
            path = "C:\\Program Files (x86)\\Steam\\steam.exe"
            speak("opening steam")
            os.startfile(path)

        if "close steam" in query:
            speak("closed steam")
            os.system("taskkill /f /im steam.exe")

        if "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'Sir, the time is {strTime}')

        if "wake up" in query:
            speak("at your service SIR")

        if "wikipedia" in query:
            speak("Searching Wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        if "vmware" in query:
            path = "C:\\Program Files (x86)\\VMware\\VMware Workstation\\vmware.exe"
            speak("opening vmware")
            os.startfile(path)

        if "close vmware" in query:
            speak("closed vmware workstation pro 16")
            os.system("taskkill /im vmware.exe")

        if "download" in query:
            speak("opening download manager")
            path = "C:\\Program Files\\Softdeluxe\\Free Download Manager\\fdm.exe"
            os.startfile(path)

        if "close download" in query:
            speak("closed download manager")
            os.system("taskkill /f /im fdm.exe")

        if "alarm" in query:
            # Getting the current path of the script
            path = os.getcwd()

            # Setting up the alarm path
            alarm_path = path + '\Alarm_Tunes'

            # If no directory present, create one.
            if not os.path.isdir(alarm_path):
                os.makedirs(alarm_path)

            # Ask user to add some alarm tunes to the folder.
            while len(os.listdir(alarm_path)) == 0:
                print(
                    "No Alarm Tunes Present. Please add some tunes to the folder before proceeding.")
                confirm = input("Have you added songs? Press Y or N:\t")
                if(confirm == "Y"):
                    print("Good! Let's continue!")
                    continue
                else:
                    continue

            # Finding out the alarm tunes added or removed from the folder
            def List_diff(list1, list2):
                if len(list1) >= len(list2):
                    return (list(set(list1) - set(list2)))
                else:
                    return (list(set(list2) - set(list1)))

            # If no csv file, create the lists with parameters as zero
            if not os.path.isfile("tune_parameters.csv"):
                tune_list = os.listdir(alarm_path)
                tune_time = [60]*len(tune_list)
                tune_counter = [1]*len(tune_list)
                tune_avg = [60]*len(tune_list)
                tune_prob_rev = [1/len(tune_list)]*len(tune_list)
                tune_prob = [1/len(tune_list)]*len(tune_list)

            # If csv file is present, read from csv file
            else:
                tune_df = pd.read_csv("tune_parameters.csv")
                tune_list_os = os.listdir(alarm_path)
                tune_list = list(tune_df['Tunes'])
                tune_diff = List_diff(tune_list_os, tune_list)
                tune_time = list(tune_df['Delay Times'])
                tune_counter = list(tune_df['Count'])
                tune_avg = list(tune_df['Average'])
                tune_prob_rev = list(tune_df['Reverse Probability'])
                tune_prob = list(tune_df['Probability'])

                # If tunes were added
                if len(tune_list_os) >= len(tune_list):
                    for i in range(0, len(tune_diff)):
                        tune_list.append(tune_diff[i])
                        tune_time.append(60)
                        tune_counter.append(1)
                        tune_avg.append(60)
                        tune_prob_rev.append(0.1)
                        tune_prob.append(0.1)

                # If tunes were removed
                else:
                    for i in range(0, len(tune_diff)):
                        tune_diff_index = tune_list.index(tune_diff[i])
                        tune_list.pop(tune_diff_index)
                        tune_time.pop(tune_diff_index)
                        tune_counter.pop(tune_diff_index)
                        tune_avg.pop(tune_diff_index)
                        tune_prob_rev.pop(tune_diff_index)
                        tune_prob.pop(tune_diff_index)

                avg_sum = sum(tune_avg)

                for i in range(0, len(tune_prob_rev)):
                    tune_prob_rev[i] = 1 - tune_avg[i]/avg_sum

                avg_prob = sum(tune_prob_rev)

                for i in range(0, len(tune_prob)):
                    tune_prob[i] = tune_prob_rev[i]/avg_prob

            # Verify whether time entered is correct or not.
            def verify_alarm(hour, minute, seconds):
                if((hour >= 0 and hour <= 23) and (minute >= 0 and minute <= 59) and (seconds >= 0 and seconds <= 59)):
                    return True
                else:
                    return False

            # Asking user to set alarm time and verifying whether true or not.
            while(True):
                hour = int(input("Enter the hour in 24 Hour Format (0-23):\t"))
                minute = int(input("Enter the minutes (0-59):\t"))
                seconds = int(input("Enter the seconds (0-59):\t"))
                if verify_alarm(hour, minute, seconds):
                    break
                else:
                    print("Error: Wrong Time Entered! Please enter again!")

            # Converting the alarm time to seconds
            alarm_sec = hour*3600 + minute*60 + seconds

            # Getting current time and converting it to seconds
            curr_time = datetime.datetime.now()
            curr_sec = curr_time.hour*3600 + curr_time.minute*60 + curr_time.second

            # Calculating the number of seconds left for alarm
            time_diff = alarm_sec - curr_sec

            # If time difference is negative, it means the alarm is for next day.
            if time_diff < 0:
                time_diff += 86400

            # Displaying the time left for alarm
            print("Time left for alarm is %s" %
                  datetime.timedelta(seconds=time_diff))

            # Sleep until the time at which alarm rings
            time.sleep(time_diff)

            print("Alarm time! Wake up! Wake up!")

            # Choose a tune based on probability
            tune_choice_np = np.random.choice(tune_list, 1, tune_prob)
            tune_choice = tune_choice_np[0]

            # Getting the index of chosen tune in list
            tune_index = tune_list.index(tune_choice)

            # Play the alarm tune
            mixer.init()
            mixer.music.load(alarm_path+"/"+tune_choice)

            # Setting loops=-1 to ensure that alarm only stops when user stops it!
            mixer.music.play(loops=-1)

            # Asking user to stop the alarm
            input("Press ENTER to stop alarm")
            mixer.music.stop()

            # Finding the time of stopping the alarm
            time_stop = datetime.datetime.now()
            stop_sec = time_stop.hour*3600 + time_stop.minute*60 + time_stop.second

            # Calculating the time delay
            time_delay = stop_sec - alarm_sec

            # Updating the values
            tune_time[tune_index] += time_delay
            tune_counter[tune_index] += 1
            tune_avg[tune_index] = tune_time[tune_index] / \
                tune_counter[tune_index]

            new_avg_sum = sum(tune_avg)

            for i in range(0, len(tune_list)):
                tune_prob_rev[i] = 1 - tune_avg[i] / new_avg_sum

            new_avg_prob = sum(tune_prob_rev)

            for i in range(0, len(tune_list)):
                tune_prob[i] = tune_prob_rev[i] / new_avg_prob

            # Create the merged list of all six quantities
            tune_rec = [[[[[[]]]]]]

            for i in range(0, len(tune_list)):
                temp = []
                temp.append(tune_list[i])
                temp.append(tune_time[i])
                temp.append(tune_counter[i])
                temp.append(tune_avg[i])
                temp.append(tune_prob_rev[i])
                temp.append(tune_prob[i])
                tune_rec.append(temp)

            tune_rec.pop(0)

            # Convert merged list to a pandas dataframe
            df = pd.DataFrame(tune_rec, columns=[
                              'Tunes', 'Delay Times', 'Count', 'Average', 'Reverse Probability', 'Probability'], dtype=float)

            # Save the dataframe as a csv (if already present, will overwrite the previous one)
            df.to_csv('tune_parameters.csv', index=False)
