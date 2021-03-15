"""file for control fail screen views"""
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string(
    """
<FailScreen>:
    FloatLayout:
        canvas:
            Color:
                rgba: 1,1,1,1
            Rectangle:
                pos: self.pos
                size: (10000, 10000)
        Label:
            text: "Entered password is incorrect."
            color: [1, 0, 0, 1]
            size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.6}
        Label:
            text: "Please try again!"
            color: [1, 0, 0, 1]
            size_hint: (0.3, 0.1)
            pos_hint: {"center_x": 0.5, "center_y": 0.55}
        Button:
            text: 'Try again'
            background_color: [1, 0, 0, 1]
            size_hint: (0.2, 0.05)
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_press: root.manager.current = 'main'
"""
)


class FailScreen(Screen):
    """control fail screen"""

    pass
