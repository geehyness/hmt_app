from kivy.uix.screenmanager import Screen  # Import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class DevotionalScreen(Screen):  # Ensure DevotionalScreen inherits from Screen
    def __init__(self, **kwargs):
        self.name = kwargs.pop('name', None)  # Extract 'name' from kwargs
        super().__init__(**kwargs)  # Call the parent constructor
        self.orientation = 'vertical'
        self.add_widget(Label(text='Devotional Screen'))
