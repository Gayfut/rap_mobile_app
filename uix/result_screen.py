from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from requests import get

from tokens import site_url

Builder.load_string(
    """
<ResultScreen>:
    FloatLayout:
        canvas:
            Color:
                rgba: 1,1,1,1
            Rectangle:
                pos: self.pos
                size: (10000, 10000)
        Button:
            text: 'Back'
            background_color: [0, 0, 0, 1]
            size_hint: (0.05, 0.05)
            pos_hint: {"center_x": 0.95, "center_y": 0.95}
            on_press: root.manager.current = 'main'
"""
)


class ResultScreen(Screen):

    album_info = StringProperty(defaultvalue="No data")

    # def show_album(self):
    #     self.album_info = self.__get_albums_list()
    #
    # @staticmethod
    # def __get_albums_list():
    #     albums = get(site_url)
    #     albums = albums.json()
    #
    #     return albums
