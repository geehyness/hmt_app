from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen

class AboutScreen(Screen):  # Ensure it inherits from Screen
    name = StringProperty()  # Define the name property

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='About Screen'))
