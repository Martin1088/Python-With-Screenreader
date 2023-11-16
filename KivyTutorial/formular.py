import kivy
from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(GridLayout, self).__init__(**kwargs)
        # colums 
        self.cols = 2
        # add widget 
        self.add_widget(Label^())

class MyApp(App):
    def build(self):
        return Label(text="Here I am")
    
if __name__ == '__main__':
    MyApp().run()
