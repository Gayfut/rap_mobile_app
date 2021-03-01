from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

from parser.parser import Parser
from settings import PATH_TO_IMAGES


class MainApp(App):
    def build(self):
        layout = FloatLayout()
        with layout.canvas:
            Color(1, 1, 1)
            Rectangle(pos=layout.pos, size=(10000, 10000))

        rap_image = Image(source=f"{PATH_TO_IMAGES}rap_logo.png", size_hint=(.4, .4), pos_hint={'center_x': .5, 'center_y': .7})
        password_input = TextInput(text="Please enter password!", background_color=[0,0,0,1], cursor_color=[1,1,1,1], foreground_color=[1,1,1,1], halign='center', border=(1, 1, 1, 1), multiline=False, size_hint=(.4, .05), pos_hint={'center_x': .5, 'center_y': .4})
        enter_button = Button(text='Show new albums', background_color=[0,0,0,1], size_hint=(.2, .05), pos_hint={'center_x': .5, 'center_y': .3})
        copyright_label = Label(text="Created by Gayfut", color=[0,0,0,1], size_hint=(.3, .05), pos_hint={'center_x': .5, 'center_y': .03})

        layout.add_widget(rap_image)
        layout.add_widget(password_input)
        layout.add_widget(enter_button)
        layout.add_widget(copyright_label)

        enter_button.bind(on_press=self.on_press_button)

        return layout

    def on_press_button(self, instance):
        parser = Parser()
        parser.start_parse(2)
        parser.stop_parse()
