from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class CNSTJunction(App):

def build(self):
    layout = BoxLayout(
        orientation="vertical",
        padding=20,
        spacing=15
    )

    title = Label(
        text="CNST JUNCTION",
        font_size=32
    )

    welcome = Label(
        text="Welcome to CNST Junction!",
        font_size=20
    )

    home = Button(text="Home")
    videos = Button(text="CNST Videos")
    groups = Button(text="Groups")
    messages = Button(text="Messages")
    marketplace = Button(text="Marketplace")

    layout.add_widget(title)
    layout.add_widget(welcome)
    layout.add_widget(home)
    layout.add_widget(videos)
    layout.add_widget(groups)
    layout.add_widget(messages)
    layout.add_widget(marketplace)

    return layout

CNSTJunction().run()
