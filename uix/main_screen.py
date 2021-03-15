"""file for control main screen views"""
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from tokens import password


Builder.load_string(
    """
<MainScreen>:

    entered_password: entered_password
    
    FloatLayout:
        canvas:
            Color:
                rgba: 1,1,1,1
            Rectangle:
                pos: self.pos
                size: (10000, 10000)
        Image:
            source: "rap_logo.png"
            size_hint: (0.4, 0.4)
            pos_hint: {"center_x": 0.5, "center_y": 0.7}
        TextInput:
            id: entered_password
            text: "Please enter password!"
            background_color: [0, 0, 0, 1]
            cursor_color: [1, 1, 1, 1]
            foreground_color: [1, 1, 1, 1]
            halign: "center"
            border: (1, 1, 1, 1)
            multiline: False
            size_hint: (0.4, 0.05)
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
        Button:
            text: "Show"
            background_color: [0, 0, 0, 1]
            size_hint: (0.2, 0.05)
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            on_press: root.on_press_handler()
        Label:
            text: "©Gayfut"
            color: [0, 0, 0, 1]
            size_hint: (0.3, 0.05)
            pos_hint: {"center_x": 0.5, "center_y": 0.03}
"""
)


class MainScreen(Screen):
    """control main screen"""

    entered_password = ObjectProperty()

    def on_press_handler(self):
        """get password from input and choose what screen will be showing"""
        if self.entered_password.text == password:
            self.manager.current = "result"
        else:
            self.manager.current = "fail"
