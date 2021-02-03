from guizero import App, Text, Picture


def exitGUI():
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
        print("Adios")


app = App("Wanted!")
app.bg = "#A0A0A0" #"#FBFBD0"
wanted_text = Text(app, "DROID")
wanted_text.text_size = 50
wanted_text.font = "Times New Roman"
cat = Picture(app, image="droid.png")
app.when_closed = exitGUI
app.display()