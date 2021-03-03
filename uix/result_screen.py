from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


Builder.load_string(
    """
<ResultScreen>:
    BoxLayout:
        Label:
            text: "Result!"
        Button:
            text: 'Back to main'
            on_press: root.manager.current = 'main'
"""
)


class ResultScreen(Screen):
    pass
