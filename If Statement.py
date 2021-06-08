
import  pyttsx3

#Ternary if statement.  Use with only one if statement

fname = input("Enter your firstname here: ")
response = pyttsx3.speak("Access granted") if fname == "Ibrahim" else pyttsx3.speak("Access Denied")
