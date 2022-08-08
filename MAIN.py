#############################
#imports:
import pyttsx3 #pyttsx3 is a cross-platform text to speech library which is platform independent.
import tkinter as tk #Tkinter is the most commonly used library for developing GUI (Graphical User Interface) in Python.
from tkinter import * # "*" means all the functions and libraries
from tkinter.ttk import * #"ttk" - This will give you the effects of modern graphics. 
import speech_recognition as sr#To convert speech to text the one and only class we need is the Recognizer class from the speech_recognition module. 
#Depending upon the underlying API used to convert speech to text, the Recognizer class convert our speech to text.
import datetime #used
import wikipedia
import webbrowser
import smtplib
import time
import requests
from bs4 import BeautifulSoup as bs
import pyjokes
from googlesearch import search
###############################

##################
#setting default browser
webbrowser.get(using = 'windows-default')
##################

##################
#setting up pyttsx3 moudule
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #0 stands for male voice
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
###################


###################
#for speech_recognition
def takeCommand(usern):
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(usern, "said -->", query)
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
    
    return query
######################


######################
#FOR NEWS
def news():
    
    url='https://www.bbc.com/news' # any news portal ,in this case 'BBC'
    response = requests.get(url) # accesing url and creating an object

    soup = bs(response.text, 'html.parser') # pulling HTTP data from the internet
    headlines = soup.find("body").find_all('h3') # iterates through object(response) and printing it as a string

    hed = headlines[0:10] # printing the top 10 headlines
    
    for x in hed:
        req = x.text.strip()
        print(req)#printing stripped data
        speak(req)      
#########################

#########################
#weather
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

url = 'https://www.bbc.com/weather/1277333'
response = requests.get(url)
soup = bs(response.text, 'html.parser')

result1 = soup.find('div', {"class":"wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque", "style":"display:block"})
atmos = result1.text.strip()
#print(res1) #success!!!!

result2 = soup.find("div", {"class":"wr-value--temperature gel-trafalgar"}).find("span", {"class":"wr-hide-visually"})
temp = result2.text.strip()
temp = temp[:3]
#print(res2)#success!!!!

atmos_s = "Today there is " + atmos
temp_s = "and the temperature is" + temp + "Celsius"
##############################

##############################
#EMAIL SETUP
def Email(to, content): 
    server = smtplib.SMTP('smtp.gmail.com', 587) # former-'server location' ,latter-'port to be used(specific to server location)'
    server.ehlo() # 'ehlo'- for domain name identification
    server.starttls() # 'start-tls'-security reasons
    server.login('nitupatil.2022@gmail.com','huidblzvwluuetbu') # former-'sender_name', latter-'sender_password'
    server.sendmail('nitupatil.2022@gmail.com',to, content) # ('sender_name','receiver_address','message to deliver')
    server.close() # close the server
################################

################################
#anything new here
#GREET:
def initiate(usern):
    hour = int(datetime.datetime.now().hour) #takes the current hr value
    if hour>= 0 and hour<12:
        speak("Good Morning!")
        speak(usern)
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!") 
        speak(usern) 
    else:
        speak("Good Evening!")
        speak(usern) 
    
    speak("I am Jarvis, your personal Assistant under construction")
    speak("how can I help?") 
###############################


