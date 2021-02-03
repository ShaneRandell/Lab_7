#Lab 7 Importt picture to GUI

from guizero import App, Text, Picture


def exitGUI():    
    
    if app.yesno("Close","Do you want to quit?"):
        app.destroy()
        print("goodbye")
        


app = App("Wanted!") 
app.bg = "#0000ff" 
wanted_text = Text(app, "DROID") 
wanted_text.text_size = 50 
wanted_text.font = "Times New Roman" 
cat = Picture(app, image="/home/pi/Pictures/Droid_giphy.gif")
app.when_closed = exitGUI       
app.display()
