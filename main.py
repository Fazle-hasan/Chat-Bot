import pywhatkit
import datetime
import wikipedia
import pyjokes

lst = ['google','search on google']     
command = input("Hi Sir,\nHow can i help you?\n ->")
while(1):
        if (command == "stop" or command == "exit"):
                print("Thank you")
                break
                
        # Here we play the song with pywahtkit library
        elif 'play' in command:
                song = command.replace('play', '')
                print("Playing",song)
                pywhatkit.playonyt(song)
                command = input("Task Completed...\n\n\nAny other help\n ->")

        # Here we get the time
        elif 'time' in command:
                time = datetime.datetime.now().strftime('%I:%M %p')
                print('Current time is ' + time)
                command = input("Task Completed...\n\n\nAny other help\n ->")

        # Here search for google
        elif "search on google" in command:
                word = command.replace("search on google", '')
                print("Searching",word)
                pywhatkit.search(word)
                command = input("Task Completed...\n\n\nAny other help\n ->")

        elif 'date' in command:
                print("I have boy Frient so pls don't want a date.")
                command = input("Task Completed...\n\n\nAny other help\n ->")

        elif 'are you single' in command:
                print("I am in a relationship with wifi.")
                command = input("Task Completed...\n\n\nAny other help\n ->")

        elif 'joke' in command:
                print("Telling...")
                pyjokes.get_joke()
                command = input("Task Completed...\n\n\nAny other help\n ->")

        else:
                print("\n\nNot get, Pls rewrite.")
                command = input("->")

        
