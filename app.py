from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition, WipeTransition  # Add this import
from kivy.uix.popup import Popup  # Add this import
from screens.home_screen import HomeScreen
from screens.devotional_screen import DevotionalScreen
from screens.community_screen import CommunityScreen
from screens.about_screen import AboutScreen
from screens.contact_screen import ContactScreen

class MyNavigationApp(App):
    def build(self):
        
        sm = ScreenManager(transition=WipeTransition())  # Set the transition here
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(DevotionalScreen(name='devotional'))
        sm.add_widget(CommunityScreen(name='community'))
        sm.add_widget(AboutScreen(name='about'))  # Add this line if missing
        sm.add_widget(ContactScreen(name='contact'))

        layout = BoxLayout(orientation='vertical')  # Change to vertical layout
        header = BoxLayout(size_hint_y=None, height='50dp')  # Header layout
        header.add_widget(Label(text='My App Name', size_hint_x=0.9))  # App name
        header.add_widget(Button(text='☰', size_hint_x=0.1, on_press=self.open_hamburger))  # Hamburger button

        sm_layout = BoxLayout()  # New layout for screens
        sm_layout.add_widget(sm)

        navigation_buttons = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp')  # Bottom navigation
        font_path = './assets/MaterialIconsTwoTone-Regular.otf'  # Update this path
        navigation_buttons.add_widget(Button(text='\uE88A', font_name=font_path, font_size=30, on_press=lambda x: setattr(sm, 'current', 'home')))
        navigation_buttons.add_widget(Button(text='\uE02F', font_name=font_path, font_size=30, on_press=lambda x: setattr(sm, 'current', 'devotional')))
        navigation_buttons.add_widget(Button(text='\uE0BF', font_name=font_path, font_size=30, on_press=lambda x: setattr(sm, 'current', 'community')))
        #navigation_buttons.add_widget(Button(text='\uE5A5', font_name=font_path, font_size=30, on_press=lambda x: setattr(sm, 'current', 'about')))
        navigation_buttons.add_widget(Button(text='\uEB8B', font_name=font_path, font_size=30, on_press=lambda x: setattr(sm, 'current', 'contact')))

        layout.add_widget(header)  # Add header with app name and hamburger
        layout.add_widget(sm_layout)  # Add screen layout
        layout.add_widget(navigation_buttons)  # Add navigation at the bottom

        
        return layout

    def open_hamburger(self, instance):
        # Create a popup for the hamburger menu
        content = BoxLayout(orientation='vertical')
        content.add_widget(Button(text='Home', on_press=lambda x: self.change_screen('home')))
        content.add_widget(Button(text='Devotional', on_press=lambda x: self.change_screen('devotional')))
        content.add_widget(Button(text='Community', on_press=lambda x: self.change_screen('community')))
        content.add_widget(Button(text='About', on_press=lambda x: self.change_screen('about')))
        content.add_widget(Button(text='Contact', on_press=lambda x: self.change_screen('contact')))
        
        
        popup = Popup(title='Menu', content=content, size_hint=(0.5, 0.5))
        popup.open()

    def change_screen(self, screen_name):
        # Change the current screen
        self.root.children[0].current = screen_name
