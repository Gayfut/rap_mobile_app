from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string("""
<MainScreen>:
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
            text: "Show new albums"
            background_color: [0, 0, 0, 1]
            size_hint: (0.2, 0.05)
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            on_press: root.manager.current = 'result'
        Label:
            text: "Created by Gayfut"
            color: [0, 0, 0, 1]
            size_hint: (0.3, 0.05)
            pos_hint: {"center_x": 0.5, "center_y": 0.03}
""")


class MainScreen(Screen):
    pass
