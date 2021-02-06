from guizero import App, Text, Picture


def exitGUI():
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()
        print("Adios")


app = App(title="Hello world")
app.bg = "#0000ff"
wanted_text = Text(app, "Hello World")
wanted_text.text_size = 50
app.display()