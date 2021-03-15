"""file for control result screen views"""
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from requests import get
from requests.exceptions import ConnectionError

from tokens import site_url


Builder.load_string(
    """
<ResultScreen>:
    BoxLayout:
        orientation: 'vertical'
        canvas:
            Color:
                rgba: 1,1,1,1
            Rectangle:
                pos: self.pos
                size: (10000, 10000)
        Button:
            text: 'Back'
            background_color: [0, 0, 0, 1]
            size_hint: (1, .05)
            on_press: root.manager.current = 'main'
        BoxLayout:
            orientation: 'horizontal'
            size_hint: (1, .05)
            Button:
                text: 'Next'
                background_color: [0, 0, 0, 1]
                on_press: root.next_album()
            Button:
                text: 'Prev'
                background_color: [0, 0, 0, 1]
                on_press: root.prev_album()
        Label:
            text: root.album_title
            color: [0, 0, 0, 1]
            font_size: 10
            size_hint: (1, .1)
        Label:
            text: root.album_rating
            color: [0, 0, 0, 1]
            font_size: 10
            size_hint: (1, .1)
        Label:
            text: root.album_link_to_download
            color: [0, 0, 0, 1]
            font_size: 10
            size_hint: (1, .1)
        Label:
            text: root.album_link_to_album
            color: [0, 0, 0, 1]
            font_size: 10
            size_hint: (1, .1)
        Label:
            text: root.album_track_list
            color: [0, 0, 0, 1]
            font_size: 10
            size_hint: (1, .5)
"""
)


class ResultScreen(Screen):
    """control result screen"""

    album_index = 0
    album_title = StringProperty(defaultvalue="No title")
    album_rating = StringProperty(defaultvalue="No rating")
    album_track_list = StringProperty(defaultvalue="No tracks")
    album_link_to_download = StringProperty(defaultvalue="No download link")
    album_link_to_album = StringProperty(defaultvalue="No link to album")

    def next_album(self):
        """get albums and show next when tap button"""
        albums = self.__get_albums_list()

        try:
            self.album_title = albums[self.album_index + 1]["title"]
            self.album_rating = albums[self.album_index + 1]["rating"]
            self.album_track_list = albums[self.album_index + 1]["track_list"]
            self.album_link_to_download = albums[self.album_index + 1][
                "link_to_download"
            ]
            self.album_link_to_album = albums[self.album_index + 1]["link_to_album"]
        except IndexError:
            self.album_index = 0

        self.album_index += 1

    def prev_album(self):
        """get albums and show previous when tap button"""
        albums = self.__get_albums_list()

        try:
            self.album_title = albums[self.album_index - 1]["title"]
            self.album_rating = albums[self.album_index - 1]["rating"]
            self.album_track_list = albums[self.album_index - 1]["track_list"]
            self.album_link_to_download = albums[self.album_index - 1][
                "link_to_download"
            ]
            self.album_link_to_album = albums[self.album_index - 1]["link_to_album"]
        except IndexError:
            self.album_index = 0

        self.album_index -= 1

    @staticmethod
    def __get_albums_list():
        """get albums info from server and return it"""
        try:
            albums = get(site_url).json()
        except ConnectionError:
            albums = [
                {
                    "title": "No title",
                    "rating": "No rating",
                    "track_list": "No tracks",
                    "link_to_download": "No download link",
                    "link_to_album": "No link to album",
                }
            ]

        return albums
