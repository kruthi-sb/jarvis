import pyttsx3
import speech_recognition as sr
import datetime
import bs4
from bs4 import BeautifulSoup as bs
import requests

#weather scrapping:

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}
#The User-Agent (UA) string is contained in the HTTP headers and is intended to identify devices requesting online content. 
# The User-Agent tells the server what the visiting device is (among many other things) and this information can be used to determine what content to return. 
# Of course this requires using a device detection solution which translates UAs into understandable software and hardware information.
url = 'https://www.bbc.com/weather/1277333'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

result1 = soup.find('div', {"class":"wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque", "style":"display:block"})
atmos = result1.text.strip()
#print(atmos) #success!!!!

result2 = soup.find("div", {"class":"wr-value--temperature gel-trafalgar"}).find("span", {"class":"wr-hide-visually"})
temp = result2.text.strip()
#print(temp) #success!!!!

atmos_s = "Today there is " + atmos
temp_s = "and the temperature is" + temp + "Celsius"



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #0 stands for male voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print("usern said -->", query)
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    
    return query


def greet():
    hour = int(datetime.datetime.now().hour) #takes the current hr value
    minutes = int(datetime.datetime.now().minute)
    hr = str(hour)
    m = str(minutes)
    time = "its" + hr + " " + m
    if hour>= 0 and hour<12:
        speak("Good Morning!")
        speak("usern")
        speak(time)
        speak("AM")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!") 
        speak("usern")
        speak(time)
        speak("PM")
    else:
        speak("Good Evening!")
        speak("usern")
        speak(time)
        speak("PM")
    
def weather():
    try:
        try:
            speak(atmos_s)
            speak(temp_s) 
        except Exception:
            try:
                speak(atmos_s)
            except Exception:
                speak(temp_s)
        speak("in Bengaluru")
    except Exception as e:
        print(e)
        speak("I\'m unable to analyze the weather currently!")

def news():
    
    url='https://www.bbc.com/news' # any news portal ,in this case 'BBC'
    response = requests.get(url) # accesing url and creating an object

    soup = bs(response.text, 'html.parser') # pulling HTTP data from the internet
    headlines = soup.find_all('h3') # iterates through object(response) and printing it as a string

    hed = headlines[0:10] # printing the top 10 headlines
    
    for x in hed:
        req = x.text.strip()
        print(req)#printing stripped data
        speak(req)
        
def news_speak():
    try:
        speak("here's the latest news")
        news()
        
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to read the news right now")


def to_do():
    speak("")



def good_morning():
    greet()
    weather()
    news_speak()


good_morning()

    



