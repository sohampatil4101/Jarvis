import pyttsx3                    #user defined module(downloaded)
import speech_recognition as sr   #user defined module(downloaded)
import wikipedia                  #user defined module(downloaded)
import pywhatkit                  #user defined module(downloaded)
import datetime                   #in-Built module
import time                       #in-Built module
import webbrowser                 #in-Built module
import os                         #in-Built module(operating system)
import random


                       

#setting of engine to taking voice 
eng=pyttsx3.init('sapi5')
voices=eng.getProperty('voices')
eng.setProperty('voices',voices[0].id)
eng.setProperty('rate',170)

#Speak function (given name as Tobo)
def Tobo(audio):
    print("   ")
    eng.say(audio)
    print("   ")
    eng.runAndWait()

#Function to listening voice command (returning the heared audio in the form of String(text))
def takecommand():
    com=sr.Recognizer()                         #com variable
    with sr.Microphone() as source:
        print("        ")
        print("Listening...")
        com.pause_threshold=1.25
        audio=com.listen(source)

    try:
        print("Recognizing...")
        query=com.recognize_google(audio,language='en-in')     #here we have used google engine AND have set the language english-india
    
    except Exception as ex:
        return "none"
    return query

    

#introducing itself
def myself():
    print("i'm JARVIS, built in 2022. i can look up for answers for you or \nhelp you with find the quickest via home. \nif you need anything just ask, your wish is my command.")
    Tobo("i'm JARVIS, built in 2022. i can look up for answers for you or help you with find the quickest via home. if you need anything just ask, your wish is my command.")
    
#wishing to user
def Wishes():
    time=datetime.datetime.now().hour
    min=datetime.datetime.now().minute
    sec=datetime.datetime.now().second
    if (time>=20 and time<24):
        Tobo("Good night sir")
    elif(time<12):
        Tobo("good morning sir")
    elif(time>=12 and time <=15):
        Tobo("Good afternoon sir")
    else:
        Tobo("good evening sir")
    Tobo("How may i help you ?")

#function to returning the current date
def date():
    dt=time.strftime("%m-%d-%Y")
    print(" -------------------")
    print("|   "+dt+"      |")
    print(" -------------------")
    Tobo(dt)
#function to returning the current time  
def clock():
    print(" -------------------")
    print(time.strftime("|   %I:%M:%S %p     |"))
    print(" -------------------")
    Tobo(time.strftime("%I:%M"))
#function to returning the today's day
def day():
    de=time.strftime("%A")
    print(de)
    Tobo("today is"+de)

