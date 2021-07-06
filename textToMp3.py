import pyttsx3

pyobj=pyttsx3.init()
fo=open("text.txt","r")
ip=fo.read()
fo.close()
pyobj.setProperty("rate",200)
pyobj.setProperty("volume",1)
pyobj.save_to_file(ip,"voice.mp3")
pyobj.runAndWait()