###############################
# THE MAIN FUNCTION        
def all_functions(usern):
    while True:
        #query = input("enter query")
        query = takeCommand(usern)
        query = query.lower()
        #print(query)
        #All the commands said by user will be stored here in 'query' and will be converted to lower case for easy recognition of command

        #wikipedia
        if 'wikipedia' in query: #command format: microsoft wikipedia
            try:
                query = query.replace("wikipedia", "") #removing the word wikipedia from query to make our search smooth
                say = "searching  "+ query +"  on wikipedia"
                speak(say)
                results = wikipedia.summary(query, sentences = 2) #will give the summary in 3 lines of the search result for query
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("sorry, couldn't search on wikipedia")
                speak("you can ask me to search on google")

        #open in webbrowser
        #In Python, webbrowser module is a convenient web browser controller. 
        # It provides a high-level interface that allows displaying Web-based documents to users. 
        elif "open" in query: # command format: open youtube 
            #This works for standard websites like: google, stackoverflow, youtube, coursera, gmail, etc
            query = query.replace("open", "")
            query = query.strip()
            say = "opening" + query
            speak(say)
            try:

                query = "https://www."+query+".com"
                print("opening...\n" , query)
                webbrowser.get(using = 'windows-default').open(query) #using your windows default browser
            
            except Exception as e:
                
                print(e)
                query = "https://www."+query+".org"
                print("opening...\n" , query)
                webbrowser.get(using = 'windows-default').open(query) #using your windows default browser
        
        #google search direct
        elif "in google" in query or "on google" in query: #command format: hey Jarvis search for wormholes in goggle
            #query = "hey Jarvis search for wormholes in goggle"
            try:

                query = query.split(" ")
                j = query.index("for")
                str1 = ""
                query = query[j+1:len(query)-2]
                #print(query)
                for i in query:
                    str1 = str1+ " " +i
                print("searching for", str1, "using google search")
            
                say = "searching for " + str1 + "using google search"
                speak(say)
            
                for i in search(str1, tld="co.in", num=1, stop=1, pause=2):
                    print("taking you to...")
                    print(i)
                    speak("redirecting you to the search results")
                    webbrowser.get(using = 'windows-default').open(i)
            except Exception as e:
                print(e)
                speak("sorry, couldn\'t fetch the results")
                


        # time sleep    
        # Python time sleep function is used to add delay in the execution of a program. 
        # We can use python sleep function to halt the execution of the program for given time in seconds.
        elif "don't listen" in query or "stop listening" in query:
            say = "OK" + usern + "for how much time?" #tell in seconds
            speak(say)
            try:
                a = int(takeCommand(usern))
                time.sleep(a)
                speak("hey! I\'m back, listening to you again...")
            except Exception as e:
                speak("there was an error in the input, I'm sleeping for 30 seconds as default")
                time.sleep(30)
                speak("hey! I\'m back, listening to you again...")
                

        #news    
        elif "read the news" in query or "latest news" in query:
            try:
                speak("Alright, here's the latest news")
                news()
                
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to read the news right now")
        
        #weather
        elif "weather" in query:

            try:
                try:
                    speak(atmos_s)
                    speak(temp_s) 
                except Exception:
                    try:
                        speak(atmos_s)
                    except Exception:
                        speak(temp_s)
                speak("in Bengaluru.")
            except Exception as e:
                print(e)
                speak("I\'m unable to analyze the weather currently!")

        #EMAIL
        elif "send an email" in query:
            try:
                speak("whom should I send? Enter their email address")
                to = input("enter here:")   # receiver's address
                speak("What should I say?")
                content = takeCommand(usern) # to be taken from takecommand()
                while True:
                    speak("confirm the content")
                    confirmation = takeCommand(usern)
                    if "confirm" in confirmation :
                        Email(to, content)
                        speak("OK, Email has been sent !")
                        break
                    else: 
                        speak("OK, tell me the content again")
                        content = takeCommand(usern)

            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        #friendly communication:
        elif "how are you" in query:
            say = "Hey " + usern +"!"
            speak(say)
            speak("I\'m doing great here! how are you?")
            reply = takeCommand(usern)
            if "good" in reply or "fine" in reply or "great" in reply:
                say = "that\'s nice " + usern
                speak(say)
            else:
                say = "Oh! I hope you\'ll get well soon " + "usern"
                speak(say)
                reply = takeCommand(usern) #thank you
                speak("cheer up, have a nice day!")

        elif "what are you doing" in query or "what are you thinking" in query:
            say = "Hey " + usern +"!"
            speak(say)
            speak("I\'m just wondering what's inside a blackhole!")
            speak("do you have any idea?")
            answer = takeCommand(usern)
            speak("Oh I see!") # I wish I could use AI for this :(
            
        elif "created you" in query or "built you" in query or "made you" in query:
            speak("some great minds called Kruthi and Natasha came together to build this masterpiece!")
            speak("thanks to them!!")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "friend" in query: # type: you're my best friend in the world!!
            speak("oh! you melted my heart! Glad to know that!")

        
         




        #exit Jarvis
        #Python interpreter exits from code when exit() is given
        elif 'exit' in query:
            speak("Do you want to exit?")
            confirmation = takeCommand(usern)
            if confirmation == "yes" or confirmation == "Yes":
                speak("OK, this is Jarvis, signing off")
                exit()
            else:
                speak("OK")
                pass

        #end of all_functions()
