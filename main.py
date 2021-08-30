import pyttsx3
import speech_recognition as sr
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import time
import wikipedia
import python_weather
import asyncio
from pygame import mixer
import pandas as pd
import numpy as np

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def time():
    t = time.localtime()
    current_time = time.strftime('%Y/%m/%d %I:%M:%S')
    print(current_time)
    speak(current_time)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

async def getweather():
    # declare the client. format defaults to metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.METRIC)

    # fetch a weather forecast from a city
    weather = await client.find("Bareilly")

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    await client.close()
def currentweather():
    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(getweather())

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)

    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        # speak("Say that again please...")
        return "none"
    return query

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    
    speak("i am jarvis SIR. please tell me how can i help you")

if __name__ == "__main__":
    wish()
    while True:

        query = takecommand().lower()

        # logic buiding for tasks

        if "brave" in query:
            path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            speak("opening brave")
            os.startfile(path)

        if "close brave" in query:
            speak("closed brave")
            os.system("taskkill /im brave.exe")

        if "discord" in query:
            path = "C:\\Users\\atifu\AppData\\Local\\Discord\\app-1.0.9002\\Discord.exe"
            speak("opening discord")
            os.startfile(path)

        if "close discord" in query:
            speak("closed discord")
            os.system("taskkill /im Discord.exe")

        if "music" in query:
            driver_path = "C:/Users/atifu/Documents/Jarvis/chromedriver.exe"
            brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

            option = webdriver.ChromeOptions()
            option.binary_location = brave_path
            # option.add_argument("--incognito") OPTIONAL
            # option.add_argument("--headless") OPTIONAL

            # Create new Instance of Chrome
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

            browser.get("https://music.youtube.com/watch?v=foE1mO2yM04&list=LM")

        if "google" in query:
            driver_path = "C:/Users/atifu/Documents/Jarvis/chromedriver.exe"
            brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

            option = webdriver.ChromeOptions()
            option.binary_location = brave_path
            # option.add_argument("--incognito") OPTIONAL
            # option.add_argument("--headless") OPTIONAL

            # Create new Instance of Chrome
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

            browser.get("https://www.google.com/")

        if "youtube" in query:
            driver_path = "C:/Users/atifu/Documents/Jarvis/chromedriver.exe"
            brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

            option = webdriver.ChromeOptions()
            option.binary_location = brave_path
            # option.add_argument("--incognito") OPTIONAL
            # option.add_argument("--headless") OPTIONAL

            # Create new Instance of Chrome
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

            browser.get("https://www.youtube.com/")

        if "github" in query:
            driver_path = "C:/Users/atifu/Documents/Jarvis/chromedriver.exe"
            brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"

            option = webdriver.ChromeOptions()
            option.binary_location = brave_path
            # option.add_argument("--incognito") OPTIONAL
            # option.add_argument("--headless") OPTIONAL

            # Create new Instance of Chrome
            browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

            browser.get("https://github.com/")

        if "teams" in query:
            path = "C:\\Users\\atifu\\AppData\\Local\\Microsoft\\Teams\\current\\Teams.exe"
            speak("opening teams")
            os.startfile(path)

        if "close teams" in query:
            speak("closed teams")
            os.system("taskkill /im Teams.exe")

        if "calculator" in query:
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            speak("opening calculator")

        if "close calculator" in query:
            speak("closed calculator")
            os.system("taskkill /im calc.exe")

        if "notepad" in query:
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            speak("opening notepad")

        if "close notepad" in query:
            speak("closed notepad")
            os.system("taskkill /im notepad.exe")

        if "wordpad" in query:
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
            speak("opening wordpad")

        if "close wordpad" in query:
            speak("closed wordpad")
            os.system("taskkill /im write.exe")

        if "call of duty" in query:
            path = "D:\\Call of Duty Advanced Warfare\\s1_sp64_ship.exe"
            speak("opening call of duty")
            os.startfile(path)

        if "close call of duty" in query:
            speak("closed call of duty")
            os.system("taskkill /im s1_sp64_ship.exe")
        
        if "content manager" in query:
            path = "D:\\AssettoCorsav1.16ALLDLCs\\Assetto Corsa\\Assetto Corsa\\Content Manager.exe"
            speak("opening content manager")
            os.startfile(path)

        if "close content manager" in query:
            speak("closed content manager")
            os.system("taskkill /im Content Manager.exe")

        
        if "open steam" in query:
            path= "C:\\Program Files (x86)\\Steam\\steam.exe"
            speak("opening steam")
            os.startfile(path)

        if "steam" in query:
            path= "C:\\Program Files (x86)\\Steam\\steam.exe"
            speak("opening steam")
            os.startfile(path)

        if "close steam" in query:
            speak("closed steam")
            os.system("taskkill /im steam.exe")

        if "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

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
            os.system("taskkill /im fdm.exe")

        if "alarm" in query:
            # Getting the current path of the script
            path = os.getcwd()

            # Setting up the alarm path
            alarm_path = path + '\Alarm_Tunes'

            # If no directory present, create one.
            if not os.path.isdir(alarm_path):
                os.makedirs(alarm_path)

            # Ask user to add some alarm tunes to the folder.
            while len(os.listdir(alarm_path))==0:
                print("No Alarm Tunes Present. Please add some tunes to the folder before proceeding.")
                confirm = input("Have you added songs? Press Y or N:\t")
                if(confirm=="Y"):
                    print("Good! Let's continue!")
                    continue
                else:
                    continue

            # Finding out the alarm tunes added or removed from the folder
            def List_diff(list1, list2): 
                if len(list1)>=len(list2):
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
                if len(tune_list_os)>=len(tune_list):
                    for i in range(0,len(tune_diff)):
                        tune_list.append(tune_diff[i])
                        tune_time.append(60)
                        tune_counter.append(1)
                        tune_avg.append(60)
                        tune_prob_rev.append(0.1)
                        tune_prob.append(0.1)
                
                # If tunes were removed
                else:
                    for i in range(0,len(tune_diff)):
                        tune_diff_index = tune_list.index(tune_diff[i])
                        tune_list.pop(tune_diff_index)
                        tune_time.pop(tune_diff_index)
                        tune_counter.pop(tune_diff_index)
                        tune_avg.pop(tune_diff_index)
                        tune_prob_rev.pop(tune_diff_index)
                        tune_prob.pop(tune_diff_index)
                
                avg_sum = sum(tune_avg)
                
                for i in range(0,len(tune_prob_rev)):
                    tune_prob_rev[i] = 1 - tune_avg[i]/avg_sum
                
                avg_prob = sum(tune_prob_rev)
                
                for i in range(0,len(tune_prob)):
                    tune_prob[i] = tune_prob_rev[i]/avg_prob


            # Verify whether time entered is correct or not.
            def verify_alarm(hour,minute,seconds):
                if((hour>=0 and hour<=23) and (minute>=0 and minute<=59) and (seconds>=0 and seconds<=59)):
                    return True
                else:
                    return False

            # Asking user to set alarm time and verifying whether true or not.
            while(True):
                hour = int(input("Enter the hour in 24 Hour Format (0-23):\t"))
                minute = int(input("Enter the minutes (0-59):\t"))
                seconds = int(input("Enter the seconds (0-59):\t"))
                if verify_alarm(hour,minute,seconds):
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

            #If time difference is negative, it means the alarm is for next day.
            if time_diff < 0:
                time_diff += 86400

            # Displaying the time left for alarm
            print("Time left for alarm is %s" % datetime.timedelta(seconds=time_diff))

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
            tune_avg[tune_index] = tune_time[tune_index] / tune_counter[tune_index]

            new_avg_sum = sum(tune_avg)

            for i in range(0,len(tune_list)):
                tune_prob_rev[i] = 1 - tune_avg[i] / new_avg_sum
                
            new_avg_prob = sum(tune_prob_rev)
                
            for i in range(0,len(tune_list)):
                tune_prob[i] = tune_prob_rev[i] / new_avg_prob
                

            #Create the merged list of all six quantities
            tune_rec = [[[[[[]]]]]]

            for i in range (0,len(tune_list)):
                temp=[]
                temp.append(tune_list[i])
                temp.append(tune_time[i])
                temp.append(tune_counter[i])
                temp.append(tune_avg[i])
                temp.append(tune_prob_rev[i])
                temp.append(tune_prob[i])
                tune_rec.append(temp)

            tune_rec.pop(0)

            #Convert merged list to a pandas dataframe
            df = pd.DataFrame(tune_rec, columns=['Tunes','Delay Times','Count','Average','Reverse Probability','Probability'],dtype=float)

            #Save the dataframe as a csv (if already present, will overwrite the previous one)
            df.to_csv('tune_parameters.csv',index=False)