def openApp():
    Tobo("tell me the name")
    name=takecommand().lower()
    if (name=='none'):
        Tobo("Sorry! tell me again")
    else:
        Tobo("ok sir, just a second")
        if 'code' in name:
            os.startfile("C:\\Users\\bhoir\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        elif 'notepad' in name:
            os.startfile("C:\\Users\\bhoir\\OneDrive\\Desktop\\Notepad.txt")    
        elif 'word' in name:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
        elif 'exel' in name:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        elif 'powerpoint' in name:
            os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
        elif 'netbeans' in name:
            os.startfile("C:\\Program Files\\NetBeans-15\\netbeans\bin\\netbeans64.exe")
        elif 'crome' in name:
            os.start("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        else :
            Tobo("Sorry !, app is not installed yet")

def playMusic():
    Tobo("tell me the song name")
    musicName=takecommand().lower()

    if 'bappa' in query:
        os.startfile("C:\\Users\\bhoir\\Music\\bappa_song.mp3")
    elif 'arjit' in query:
        os.startfile("C:\\Users\\bhoir\\Music\\best_song_arjit_singh(128kbps).m4a")
    elif 'that should be me' in query:
        os.startfile("")
    else:
        pywhatkit.playonyt(musicName)
    Tobo("Enjoy Sir")

#::::::::::: to play movies :::::::::::
def playMovie():
    print("function will be make soon")

def PlayGames():
    name=takecommand().lower()
    num=random.randint(1,2)
    if(num==1):
        Num_


def SearchHistory():
    Tobo("This is your search history.")
    print("_________________________________________________________")
    print("---------------------------------------------------------")      
    file=open("JarvisSearchHistory.txt","r")
    history=file.read()
    print(history)
    print("_________________________________________________________")
    print("---------------------------------------------------------")
    time.sleep(5)
    file.close()
def SaveHis(query):
    file=open("JarvisSearchHistory.txt","a")
    file.write(query + "       \t\t" + time.strftime("TIME:[ %I:%M %p ]") + "\t" + time.strftime("DATE:[ %m-%d-%Y ]") + "\n\n" ) 
    file.close()

#===============================MAIN FUNCTION======================================================================================================

if __name__ == "__main__":                 
    Wishes()
     
    while True:
        query=takecommand().lower()  #we have converted the query in lowecase to case-sensation
        SaveHis(query)
        print(query)
        #command to asking about itself
        if 'yourself' in query:
            myself()
       
        #command to asking about current timing 
        if 'timing' in query:
            clock()
           
        #command to asking about today's day
        elif 'day' in query:
            day()

        #command to asking about today's date
        elif 'date' in query:
            date()

        #reply to thanks
        elif 'thank' in query:
            Tobo("you'r most welcome sir")
        
        #Jarvis wait , up till the given timing
        elif 'wait' in query:
            Tobo("For how many minutes !")
            min=takecommand().lower()
            if (min=='none'):
                time.sleep(1)
            else:
                min=min.replace("minutes","")
                min=(int)(min.replace("minute",""))
                time.sleep(min*60)
            Tobo("Time out !")
 
        #command to open youtube from web
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
         
        #command to open google from web
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
          
        #command to open facebokk from web
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com")
            
        #command to open watsapp from web
        elif  'open whatsapp' in query:
            webbrowser.open("https://www.whatsapp.com")

        #command to open insta from web
        elif 'open instagram' in query:
            webbrowser.open('https://www.instagram.com')
            
        #command to open telegram from web
        elif 'open telegram' in query:
            webbrowser.open("https://www.telegram.com")

        elif 'open canva' in query:
            webbrowser.open('https://canva.com')

        #to Search perticuler thing on you tube
        elif 'youtube search' in query:
            Tobo('ok sir, This is , i found on search')
            query=query.replace("jarvis","")
            query=query.replace("youtube search","")
            website='https://www.youtube.com/results?search_query='+query
            webbrowser.open(website)
            Tobo("Done sir")
        
        

        #to open the website of given name
        elif 'website' in query:
            Tobo("Launching...")
            query=query.replace("jarvis","")
            query=query.replace("open","")
            query=query.replace("the","")
            query-query.replace(".com","")
            query=query.replace("launch","")
            query=query.replace("website","")
            web1=query.replace(" ","")
            web2='https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Tobo("Launched!")
        
        #to extracting information from Browser
        elif 'wikipedia' in query:
            print("searching wikipedia...")
            query=query.replace("wikipedia","")
            text=wikipedia.summary(query,5)
            print("according to wikipedia,"+text)
            Tobo("according to wikipedia.."+text)
           
        #to Searching perticuler thing on google
        elif 'google search' in query:
            Tobo("Yes Sir, This is what i found on search")
            query=query.replace("jarvis","")
            query=query.replace("google search","")
            pywhatkit.search(query)
            Tobo("done sir")
        
        elif 'app' in query:
            openApp()
        
        elif 'play music' in query:
            playMusic()

        elif 'search history' in query:
            SearchHistory()
        
        elif 'guide' in query:
            Tobo("Dr. Swapna Borde Mam")
            print("Dr. Swapna Borde Mam")

        elif 'none' in query:
            Tobo("please say that again, i couldn't hear the words.")

        #QUIT The JARVIS
        elif 'quit' in query:
            exit()
        elif 'exit' in query:
            exit()

        
        else :
            query=query.replace("jarvis","")
            pywhatkit.search(query)
        
        """def renames(old: StrOrBytesPath, new: StrOrBytesPath)"""
        """def removedirs(old: StrOrBytesPath, new: StrOrBytesPath)"""