############################################################################


############################################################################
############################################################################
#main founction starts here:
def main():



    def Result(user_e, pass_e):
        usern = user_e.get()
        input2 = pass_e.get()
        success = "starting Jarvis..."
        if (usern=="kruthi" and input2 == "ironman46") or (usern == "natasha" and input2 == "explorer67"): #to let know jarvis who's the user
            Message(root, text = success).place(x = 330, y = 200)
            greeting = takeCommand(usern)
            if "good morning" in greeting or "Good morning" in greeting:
                #good morining routine call function
                good_morning(usern)
                pass
            else: # if greeting is hi or hello or anything
                initiate(usern)
                all_functions(usern)
                #call your functions here!!!

        else:
            Message(root, text = "Autorisation failed!").place(x = 300, y = 200)


    root = Tk()  #root is the name of the window that opens
    frame = Frame(root).pack()
    root.title("Jarvis Authorisation")
    label = Label(root, text ="Welcome!", font=('calibre',10, 'bold')).pack() #The Pack geometry manager packs widgets in rows or columns.

    root.geometry("400x250") #set size of window

    user_e = tk.StringVar()
    pass_e = tk.StringVar()


    user_name = Label(root, text = "Username").place(x = 40, y = 60)

    user_pass = Label(root, text ="Password").place(x = 40, y = 100)

    user_entry = Entry(root, width = 30, textvariable = user_e).place(x = 110, y = 60)

    pass_entry = Entry(root, width = 30, textvariable = pass_e, show = "*").place(x = 110, y = 100)

    submit_b = Button(root, text ="Submit", command = lambda: Result(user_e, pass_e)).place(x = 160, y = 140) 

    #exit_b = Button(root, text = "Exit", command = root.destroy).place(x = 300, y= 160)#root.destroy is for exitting the window
    root.mainloop()


#main() ends here
#####################################################################################





#####################################################################################
#THEBELOW CODE IS FOR GOOD MORNING ROUTINE ONLY:
#######################################
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
temp = temp[:3]
#print(temp) #success!!!!

atmos_s = "Today there is " + atmos
temp_s = "and the temperature is" + temp + "Celsius"
#######################################

#NOTE: THESE FUNCTIONS ARE DIFFRENT FROM THOSE ABOVE!!!!!!!!!!!!

#######################################
#greet
def greet(usern):
    hour = int(datetime.datetime.now().hour) #takes the current hr value
    minutes = int(datetime.datetime.now().minute)
    hr = str(hour)
    m = str(minutes)
    time = "its" + hr + " " + m
    if hour>= 0 and hour<12:
        speak("Good Morning!")
        speak(usern)
        speak(time)
        speak("AM")
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!") 
        speak(usern)
        speak(time)
        speak("PM")
    else:
        speak("Good Evening!")
        speak(usern)
        speak(time)
        speak("PM")
######################################

#NOTE: THESE FUNCTIONS ARE DIFFRENT FROM THOSE ABOVE!!!!!!!!!!!!

######################################
#weather
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
######################################


######################################
#NEWS
def news():
    
    url='https://www.bbc.com/news' # any news portal ,in this case 'BBC'
    response = requests.get(url) # accesing url and creating an object

    soup = bs(response.text, 'html.parser') # pulling HTTP data from the internet
    headlines = soup.find_all('h3') # iterates through object(response) and printing it as a string

    hed = headlines[0:6] # printing the top 10 headlines
    
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
#######################################



########################################################################
#mix
def good_morning(usern):
    greet(usern)
    weather()
    news_speak()
    say = "Make a great day! " + usern
    speak(say)
########################################################################
################################################################################################
#the main function call
main()
################################################################################################