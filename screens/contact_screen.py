from kivy.uix.screenmanager import Screen  # Add this import
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ContactScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(text='Contact Screen'))
