from kivy.uix.screenmanager import Screen  # Import Screen
from kivy.uix.label import Label

class HomeScreen(Screen):  # Change to inherit from Screen
    def __init__(self, **kwargs):
        # Extract 'name' from kwargs if it exists
        self.name = kwargs.pop('name', None)  # Remove 'name' from kwargs
        super().__init__(**kwargs)  # Call the parent constructor
        self.orientation = 'vertical'
        self.add_widget(Label(text='Home Screen'))
